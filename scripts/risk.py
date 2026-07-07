#!/usr/bin/env python3
"""Pre-trade guardrail gate for trader-agent. Standard library only.

This is the SINGLE SOURCE OF TRUTH for risk limits. scripts/alpaca.py refuses to
submit any order that check_order() rejects, so even a confused or hallucinating
agent physically cannot breach the limits in config/risk.yaml.

Limits enforced for new BUY entries:
  - no options / non-equity symbols, ever
  - daily loss cap: no new entries once the day is down past the cap
  - max % of equity per SATELLITE position
  - max new satellite positions per ISO week
The passive core symbol (e.g. SPY) is intentionally exempt from the per-position
and weekly caps, but hard-capped at core_target_pct + rebalance_band_pct.
Sells / closes are always allowed (they reduce risk).
"""
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RISK_FILE = REPO_ROOT / "config" / "risk.yaml"
COUNTERS_FILE = REPO_ROOT / "memory" / "counters.json"

# A plain US equity/ETF ticker: 1-5 uppercase letters, optional .X class suffix.
# Anything else (option OCC symbols, crypto pairs with "/", etc.) is rejected.
_TICKER_RE = re.compile(r"^[A-Z]{1,5}(\.[A-Z])?$")


def _coerce(v):
    v = v.strip().strip('"').strip("'")
    low = v.lower()
    if low in ("true", "false"):
        return low == "true"
    if low in ("null", "none", "~", ""):
        return None
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        return v


def load_yaml(path):
    """Minimal YAML subset parser: flat scalars and single-level lists. No deps."""
    data = {}
    cur = None
    with open(path, "r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.split("#", 1)[0].rstrip()
            if not line.strip():
                continue
            stripped = line.strip()
            if stripped.startswith("- "):
                if cur is not None:
                    if not isinstance(data.get(cur), list):
                        data[cur] = []
                    data[cur].append(_coerce(stripped[2:]))
            elif ":" in line:
                key, _, val = line.partition(":")
                key = key.strip()
                val = val.strip()
                if val == "":
                    data[key] = []
                    cur = key
                else:
                    data[key] = _coerce(val)
                    cur = key
    return data


def load_risk():
    return load_yaml(RISK_FILE)


def _iso_week(d=None):
    iso = (d or date.today()).isocalendar()
    return f"{iso[0]}-W{iso[1]:02d}"


def load_counters():
    """Load machine state, applying an automatic weekly-counter reset on ISO-week rollover."""
    if COUNTERS_FILE.exists():
        c = json.loads(COUNTERS_FILE.read_text(encoding="utf-8"))
    else:
        c = {}
    c.setdefault("inception_equity", None)
    c.setdefault("inception_date", None)
    c.setdefault("spy_inception_price", None)
    c.setdefault("week_of", None)
    c.setdefault("new_positions_this_week", 0)
    c.setdefault("loss_cap_tripped_date", None)
    c.setdefault("last_updated", None)
    wk = _iso_week()
    if c["week_of"] != wk:
        c["week_of"] = wk
        c["new_positions_this_week"] = 0
    return c


def save_counters(c):
    c = {k: v for k, v in c.items() if not k.startswith("_")}  # drop transient keys
    c["last_updated"] = datetime.now().isoformat(timespec="seconds")
    COUNTERS_FILE.write_text(json.dumps(c, indent=2) + "\n", encoding="utf-8")


def is_option_symbol(symbol):
    return not bool(_TICKER_RE.match(symbol.upper()))


def check_order(symbol, side, notional, equity, positions, counters, risk):
    """Return (ok: bool, reason: str). `positions` maps SYMBOL -> {'market_value':float,...}."""
    symbol = symbol.upper()
    side = side.lower()

    if side in ("sell", "close"):
        return True, "sell/close is risk-reducing; allowed"

    # 1. No options / non-equity symbols, ever.
    if not risk.get("allow_options", False) and is_option_symbol(symbol):
        return False, f"{symbol} is not a plain US equity/ETF ticker (options/derivatives hard-blocked)"

    equity = float(equity)
    notional = float(notional)
    held = float(positions.get(symbol, {}).get("market_value", 0) or 0)
    proposed = held + notional

    # 2. Passive core: exempt from satellite caps, but hard-capped near its target.
    core_symbol = str(risk.get("core_symbol", "SPY")).upper()
    if symbol == core_symbol:
        core_max = float(risk.get("core_target_pct", 70)) + float(risk.get("rebalance_band_pct", 10))
        limit = equity * core_max / 100.0
        if proposed > limit + 1e-6:
            return False, f"core {symbol} would be {proposed/equity*100:.1f}% of equity; hard cap {core_max}%"
        return True, "core position (exempt from satellite caps)"

    # 3. Daily loss cap -> no new entries once the day is down past the cap.
    cap = float(risk.get("daily_loss_cap_pct", 3))
    day_pl_pct = counters.get("_day_pl_pct")
    if day_pl_pct is not None and float(day_pl_pct) <= -cap:
        return False, f"daily loss cap hit ({float(day_pl_pct):+.2f}% <= -{cap}%): no new entries today"

    # 4. Per-position size cap (existing + new must stay within max_position_pct).
    maxpct = float(risk.get("max_position_pct", 5))
    limit = equity * maxpct / 100.0
    if proposed > limit + 1e-6:
        return False, (f"position cap: {symbol} would be ${proposed:,.0f} "
                       f"({proposed/equity*100:.1f}% of ${equity:,.0f}); max {maxpct}% = ${limit:,.0f}")

    # 5. Weekly new-position cap (only counts brand-new satellite symbols).
    is_new = held <= 0
    maxnew = int(risk.get("max_new_positions_per_week", 3))
    opened = int(counters.get("new_positions_this_week", 0))
    if is_new and opened >= maxnew:
        return False, f"weekly cap: already opened {opened}/{maxnew} new positions this ISO week"

    return True, "ok"


def _cli_status():
    """Human-readable snapshot of current guardrail state. Imports alpaca lazily."""
    import alpaca
    risk = load_risk()
    counters = load_counters()
    acct = alpaca.get_account()
    equity = float(acct["equity"])
    last_eq = float(acct.get("last_equity", equity) or equity)
    day_pl_pct = (equity - last_eq) / last_eq * 100 if last_eq else 0.0
    positions = alpaca.positions_map()
    cap = float(risk["daily_loss_cap_pct"])
    print("---- guardrail status ----")
    print(f"equity                 ${equity:,.2f}")
    print(f"day P&L                {day_pl_pct:+.2f}%   (loss cap -{cap}%)  "
          f"{'** HALTED **' if day_pl_pct <= -cap else 'ok'}")
    print(f"open positions         {len(positions)}")
    print(f"new positions this wk  {counters['new_positions_this_week']}/"
          f"{risk['max_new_positions_per_week']}  (week {counters['week_of']})")
    print(f"max per position       {risk['max_position_pct']}% = ${equity*risk['max_position_pct']/100:,.0f}")
    print(f"core target            {risk['core_target_pct']}% {risk['core_symbol']}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "status":
        _cli_status()
    else:
        print("usage: python risk.py status")

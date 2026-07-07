#!/usr/bin/env python3
"""Zero-dependency Alpaca REST client + CLI for trader-agent (standard library only).

Credentials are read from the ENVIRONMENT, never from a .env file:
  ALPACA_API_KEY_ID, ALPACA_API_SECRET_KEY, ALPACA_PAPER (default "1" = paper).

Every order-placing command runs through risk.check_order() first and refuses to
submit anything that breaches config/risk.yaml.

Examples:
  python scripts/alpaca.py account
  python scripts/alpaca.py clock
  python scripts/alpaca.py positions
  python scripts/alpaca.py quote NVDA
  python scripts/alpaca.py buy SPY --pct 70                 # establish core (no trailing stop)
  python scripts/alpaca.py buy NVDA --pct 4 --trail-percent 10
  python scripts/alpaca.py buy NVDA --pct 6 --dry-run       # -> REJECTED (over 5% cap)
  python scripts/alpaca.py stop NVDA --trail-percent 8      # tighten stop on a winner
  python scripts/alpaca.py sell NVDA --all                  # cut a loser
"""
import argparse
import json
import math
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import risk  # same directory (scripts/)

PAPER = os.environ.get("ALPACA_PAPER", "1") not in ("0", "false", "False", "")
TRADE_BASE = "https://paper-api.alpaca.markets" if PAPER else "https://api.alpaca.markets"
DATA_BASE = "https://data.alpaca.markets"

KEY = os.environ.get("ALPACA_API_KEY_ID", "")
SECRET = os.environ.get("ALPACA_API_SECRET_KEY", "")


def _headers():
    if not KEY or not SECRET:
        sys.exit("ERROR: ALPACA_API_KEY_ID / ALPACA_API_SECRET_KEY not set in the environment. "
                 "Set them in your shell (local) or cloud secrets (remote) -- never in a committed file.")
    return {
        "APCA-API-KEY-ID": KEY,
        "APCA-API-SECRET-KEY": SECRET,
        "Content-Type": "application/json",
    }


def _request(method, base, path, params=None, body=None):
    url = base + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=_headers(), method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raise SystemExit(f"Alpaca API {e.code} on {method} {path}: {e.read().decode()}")
    except urllib.error.URLError as e:
        raise SystemExit(f"Network error on {method} {path}: {e.reason}")


# ---- data helpers ----
def get_account():
    return _request("GET", TRADE_BASE, "/v2/account")


def get_clock():
    return _request("GET", TRADE_BASE, "/v2/clock")


def get_positions():
    return _request("GET", TRADE_BASE, "/v2/positions")


def get_open_orders():
    return _request("GET", TRADE_BASE, "/v2/orders", params={"status": "open"})


def positions_map():
    out = {}
    for p in get_positions():
        out[p["symbol"].upper()] = {
            "qty": float(p["qty"]),
            "market_value": float(p["market_value"]),
            "avg_entry": float(p["avg_entry_price"]),
            "unrealized_plpc": float(p["unrealized_plpc"]) * 100,
        }
    return out


def get_latest_price(symbol):
    j = _request("GET", DATA_BASE, f"/v2/stocks/{symbol.upper()}/trades/latest",
                 params={"feed": "iex"})
    return float(j["trade"]["p"])


# ---- order helpers ----
def submit_order(symbol, qty=None, side="buy", type="market",
                 time_in_force="day", trail_percent=None, limit_price=None):
    body = {"symbol": symbol.upper(), "side": side, "type": type, "time_in_force": time_in_force}
    if qty is not None:
        body["qty"] = str(qty)
    if trail_percent is not None:
        body["type"] = "trailing_stop"
        body["trail_percent"] = str(trail_percent)
    if limit_price is not None:
        body["type"] = "limit"
        body["limit_price"] = str(limit_price)
    return _request("POST", TRADE_BASE, "/v2/orders", body=body)


def close_position(symbol):
    return _request("DELETE", TRADE_BASE, f"/v2/positions/{symbol.upper()}")


def _wait_for_fill(order_id, timeout=15):
    end = time.time() + timeout
    while time.time() < end:
        o = _request("GET", TRADE_BASE, f"/v2/orders/{order_id}")
        if o.get("status") == "filled":
            return float(o.get("filled_qty") or 0)
        time.sleep(1)
    return None


# ---- command handlers ----
def cmd_account(_):
    a = get_account()
    for k in ("status", "equity", "last_equity", "cash", "buying_power",
              "portfolio_value", "pattern_day_trader"):
        if k in a:
            print(f"{k:<18} {a[k]}")


def cmd_clock(_):
    c = get_clock()
    print(f"is_open   {c.get('is_open')}")
    print(f"timestamp {c.get('timestamp')}")
    print(f"next_open {c.get('next_open')}")
    print(f"next_close {c.get('next_close')}")


def cmd_positions(_):
    pm = positions_map()
    if not pm:
        print("(no open positions)")
        return
    for sym, p in sorted(pm.items()):
        print(f"{sym:<6} {p['qty']:>9.2f} sh  ${p['market_value']:>11,.0f}  "
              f"avg ${p['avg_entry']:.2f}  {p['unrealized_plpc']:+.1f}%")


def cmd_orders(_):
    oo = get_open_orders()
    if not oo:
        print("(no open orders)")
        return
    for o in oo:
        print(f"{o['symbol']:<6} {o['side']:<4} {o['type']:<14} "
              f"qty {o.get('qty')} trail {o.get('trail_percent')} status {o['status']} id {o['id']}")


def cmd_quote(args):
    print(f"{args.symbol.upper()} last ${get_latest_price(args.symbol):.2f}")


def cmd_buy(args):
    symbol = args.symbol.upper()
    acct = get_account()
    equity = float(acct["equity"])
    last_eq = float(acct.get("last_equity", equity) or equity)
    positions = positions_map()
    counters = risk.load_counters()
    counters["_day_pl_pct"] = (equity - last_eq) / last_eq * 100 if last_eq else 0.0
    r = risk.load_risk()

    if args.notional:
        notional = float(args.notional)
    elif args.pct:
        notional = equity * float(args.pct) / 100.0
    else:
        sys.exit("buy requires --notional or --pct")

    ok, reason = risk.check_order(symbol, "buy", notional, equity, positions, counters, r)
    print(f"[risk] {'PASS' if ok else 'REJECT'}: {reason}")
    if not ok:
        sys.exit(1)

    price = get_latest_price(symbol)
    qty = math.floor(notional / price)
    if qty < 1:
        sys.exit(f"notional ${notional:,.0f} is < 1 share of {symbol} at ${price:.2f}")

    core = str(r.get("core_symbol", "SPY")).upper()
    trail = args.trail_percent
    if trail is None and symbol != core:
        trail = float(r.get("default_trail_percent", 10))

    if args.dry_run:
        print(json.dumps({"dry_run": True, "symbol": symbol, "qty": qty, "price": round(price, 2),
                          "notional": round(qty * price, 2), "trail_percent": trail}, indent=2))
        return

    order = submit_order(symbol, qty=qty, side="buy", type="market")
    print(f"[buy] market buy {qty} {symbol} (~${qty*price:,.0f}) submitted, order {order['id']}")

    # Count a brand-new satellite position against the weekly cap.
    if symbol != core and positions.get(symbol, {}).get("qty", 0) <= 0:
        counters["new_positions_this_week"] = int(counters.get("new_positions_this_week", 0)) + 1
    risk.save_counters(counters)

    if trail:
        filled = _wait_for_fill(order["id"], timeout=15)
        stop = submit_order(symbol, qty=int(filled or qty), side="sell",
                            type="trailing_stop", time_in_force="gtc", trail_percent=trail)
        print(f"[stop] trailing stop {trail}% placed on {symbol}, order {stop['id']}")
    elif symbol == core:
        print("[stop] core position: no trailing stop (buy-and-hold)")


def cmd_sell(args):
    symbol = args.symbol.upper()
    if args.dry_run:
        print(json.dumps({"dry_run": True, "sell": symbol,
                          "qty": "ALL" if args.all else args.qty}, indent=2))
        return
    if args.all:
        print(json.dumps(close_position(symbol), indent=2)[:400])
        print(f"[sell] closed entire {symbol} position")
        return
    if not args.qty:
        sys.exit("sell requires --qty or --all")
    o = submit_order(symbol, qty=args.qty, side="sell", type="market")
    print(f"[sell] market sell {args.qty} {symbol}, order {o['id']}")


def cmd_stop(args):
    symbol = args.symbol.upper()
    pos = positions_map().get(symbol)
    if not pos:
        sys.exit(f"no open position in {symbol}")
    if args.dry_run:
        print(json.dumps({"dry_run": True, "trailing_stop": symbol,
                          "trail_percent": args.trail_percent, "qty": pos["qty"]}, indent=2))
        return
    o = submit_order(symbol, qty=int(pos["qty"]), side="sell",
                     type="trailing_stop", time_in_force="gtc", trail_percent=args.trail_percent)
    print(f"[stop] trailing stop {args.trail_percent}% on {symbol}, order {o['id']}")


def main():
    ap = argparse.ArgumentParser(prog="alpaca.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("account")
    sub.add_parser("clock")
    sub.add_parser("positions")
    sub.add_parser("orders")
    q = sub.add_parser("quote"); q.add_argument("symbol")

    b = sub.add_parser("buy"); b.add_argument("symbol")
    b.add_argument("--notional", type=float)
    b.add_argument("--pct", type=float, help="percent of total equity")
    b.add_argument("--trail-percent", type=float, dest="trail_percent")
    b.add_argument("--dry-run", action="store_true")

    s = sub.add_parser("sell"); s.add_argument("symbol")
    s.add_argument("--qty", type=float)
    s.add_argument("--all", action="store_true")
    s.add_argument("--dry-run", action="store_true")

    st = sub.add_parser("stop"); st.add_argument("symbol")
    st.add_argument("--trail-percent", type=float, dest="trail_percent", required=True)
    st.add_argument("--dry-run", action="store_true")

    args = ap.parse_args()
    handlers = {
        "account": cmd_account, "clock": cmd_clock, "positions": cmd_positions,
        "orders": cmd_orders, "quote": cmd_quote, "buy": cmd_buy,
        "sell": cmd_sell, "stop": cmd_stop,
    }
    handlers[args.cmd](args)


if __name__ == "__main__":
    main()

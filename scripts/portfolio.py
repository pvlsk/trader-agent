#!/usr/bin/env python3
"""Portfolio snapshot + benchmark vs SPY since inception. Standard library only.

On first run it records the inception equity, date, and SPY price into
memory/counters.json, then every run compares portfolio total return against
SPY total return over the same window -- the actual "did we beat the index" number.
"""
from datetime import date

import alpaca
import risk


def main():
    acct = alpaca.get_account()
    equity = float(acct["equity"])
    cash = float(acct["cash"])
    last_eq = float(acct.get("last_equity", equity) or equity)
    counters = risk.load_counters()

    changed = False
    if not counters.get("inception_equity"):
        counters["inception_equity"] = equity
        counters["inception_date"] = date.today().isoformat()
        changed = True
    if not counters.get("spy_inception_price"):
        counters["spy_inception_price"] = alpaca.get_latest_price("SPY")
        changed = True
    if changed:
        risk.save_counters(counters)

    inc_eq = float(counters["inception_equity"])
    spy0 = float(counters["spy_inception_price"])
    spy_now = alpaca.get_latest_price("SPY")
    port_ret = (equity - inc_eq) / inc_eq * 100 if inc_eq else 0.0
    spy_ret = (spy_now - spy0) / spy0 * 100 if spy0 else 0.0
    day_pl = (equity - last_eq) / last_eq * 100 if last_eq else 0.0

    line = "=" * 52
    print(line)
    print(f" trader-agent portfolio   {date.today().isoformat()}")
    print(line)
    print(f" Equity              ${equity:,.2f}")
    print(f" Cash                ${cash:,.2f}")
    print(f" Day P&L             {day_pl:+.2f}%")
    print(f" Since inception     {port_ret:+.2f}%   (from {counters['inception_date']})")
    print(f" SPY same period     {spy_ret:+.2f}%")
    print(f" ALPHA vs SPY        {port_ret - spy_ret:+.2f}%   <- goal: positive")
    print("-" * 52)
    pm = alpaca.positions_map()
    if not pm:
        print(" (no open positions)")
    for sym, p in sorted(pm.items()):
        print(f" {sym:<6} {p['qty']:>8.2f} sh  ${p['market_value']:>11,.0f}  {p['unrealized_plpc']:+.1f}%")
    print(line)


if __name__ == "__main__":
    main()

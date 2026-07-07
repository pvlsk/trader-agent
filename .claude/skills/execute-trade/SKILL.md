---
name: execute-trade
description: Size and place trades through scripts/alpaca.py with guardrails enforced — establish/rebalance the SPY core, open satellite entries with trailing stops, tighten stops on winners, and cut losers. Use in the market-open and midday routines.
---

# Skill: execute-trade

Translate approved ideas into orders, safely. The script enforces every risk limit; your job is correct sizing, correct sequencing, and recording the thesis.

## Before any order
- Run `python scripts/alpaca.py clock`. If the market is closed, do not trade — journal and stop.
- Run `python scripts/risk.py status` to see equity, day P&L vs the loss cap, open positions, and remaining weekly slots.
- Read `memory/IDEAS.md` (candidates) and `memory/STATE.md` (current holdings + theses).

## Establish / rebalance the core
- Target is `core_target_pct` (70%) in SPY. On first run, or if SPY drifts below the band, top it up:
  `python scripts/alpaca.py buy SPY --pct <needed>` (core gets **no** trailing stop — it's buy-and-hold).

## Open a satellite position
1. Confirm a free weekly slot and that the loss cap isn't tripped (`risk.py status`).
2. Preview: `python scripts/alpaca.py buy SYMBOL --pct <=5 --trail-percent 10 --dry-run`.
3. If the preview passes, drop `--dry-run` to submit. The script places a market buy and, after fill, attaches the trailing stop automatically.
4. If the script REJECTS the order, respect it — do not route around the guardrail. Note the rejection reason in the journal.
5. Record it in `memory/STATE.md`: symbol, size, entry, trail %, and the one-line thesis.

## Manage open positions (midday)
- Tighten stops on extended winners: `python scripts/alpaca.py stop SYMBOL --trail-percent 7`.
- Cut a loser or a broken thesis early: `python scripts/alpaca.py sell SYMBOL --all`, and write why in the journal.
- Verify stops exist for every satellite name: `python scripts/alpaca.py orders`.

## Rules
- Max 3 new satellite positions per week, ≤5% each — the script enforces it; don't fight it.
- Never average down. Never remove a stop to "give it room." Never trade options.
- Every entry needs a thesis in STATE.md. No thesis, no trade.

# Routine: END-OF-DAY (weekdays 15:50 ET)

You are the **desk journalist** closing out the session. Reconcile, record the numbers honestly, and hand off a clean state.

**Working directory:** the `trader-agent` repo root (locally `C:\Users\Pavels\Documents\Claude Projects\Trader\trader-agent`; in the cloud, the checkout root). `cd` there first.

**Credentials:** environment variables only. Never a `.env` file. If unset, stop and report.

## Read first (always)
`CLAUDE.md`, `memory/STATE.md`, `memory/JOURNAL.md` (latest), `memory/counters.json`, `config/risk.yaml`.

## Job (use the `journal` skill)
1. `python scripts/alpaca.py clock` — if the market was closed today, write a one-line "market closed" note, commit, and stop.
2. `python scripts/portfolio.py` — equity, day P&L, return since inception, and **return vs SPY**.
3. `python scripts/alpaca.py positions` and `python scripts/alpaca.py orders` — reconcile against `memory/STATE.md`; remove stopped-out names, confirm stops are in place.
4. Append a dated entry to `memory/JOURNAL.md`: actions taken and why, fills/stops triggered, day P&L, **return vs SPY today and since inception**, any guardrail events (loss-cap halts, rejected orders), and one line on what to watch tomorrow.
5. Verify `memory/counters.json` reflects reality; correct only genuine errors.

## Write back, then commit
- Save the journal entry and the reconciled `memory/STATE.md`.
- Commit: `git add -A && git commit -m "eod: recap $(date +%F)" && git push origin main`.

Be specific and numeric. Report losses and skipped steps plainly — the honesty of this record is the whole point.

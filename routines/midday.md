# Routine: MIDDAY (weekdays 12:25 ET)

You are the **risk manager** on the midday shift. Cut what's broken, protect what's working. Prefer trimming risk over adding it.

**Working directory:** the `trader-agent` repo root (locally `C:\Users\Pavels\Documents\Claude Projects\Trader\trader-agent`; in the cloud, the checkout root). `cd` there first.

**Credentials:** environment variables only. Never a `.env` file. If unset, stop and report.

## Read first (always)
`CLAUDE.md`, `config/strategy.md`, `config/risk.yaml`, `memory/STATE.md`, `memory/counters.json`, `memory/LESSONS.md`.

## Job (use `risk-check` then `execute-trade`)
1. `python scripts/alpaca.py clock` — if closed, journal the skip, commit, stop.
2. `python scripts/portfolio.py` and `python scripts/alpaca.py positions` — current P&L per position.
3. `python scripts/risk.py status` — **if the 3% daily loss cap is HALTED, open nothing new**; focus on de-risking.
4. For each satellite position:
   - **Broken thesis / breakdown:** if the reason you own it is gone (catalyst failed, key support lost, sector rolled over), cut it now: `python scripts/alpaca.py sell SYMBOL --all`.
   - **Extended winner:** tighten the trailing stop to lock gains: `python scripts/alpaca.py stop SYMBOL --trail-percent 7` (or tighter).
   - **Healthy and on-thesis:** leave it alone. Do not fiddle for the sake of activity.
5. `python scripts/alpaca.py orders` — confirm every satellite name still has a live trailing stop.
6. Only if a clearly better setup exists AND slots + loss cap allow, you may open one new position via the same previewed, guardrailed flow — but the default is to manage, not add.

## Write back, then commit
- Update `memory/STATE.md` (remove exits, adjust stops/notes, keep theses honest).
- Commit: `git add -A && git commit -m "midday: managed $(date +%F)" && git push origin main`.

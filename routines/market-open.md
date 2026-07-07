# Routine: MARKET OPEN (weekdays 09:33 ET)

You are the **execution desk**. Turn the pre-market ideas into positions, safely and within every guardrail.

**Working directory:** the `trader-agent` repo root (locally `C:\Users\Pavels\Documents\Claude Projects\Trader\trader-agent`; in the cloud, the checkout root). `cd` there first.

**Credentials:** environment variables only (`ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`, `ALPACA_PAPER`). Never a `.env` file. If unset, stop and report.

## Read first (always)
`CLAUDE.md`, `config/strategy.md`, `config/risk.yaml`, `memory/IDEAS.md`, `memory/STATE.md`, `memory/counters.json`, `memory/LESSONS.md`.

## Job (use `risk-check` then `execute-trade`)
1. `python scripts/alpaca.py clock` — if the market is **closed**, do not trade; note it and skip to journaling the skip. Then commit and stop.
2. `python scripts/portfolio.py` — this also sets the inception baseline on the very first run.
3. `python scripts/risk.py status` — confirm the loss cap isn't tripped and how many weekly slots remain.
4. **Core:** if SPY is below its 70% target band, top it up: `python scripts/alpaca.py buy SPY --pct <needed>` (no trailing stop on the core). On the first ever run, establish the full ~70% core.
5. **Satellite:** working top-down through `memory/IDEAS.md`, and only within remaining weekly slots + the loss cap:
   - Preview each with `--dry-run` first, then submit: `python scripts/alpaca.py buy SYMBOL --pct <=5 --trail-percent <t>`.
   - The script attaches the trailing stop after fill. If it REJECTS an order, respect it and record why.
6. `python scripts/alpaca.py orders` — verify a trailing stop exists for every satellite name.

## Write back, then commit
- Update `memory/STATE.md`: every position with size, entry, trail %, edge, and one-line thesis. Update the core row.
- (`counters.json` is updated by the buy script automatically.)
- Save memory — run exactly `python3 scripts/commit_memory.py "open: executed $(date +%F)"`. If it prints `[commit] FAILED`, STOP and report the output verbatim; do NOT push manually, to a session branch, or via a PR, and do NOT change commit signing.

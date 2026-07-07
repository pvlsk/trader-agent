# trader-agent

An autonomous, memory-driven **swing-trading desk** on an Alpaca **paper** account. Goal: **beat SPY total return over the long run** with a core–satellite strategy (70% passive SPY core + 30% tactical sleeve). Five scheduled routines act as the desk; they read shared memory, act, and commit updates back to `main`.

> ⚠️ **Paper trading only.** No real money until a sustained, disciplined track record exists. No options, ever.

## How it works

```
Pre-market → Market open → Midday → End-of-day → (Fri) Weekly review
   research     execute       manage     recap         grade
        \___________ shared memory in memory/ ___________/
```

Every routine: **reads** `config/*` + `memory/*` → **checks the market** (`alpaca.py clock`) → **does its job** through the scripts/skills → **writes** `memory/*` → **commits & pushes**.

Hard risk limits live in **code** (`scripts/risk.py`, driven by `config/risk.yaml`), not in prompts, so no run can breach them: max 5%/position, 3% daily loss cap, 3 new positions/week, no options. The SPY core is the only intentionally large holding.

## Layout
- `scripts/` — zero-dependency Python (stdlib only): `alpaca.py` (REST client + CLI), `risk.py` (guardrail gate), `portfolio.py` (snapshot + SPY benchmark).
- `config/` — `risk.yaml` (limits), `strategy.md` (the plan), `universe.yaml` (what we may trade).
- `.claude/skills/` — reusable behaviors: research, execute-trade, journal, risk-check.
- `memory/` — `STATE.md`, `IDEAS.md`, `JOURNAL.md`, `WEEKLY.md`, `LESSONS.md`, `counters.json`.
- `routines/` — the exact prompt each scheduled run executes.

## Setup (local)

Requires Python 3.12+ and git.

```bash
# 1. Provide credentials via ENVIRONMENT VARIABLES (never a committed file).
#    PowerShell:
$env:ALPACA_API_KEY_ID    = "<your paper key>"
$env:ALPACA_API_SECRET_KEY= "<your paper secret>"
$env:ALPACA_PAPER         = "1"
#    bash:
export ALPACA_API_KEY_ID=<your paper key>
export ALPACA_API_SECRET_KEY=<your paper secret>
export ALPACA_PAPER=1

# 2. Smoke-test
python scripts/alpaca.py account          # should print ~100000 equity
python scripts/portfolio.py               # snapshot + SPY benchmark
python scripts/alpaca.py buy NVDA --pct 6 --dry-run   # should be REJECTED (over 5% cap)
```

## Scheduling (ET; markets are ET so no conversion)
| Routine | Cron | Time |
|---|---|---|
| Pre-market | `5 8 * * 1-5` | 8:05 |
| Market open | `33 9 * * 1-5` | 9:33 |
| Midday | `25 12 * * 1-5` | 12:25 |
| End-of-day | `50 15 * * 1-5` | 15:50 |
| Weekly review | `15 16 * * 5` | Fri 16:15 |

## Running truly 24/7 (Claude Code web)
The local scheduler only fires while the desktop app is open. For genuine round-the-clock operation, run the routines in **Claude Code on the web** (claude.ai/code):
1. Connect this GitHub repo to a cloud environment.
2. Add environment **secrets**: `ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`, `ALPACA_PAPER=1`. (Secrets live in the cloud, not the repo.)
3. Create one scheduled routine per file in `routines/`, on the cron above.
4. In each routine's permissions, enable **"allow unrestricted branch pushes"** so it can commit memory back to `main`.

## Safety
- Secrets come from the environment only; `.gitignore` blocks `.env`. Run a secret scan before any push.
- Guardrails are enforced in `risk.py` — do not bypass by calling the API directly.
- This is paper money. Treat the track record honestly; that's the whole value.

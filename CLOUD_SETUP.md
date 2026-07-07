# Running trader-agent truly 24/7 (Claude Code for web)

The local desktop scheduler only fires while the app is open. To run genuinely 24/7, independent of your machine, host the five routines as **scheduled cloud agents on Claude Code for web** (claude.ai/code). The repo, scripts, skills, and routine prompts already run unchanged there. This is a UI-driven, one-time setup you perform with your own GitHub login.

> ⚠️ **Do not run local and cloud at the same time.** Both would trade the same account and both push to `main`, causing duplicate orders and git conflicts. The **last step** here is to disable the five local scheduled tasks. Keep them on only until the cloud version is confirmed working.

## 1. Connect the repo
1. Go to **claude.ai/code** and sign in.
2. Connect **GitHub** and grant access to the private repo **`pvlsk/trader-agent`**.
3. Create a **cloud environment** for that repo (it clones the repo into a Linux sandbox with network access).

## 2. Add the secrets (this is where your keys live in the cloud)
In the environment's **Secrets / Environment variables** settings, add the same three values currently in your local `.env`:
- `ALPACA_API_KEY_ID`
- `ALPACA_API_SECRET_KEY`
- `ALPACA_PAPER` = `1`

These live in the cloud secret store, never in the repo. The scripts read them from the environment automatically.

## 3. Create the five scheduled routines
Create one scheduled routine per file below. For each, the **prompt** is simply:

> Follow the instructions in `routines/<file>` exactly. Read the memory and config files first, do the job, update memory, then commit and push to `main`.

Set the schedule in the **America/New_York** timezone if the UI offers a timezone (recommended — it handles daylight saving automatically). If it only accepts **UTC** cron, use the UTC column, and note the DST caveat below.

| Routine | Prompt file | New York time | Cron (America/New_York) | Cron (UTC, EDT) |
|---|---|---|---|---|
| Pre-market | `routines/premarket.md` | 08:05 Mon–Fri | `5 8 * * 1-5` | `5 12 * * 1-5` |
| Market open | `routines/market-open.md` | 09:33 Mon–Fri | `33 9 * * 1-5` | `33 13 * * 1-5` |
| Midday | `routines/midday.md` | 12:25 Mon–Fri | `25 12 * * 1-5` | `25 16 * * 1-5` |
| End-of-day | `routines/end-of-day.md` | 15:50 Mon–Fri | `50 15 * * 1-5` | `50 19 * * 1-5` |
| Weekly review | `routines/friday-review.md` | 16:15 Fri | `15 16 * * 5` | `15 20 * * 5` |

**DST caveat:** the UTC column is for Eastern Daylight Time (mid-March to early November). During Eastern Standard Time (winter), add one hour to each UTC value. Using the America/New_York timezone avoids this entirely.

## 4. Grant push permission per routine
In each routine's **permissions**, enable **"allow unrestricted branch pushes"** so it can commit its memory updates back to `main`. Also allow it to run shell/Python commands (the routines call `python3 scripts/...` and `git`).

## 5. Test each one before trusting the schedule
Use **Run now** on each routine, in order (pre-market first), and confirm:
- It reads memory, runs the scripts against Alpaca paper, and prints sensible output.
- It pushes a commit to `main` (check the GitHub commit history).
- The market-open run respects the guardrails (rejections logged, no more than the weekly cap).

## 6. Turn off the local scheduler (prevents double-trading)
Once the cloud routines are confirmed committing to `main`, disable the five local scheduled tasks so only the cloud runs the account:
- In the desktop app's **Scheduled** panel, disable `trader-premarket`, `trader-market-open`, `trader-midday`, `trader-eod`, `trader-friday-review`.

From then on the desk runs entirely in the cloud, on schedule, whether or not your machine is on.

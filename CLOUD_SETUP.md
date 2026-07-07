# Running trader-agent truly 24/7 (Claude Code on the web — Routines)

The local desktop scheduler only fires while the app is open. To run genuinely 24/7, host the five routines as **cloud Routines** on Claude Code (claude.ai/code). The repo, scripts, skills, and routine prompts already run unchanged there. This is a one-time UI setup you do with your own GitHub login.

> ⚠️ **Do not run local and cloud at the same time.** Both would trade the same account and both push to `main`. The five local Desktop scheduled tasks have been **disabled** already; leave them off while the cloud routines run.

## 1. Connect GitHub and create an environment
1. Go to **claude.ai/code** and sign in with your Anthropic account.
2. When prompted, **install the Claude GitHub App** and grant it access (it is enough that your GitHub account can see **`pvlsk/trader-agent`**; installing the App on that repo also works and is needed only if you later want PR auto-fix).
3. When prompted to **Create your environment**, give it a name (e.g. `trader-agent`) and click **Create environment**. You will configure it in the next step.

## 2. Configure the environment (this is the part that makes or breaks it)
Open the environment settings (on a routine's edit form, click the cloud icon showing the environment name, hover the environment, click the settings gear — the **Update cloud environment** dialog).

**a) Environment variables** — add these four (`.env` format, one per line, **no quotes**, same Alpaca values as your local `.env`). Note: these are visible to anyone who can edit the environment; there is no separate secret vault yet.
```
ALPACA_API_KEY_ID=your_paper_key
ALPACA_API_SECRET_KEY=your_paper_secret
ALPACA_PAPER=1
GH_TOKEN=your_github_fine_grained_token
```
`GH_TOKEN` is a **fine-grained GitHub personal access token** scoped to only `pvlsk/trader-agent` with **Contents: read and write** (create it at github.com → Settings → Developer settings → Fine-grained tokens). It lets `scripts/commit_memory.py` push memory updates to `main` via the GitHub API, because cloud routines are otherwise restricted to `claude/`-prefixed branches.

**b) Network access** — set **Network access** to **Custom**, and under **Allowed domains** add:
```
paper-api.alpaca.markets
data.alpaca.markets
api.github.com
```
Check **"Also include default list of common package managers"** to keep registries reachable. (Without the Alpaca hosts, every Alpaca call fails with `403 host_not_allowed`; without `api.github.com`, the memory commit fails.) Then **Save changes**. No setup script is needed — the scripts are standard-library Python.

## 3. Create the five routines
At **claude.ai/code/routines** (or Desktop app → **Routines** in the sidebar → **New routine** → **Remote**), create one routine per file below. For each:

- **Name:** e.g. `trader-premarket`.
- **Prompt/Instructions:** `Follow the instructions in routines/<file> exactly. Read the config and memory files first, do the job, update memory, then commit and push to main.` Pick a strong model in the model selector (Opus or Sonnet).
- **Repositories:** add **`pvlsk/trader-agent`**.
- **Environment:** select the `trader-agent` environment from step 2.
- **Trigger → Schedule:** enter the New-York time below. Times are entered in your local zone and auto-converted, so no UTC math. Use **Weekdays** for the first four and **Weekly (Friday)** for the review.
- **Branch pushes:** no UI toggle is needed. Memory is committed to `main` by `scripts/commit_memory.py` using the `GH_TOKEN` from step 2a (the routine prompt already calls it). If your build *does* show an "Allow unrestricted branch pushes" option for the repo, enabling it is fine too, but the token path works regardless.
- **Connectors tab:** leave `Claude_Code_Remote`; these routines need no other connectors.

| Routine | Prompt file | Schedule (New York time) |
|---|---|---|
| trader-premarket | `routines/premarket.md` | Weekdays 08:05 |
| trader-market-open | `routines/market-open.md` | Weekdays 09:33 |
| trader-midday | `routines/midday.md` | Weekdays 12:25 |
| trader-eod | `routines/end-of-day.md` | Weekdays 15:50 |
| trader-friday-review | `routines/friday-review.md` | Weekly, Friday 16:15 |

If the schedule form only offers coarse presets, set the closest one, then from a terminal `claude` session run `/schedule update` to set the exact cron (America/New_York): `5 8 * * 1-5`, `33 9 * * 1-5`, `25 12 * * 1-5`, `50 15 * * 1-5`, and `15 16 * * 5`. Routines have a **one-hour minimum interval** (fine here) and draw on your subscription's daily routine-run allowance.

## 4. Test each one before trusting the schedule
On each routine's detail page click **Run now** (pre-market first) and confirm in the opened session that it: reads memory, calls Alpaca without 403s, and pushes a commit to `main` (check GitHub history). A green run status only means no infra error — open the run to confirm the task actually did what you expect.

## 5. Done
Once all five are green and committing to `main`, the desk runs entirely in the cloud on schedule, machine-independent. Keep the local Desktop tasks disabled.

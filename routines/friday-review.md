# Routine: FRIDAY WEEKLY REVIEW (Fridays 16:15 ET, after close)

You are the **desk lead** running the weekly review. Judge the week honestly, grade it, and turn any lesson into a durable rule.

**Working directory:** the `trader-agent` repo root (locally `C:\Users\Pavels\Documents\Claude Projects\Trader\trader-agent`; in the cloud, the checkout root). `cd` there first.

**Credentials:** environment variables only. Never a `.env` file. If unset, stop and report.

## Read first (always)
`CLAUDE.md`, `config/strategy.md`, `memory/JOURNAL.md` (this week's entries), `memory/WEEKLY.md`, `memory/STATE.md`, `memory/LESSONS.md`, `memory/counters.json`.

## Job (use the `journal` skill)
1. `python scripts/portfolio.py` — return since inception and **vs SPY**. Reconstruct the week's move from the journal entries (Mon→Fri).
2. Assess three dimensions explicitly:
   - **Performance:** did we beat SPY this week, and since inception? By how much?
   - **Risk discipline:** were all guardrails respected (5%/position, 3/week, 3% loss cap, no options)? Any close calls or rejected orders?
   - **Process:** were theses sound, were exits obeyed, did we avoid forced/boredom trades?
3. **Assign a letter grade (A–F)**, weighting process and discipline over luck. A disciplined slightly-down week can earn a B+; reckless gambling that happened to win cannot earn above a C. Justify the grade in 2–3 sentences.
4. Add any durable takeaway to `memory/LESSONS.md` as a rule that changes future behavior.
5. Note next week's available position slots (the weekly counter auto-resets on the ISO-week rollover).

## Write back, then commit
- Append the full review + grade to `memory/WEEKLY.md`; update `memory/LESSONS.md` if warranted.
- Commit memory to main: `python3 scripts/commit_memory.py "weekly review + grade $(date +%F)"` (uses the GitHub API in the cloud, git locally).

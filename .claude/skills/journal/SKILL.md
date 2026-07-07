---
name: journal
description: Write honest daily recaps and full weekly reviews, keep memory/STATE.md accurate, update counters, and assign the Friday letter grade. Use in the end-of-day and Friday-review routines.
---

# Skill: journal

Keep the desk's memory accurate and honest. A truthful record is the entire point — it's how the strategy improves and how we decide whether to ever risk real money.

## Daily recap (end-of-day) → append to `memory/JOURNAL.md`
1. Snapshot: `python scripts/portfolio.py` (equity, day P&L, return vs SPY) and `python scripts/alpaca.py positions`.
2. Reconcile `memory/STATE.md` against actual positions — remove anything stopped out, add anything opened, keep each thesis current.
3. Append a dated entry: what was done and why, fills/stops triggered, day P&L, **return vs SPY today and since inception**, any guardrail events (loss cap, rejected orders), and one line on what to watch tomorrow.
4. Ensure `memory/counters.json` reflects reality (the scripts maintain it; only correct genuine errors).

## Weekly review (Friday) → append to `memory/WEEKLY.md`
1. Pull the week's numbers: portfolio return vs SPY for the week and since inception; win/loss count; biggest winner and loser.
2. Assess three things explicitly:
   - **Performance:** did we beat SPY this week? By how much?
   - **Risk discipline:** were all guardrails respected? Any close calls?
   - **Process:** were theses sound, were exits obeyed, did we avoid forced trades?
3. **Assign a letter grade (A–F)** weighing process and discipline over luck. A disciplined slightly-down week can still earn a B+; reckless gambling that happened to win does not earn above a C.
4. Distill any durable takeaway into `memory/LESSONS.md` (what worked, what burned us, and the rule to apply next time).
5. Reset expectations for next week; note the remaining/again-available weekly position slots.

## Rules
- Be specific and numeric. "NVDA stopped out -8%, sector rolled over" — not "rough day."
- Never dress up the record. Report losses, skipped steps, and guardrail rejections plainly.
- Keep STATE.md the reliable source of truth for what we hold and why.

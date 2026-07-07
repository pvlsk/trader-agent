---
name: risk-check
description: Read current guardrail state (equity, day P&L vs loss cap, open positions, remaining weekly slots) before acting, and confirm proposed trades will pass before submitting. Use at the start of any routine that might trade.
---

# Skill: risk-check

The safety pre-flight. Run this before the execute-trade skill so you act with a clear picture of what's allowed right now.

## Steps
1. `python scripts/risk.py status` — prints equity, day P&L vs the 3% loss cap (and whether trading is HALTED), open position count, new positions used this week vs the cap, and the per-position dollar limit.
2. Cross-check `config/risk.yaml` for the current limits and `memory/counters.json` for the weekly count and inception baseline.
3. For any trade you intend to place, **preview it first** with `--dry-run`:
   `python scripts/alpaca.py buy SYMBOL --pct <n> --trail-percent <t> --dry-run`.
   A PASS means the live order will be accepted; a REJECT tells you exactly which limit blocks it.

## Interpreting results
- **Loss cap HALTED:** open no new positions today. You may still manage/exit existing ones (sells are always allowed).
- **Weekly slots used up:** no brand-new satellite names until the ISO week rolls over; you may still add to the core or manage existing positions within the per-position cap.
- **Position cap:** if adding to an existing name would exceed 5%, size down or skip.

## Rules
- Treat a REJECT as final. Never call the REST API directly to bypass the gate.
- If `risk.py status` errors on missing credentials, stop and report — do not guess keys.
- When in doubt, do less. Preserving the guardrails matters more than any single trade.

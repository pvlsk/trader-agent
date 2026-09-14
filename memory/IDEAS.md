# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-09-14 (pre-market, Monday) — market closed, checked 08:07 ET, next open 09:30 ET._

**No actionable new entry today — the desk is now double-blocked, not just cash-blocked.** `risk.py status`: equity **$100,667.42** (`portfolio.py`, seconds apart with `risk.py`'s $100,656.59 — consistent), day P&L **-0.45%/-0.46%** (loss cap -3% not tripped), **fresh week 2026-W38, 0/3 slots used**. Cash re-checked via `portfolio.py`: **$57.40** — unchanged since 2026-09-08, now a 10th-plus straight shift with a hard lockout (cash-not-margin rule, `LESSONS.md` 2026-08-05/08-21). **New this shift: even setting cash aside, the satellite sleeve has no dollar room left** — the 10 existing satellite positions sum to ≈$39,873, **≈39.6% of equity, essentially at the 40% target already** (target band, not a hard ceiling, but there's no slack to add an 11th name without first trimming or a stop-out freeing capacity). SPY core sits ≈60.3%, on target, so no rebalance-band trim is sanctioned to manufacture cash either. Weekly slot capacity (0/3 used) is not the binding constraint this week — capital is.

## Market read (2026-09-14 pre-market)

Futures are lower ahead of the FOMC meeting Tuesday-Wednesday (Sept 15-16): rising oil prices (Middle East tensions escalating further over the weekend), a fresh AI/semiconductor selloff (NVDA, AMD, AVGO, and related data-center/power names all cited lower), and last week's CPI/PPI prints showing inflation "not sliding," which raised — not lowered — the odds the Fed holds or even hikes this week rather than cutting. This is a real, dated macro risk window sitting directly over the next two sessions: a hawkish surprise or dovish disappointment on Wednesday could move the whole book, held satellites included. Sector-rotation commentary (StockCharts RRG, weekly) has Health Care and Financials still leading but losing relative momentum, Technology weakening but starting to build momentum back, Energy showing the longest tail in the "improving" quadrant and moving fast toward leading, and Materials just crossing into "improving." **Every one of those five sectors is already held** (XLV, XLF, XLK, XLE, XLB) — rotation analysis surfaces no fresh *unheld* sector idea, same pattern as recent weeks. One dated, verified single-name catalyst worth logging for context even though CAT isn't in the universe: Stifel initiated Caterpillar at Buy with a $980 target (2026-09-12) — CAT is a top holding inside XLI, so this is a mild tailwind for XLI's still-broken thesis, not an actionable idea on its own (not in `config/universe.yaml`, no justification to add it).

## Held-position status (carried forward, informational only — no action, not a trade recommendation)

- **XLI (thesis confirmed broken 09-09):** live quote $172.37, still below the ~$173.6 50-day MA line, essentially unchanged from Friday's $172.41. The Stifel CAT upgrade (09-12) is a mild positive for one of XLI's top holdings but hasn't moved the ETF back above its line. Un-cuttable except by its own trailing stop (cancel/replace tooling gap, `LESSONS.md` 2026-07-24 + follow-ups).
- **XLB (thesis confirmed broken 09-10):** live quote $50.94, still below its ~$51.06 line, essentially flat vs Friday's $50.95. Rotation commentary flags Materials just entering the "improving" RRG quadrant — worth watching for an actual close back above the line before treating this as a recovery, not before. Same tooling gap, same un-cuttable status.
- **XLE (extended winner, +15.6%):** live quote $65.12, up from Friday's $65.00 and now the standing longest-tenured tighten candidate at its widest margin yet. Still blocked by the same tooling gap.

## Screened all three edges

- **Momentum/trend:** No unheld universe name screened this morning shows a clean, undamaged uptrend that would clear the bar even if capital were available — the dominant tape story is a tech/AI-stock selloff (NVDA/AMD/AVGO/data-center names all cited lower pre-market), which argues against fresh momentum entries in that space regardless. No candidate surfaced.
- **Catalyst:** No fresh, verified, dated catalyst on an unheld universe name this morning beyond the CAT/XLI note above (CAT itself isn't tradable under `config/universe.yaml`). Did not find a credible earnings/upgrade catalyst on the momentum watchlist worth flagging.
- **Relative-strength rotation:** All five sectors named as leading or improving this week (Health Care, Financials, Energy, Materials, and now-building Technology) are already held via XLV/XLF/XLE/XLB/XLK. No unheld sector ETF shows a fresh rotation case.

## Ranked ideas

**None.** The honest call today is to do nothing, for two independent reasons: (1) cash remains a hard lockout at $57.40, unchanged for a 10th-plus straight shift, and (2) even if cash weren't binding, the satellite sleeve is already at ≈39.6% of equity against a 40% target — there's no meaningful room to add an 11th name without first freeing capacity via a trim or a stop-out. No screened idea across any of the three edges cleared the bar strongly enough to argue for forcing either constraint anyway; the tape's dominant theme (tech selloff, rising oil, FOMC risk) argues for caution, not urgency.

**Recommendation for the open routine:** No new entry is executable today. Manage the existing book: re-verify all 10 satellite trailing stops are live, check whether XLI or XLB show any close-basis recovery above their falsifiable lines (neither has intraday so far), and hold XLE's tighten call as still blocked by the same tooling gap. FOMC Tuesday-Wednesday is the week's dominant risk event — no held position's thesis explicitly hinges on the Fed decision, but a broad market reaction either way could move the whole book; nothing to do about that pre-emptively beyond normal stop discipline.

## Notes for the open/midday routines

- Fresh count: 2026-W38, 0/3 slots used — capacity is not the constraint this week, capital is (cash lockout **and** satellite sleeve at ~39.6%/40% target).
- Cash is $57.40, unchanged for a 10th-plus straight shift — re-verify at the open. This has now gone unresolved long enough (since 2026-09-08) that it's worth a fresh mention at the next weekly review if it's still unchanged then, per `LESSONS.md` guidance on stuck escalations (though note the 2026-08-28 core tilt shows this kind of lockout can resolve itself via an unrelated later decision — don't assume it needs a brand-new escalation without first checking whether anything already addressed it).
- XLI and XLB (both thesis-confirmed-broken, now a 4th/5th+ session respectively) and XLE (extended winner at its widest margin yet, +15.6%) are unchanged in kind, informational only — same cancel/replace tooling gap as before.
- FOMC meets Sept 15-16 (Tue-Wed) — the week's dominant, dated macro catalyst; CPI/PPI last week both ran hot, raising odds of a hawkish outcome. Real, dated event risk for the whole book, not just satellites.
- Oil prices rising on escalating Middle East tensions is a live tailwind for the held XLE position (already the book's best performer) and a headwind for the broader tape.

## Sources

- [Stock Market Today (Sept. 14, 2026): Nasdaq futures fall on rising oil prices, sagging AI stocks — TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-14-2026)
- [Morning Preview: September 14, 2026 — Investrade](https://investrade.com/morning-preview-september-14-2026/)
- [Stock market today: investors await Fed decision — CNBC (via eciks.org)](https://eciks.org/26613-stock-market-today-fed-decision-cnbc)
- [The Best Five Sectors This Week #82 — StockCharts](https://articles.stockcharts.com/article/best-five-us-stock-market-sectors-week-of-09-07-2026-82/)
- [Sector Rotation Just Changed. Here's What's Leading — StockCharts](https://articles.stockcharts.com/article/sector-rotation-just-changed-heres-whats-leading/)
- [Caterpillar stock gains on fresh analyst upgrades and strong quarterly figures — ad-hoc-news.de](https://www.ad-hoc-news.de/boerse/news/corporate-news/caterpillar-stock-gains-on-fresh-analyst-upgrades-and-strong-quarterly/70093234)

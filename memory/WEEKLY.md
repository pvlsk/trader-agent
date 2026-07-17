# WEEKLY REVIEW — Friday reviews + letter grades (newest at top)

Each entry: portfolio return vs SPY (week + since inception), win/loss count, biggest winner/loser, an honest read on performance / risk discipline / process, a **letter grade (A–F)**, and the lesson carried forward.

---

## Week of 2026-07-13 to 2026-07-17 (2026-W29) — Grade: B+

### Performance
- **Return this week:** portfolio -1.36% vs **SPY -1.60%** → **alpha +0.24%** this week — a genuine, if narrow, beat of the benchmark, the first positive weekly alpha since the desk went live.
- **Return since inception:** -0.55% vs **SPY -0.35%** → **alpha -0.21%**, narrower than last Friday's -0.45/-0.46% gap. The satellite sleeve clawed back roughly a quarter-point of the deficit this week even as the account round-tripped from +0.82% to -0.55% since inception on a broad Thursday/Friday tech-led selloff.
- Equity $100,816.92 (last Friday close) → $99,445.70 (this Friday close). Worst day was today (-0.85 to -0.87%), driven by a genuine, worsening chip-sector rout (TSMC capex-guidance concerns, GOOGL Gemini delay, broad semis weakness) — not a portfolio-specific event, and well inside the -3% loss cap.
- Winners since entry: AAPL +1.9%, XLF +1.3%, XLE +1.2% (energy/Strait-of-Hormuz catalyst held up all week). Losers: XLK -5.4% (worst, and worsening daily — sector "Lagging" RS the whole week, thesis now confirmed broken), XLV -2.3%, XLI -1.4%.
- Three new satellites opened this week, all matching the weekly cap exactly: XLI (Mon, industrials/defense catalyst), XLE (Tue, energy/Hormuz catalyst), AAPL (Thu, momentum/rotation catalyst). All three are green or roughly flat since entry; the drag is entirely from positions opened in prior weeks (XLK, XLV).

### Risk discipline
- **Zero guardrail breaches this week** — a clean improvement on last week's self-corrected 5%-cap breach. All three new entries sized well under the 5% cap (XLI ~4.3%, XLE ~4.0%, AAPL ~3.9%, all under the $4,972 threshold). The 3-per-week cap was hit exactly at 3 and respected the rest of the week (Wednesday and Friday correctly took no new positions with the cap exhausted). The 3% daily loss cap was never approached (worst day -0.87%, less than a third of the cap). No options, leveraged/inverse ETFs, or crypto were ever attempted.
- **One real operational limitation, not a discipline lapse:** Friday's market-open routine correctly identified that XLK's thesis had broken (price below its tracked ~$178.6 50-day MA, confirmed worsening sector rout via WebSearch) and correctly attempted the mandated discretionary cut per `config/strategy.md`'s exit rules — but `scripts/alpaca.py sell XLK --all` was **rejected by Alpaca** (403, `held_for_orders`) because the resting 10% trailing-stop order already holds all shares as sell-side inventory, and the script has no cancel/replace-order subcommand to free them first. This is the same root-cause gap first found on 2026-07-14 (blocked retightening XLV's stop) — Friday's event is the **third** confirmation, and now proves the gap blocks *any* sell on a stopped position, not just retightening. The routine correctly declined to work around it via a raw API call. This is a tooling gap, not a judgment failure — the desk did exactly what the strategy calls for and was blocked by the automation itself.

### Process
- Every new entry had a clear, falsifiable, written thesis (XLI: industrials RS + defense catalyst, falsifiable at the 50-day MA; XLE: energy uptrend + Strait-of-Hormuz supply catalyst; AAPL: momentum + rotation-into-cash-generators catalyst, tightened to an 8% trail given overbought RSI at entry).
- Correctly passed on forcing a trade Wednesday (07-15) when no idea cleared the bar — held the remaining slot rather than chasing.
- Correctly escalated XLK: flagged the falsifiable break in Friday's pre-market ideas, re-verified at the open with a live quote and a fresh WebSearch confirming the rout was genuine and worsening (not a one-day wobble), then attempted the cut exactly as the strategy prescribes. The failure was purely mechanical (script limitation), and the routine did not compromise by working around it improperly.
- No averaging down, no stop-widening, no revenge trading. XLV, still a laggard, was left alone with its original stop rather than force-managed.

### Grade: B+
Better than last week on every axis that's actually within the desk's control: zero guardrail breaches (vs. one self-corrected breach last week), a positive weekly alpha (+0.24%, first of the desk's short life), and sound, disciplined process including the right call on an entry to skip and the right call on an exit to attempt. It doesn't reach A-range because the account is still net negative since inception (-0.55%) and because a real, live risk-management action — cutting a thesis-broken position — is currently **impossible to execute** through the desk's own tooling, which is now a three-times-confirmed, unresolved gap sitting on the critical path of the strategy's exit discipline. That is a process risk serious enough to keep this out of the top grade tier even though it isn't this routine's fault.

### Next week (2026-W30, opens Monday 2026-07-20)
All 3 satellite slots reset. One idea queued in `memory/IDEAS.md`: **XLRE** (relative-strength rotation, Medium conviction, confirmed 50-day MA crossover 6/22) — re-verify fresh at Monday's open. **Priority carryover: XLK's thesis is broken and the discretionary cut is still pending** — it can only resolve via the 10% trailing stop triggering on its own, or a fix to `scripts/alpaca.py` (a cancel/replace-order subcommand) that lets a routine free up shares held by a resting stop order. Recommend this tooling fix be prioritized before it costs more than the ~5.4% already lost on XLK. Also watch XLV (-2.3%, sector RS still weak) and XLI (-1.4%, pulled down by the same chip-rout risk-off tone despite an intact defense catalyst).

---

## Week of 2026-07-07 to 2026-07-10 (2026-W28) — first week live — Grade: B-

**This was the desk's first week** (account initialized Tue 2026-07-07), so the weekly window and since-inception window are the same.

### Performance
- **Return since inception:** +0.79% vs **SPY +1.24%** → **alpha -0.45%**.
- Equity $100,000 → $100,787.98 (Fri close). Day P&L Fri +0.31% (no loss-cap events all week).
- Winners: XLK +0.5% (entered 7/9), XLF +0.4% (entered 7/8). Loser: XLV -2.4% (entered 7/7, biggest drag on the week).
- We did not beat SPY this week. The core (70% SPY, +1.24%) carried the account; the satellite sleeve (XLV/XLF/XLK) underperformed the core on net, mainly because XLV faded after being flagged overbought (RS>70) the day after entry and never recovered. This is exactly the asymmetry the strategy is built around — a lagging satellite sleeve cost us ~45bps of alpha, not principal — but it's still a below-benchmark week and should be recorded as one.

### Risk discipline
- Guardrails were exercised and held: a 6%-of-equity order was correctly **rejected** on day one (2026-07-07); the 3% daily loss cap was never approached (worst day P&L was a small negative, nowhere near -3%); no options/leveraged/crypto symbols were ever attempted; the 3-per-week satellite cap was hit exactly at 3 (XLV/XLF/XLK) and respected for the rest of the week — Friday's routine correctly took no new positions even with `IDEAS.md` queued, because the cap was already used.
- One real lapse: on 2026-07-08, a `buy XLF` command wrapped in a shell `python3 ... || python ...` fallback pattern caused a **duplicate live buy** after a transient race on the trailing-stop attach step, temporarily pushing the XLF position to ~7.9% of equity — over the 5% cap — and double-counting the weekly counter. It was self-caught within the same routine (checked `positions`/`orders` against intent), corrected back to the intended 71-share/~3.95% position, and `counters.json` was hand-corrected. No harm reached the next routine's starting state, but the cap was breached, even if briefly and by tooling rather than by a bad trading decision.
- The lesson from that incident was then correctly applied the very next day (2026-07-09): a similar 403 error fired for a legitimately slow paper-market fill, and instead of retrying, the routine polled `orders`/`positions`, confirmed no duplicate, and proceeded correctly. That's real evidence the fix stuck.

### Process
- Theses were written and falsifiable for every entry (XLV relative-strength rotation, XLF bank-earnings catalyst rotation, XLK momentum/AI-capex). Exits were obeyed — no stop was ever loosened, no position was averaged down.
- Good judgment on what to skip: SMH/AVGO/XLE were passed on repeatedly despite loud headlines (SK Hynix IPO, Iran/oil spike) because their technicals didn't confirm a trend — the desk didn't chase narrative over price action.
- No boredom or forced trades: once the weekly cap was hit on 7/9, Friday correctly did pure reconciliation with no attempt to work around the cap.

### Grade: B-
Weighting process and discipline over the raw number: guardrail enforcement, thesis discipline, and refusal to chase headlines were all sound, and the one real cap breach was self-inflicted by an operational shortcut (not a trading decision), caught within the same routine, fully reversed, and turned into a lesson that was correctly applied the next day. That keeps this out of C-range "reckless" territory. But it's still a week that underperformed SPY and had an actual (if brief) breach of the single most important guardrail — the 5% position cap — so it doesn't earn better than a B-. A clean repeat of this week's discipline with no cap breach, or a week where the satellite sleeve adds alpha instead of dragging, earns the upgrade to B/B+.

### Next week (2026-W29, opens Monday 2026-07-13)
All **3 satellite slots reset and are available**. `memory/IDEAS.md` has XLI (Medium-High conviction, confirmed uptrend) queued as the top idea, AMD (Medium conviction, extended) as #2. Watch XLV's trailing stop closely — it's the weakest position and the RS-overbought flag from 7/8 has not resolved bullishly. Bank earnings (JPM/WFC/BAC/C) begin 2026-07-14, the catalyst underpinning the XLF thesis — a good real-world test this coming week.

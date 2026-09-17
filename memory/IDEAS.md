# IDEAS — pre-market candidates (overwritten each research shift)

_2026-09-17 08:xx ET pre-market. Market closed (`clock`: is_open false, checked 08:06:18 ET, next open 09:30 ET today — normal overnight closure, not a holiday). `risk.py status`: equity $100,616.56, day P&L +0.78% (loss cap ok), 10 open positions, **week 2026-W38 still at 0/3 new-position slots used — all 3 available**, so capacity is not the constraint today._

## Market read

**FOMC (Wed 09-16, 2pm ET decision / 2:30pm ET press conf) has now resolved and the reaction was risk-off into yesterday's close** — per yesterday's EOD journal, equity fell -0.76% from midday to close, every satellite pulled back from its midday read, and since-inception alpha was flat-to-slightly-negative at -1.27%. Today's `risk.py` snapshot (+0.78% day P&L) reflects the pre-market baseline reset, not a live intraday read.

**Operational flag — WebSearch tool unavailable this shift.** Every WebSearch query attempted this morning (FOMC market reaction, sector relative-strength rankings, premarket movers/catalysts, and even an unrelated control query) returned only generic/Wikipedia-style static content with an explicit "Web search error: unavailable" — no live news, no current prices, no real-time data of any kind came back. This is a hard blocker for two of the three edges this shift:
- **Catalyst edge:** cannot verify or cite any overnight/pre-market news, earnings, or upgrades — the skill's explicit rule is "unverified rumor is not a catalyst," and with no working search there is nothing to verify.
- **Relative-strength rotation edge:** `scripts/alpaca.py quote` only returns a last price, no moving averages or historical bars, so 1–3 month sector RS ranking is not computable from tooling alone; WebSearch was the only source for that context and it's down.
- **Momentum/trend edge:** same problem — a live last-price snapshot alone (checked below) cannot establish "confirmed uptrend" (needs 50-day/200-day MA context) without either working search or a bars subcommand, neither of which is available this shift.

Live quotes were pulled for every un-held sector ETF and every un-held momentum-watchlist/theme name as a sanity check (XLY $110.15, XLU $41.33, XLRE $42.79, XLC $113.02, XLI $168.68 — still confirmed-broken, well below its cited ~$173-176 50-day MA range from prior shifts, stays watch-only, no revenge trade; AAPL $332.49, MSFT $490.45, NVDA $213.94, AMZN $249.78, GOOGL $342.94, META $673.88, AVGO $339.40, AMD $512.78, TSLA $358.13, COST $893.57, LLY $1138.46, NFLX $76.41, QQQ $705.13, SMH $545.83, XBI $154.13, GLD $391.68) — but a price snapshot alone, with no trend/MA context and no catalyst verification, is exactly the "vibes" basis the strategy and this skill explicitly forbid ("a falsifiable thesis... not vibes"). None of this clears the bar for a written thesis.

## Ranked candidates

**None. Recommended action: do nothing — no new entries today.**

Not because nothing looks interesting, but because the tooling needed to verify any of the three edges (working web search for catalysts/RS context, or a price-history source for trend confirmation) was unavailable this shift. Forcing a trade off a bare last-price snapshot with no falsifiable line would be exactly the "boredom is not a signal" / marginal trade `LESSONS.md` and `config/strategy.md` say to skip. All 3 weekly slots remain open for market-open/midday today if either the tooling recovers or a routine has another way to verify a setup.

## Watch list (carried forward, unverified this shift due to the tool outage)
- **XLI** — still confirmed-broken by last price ($168.68 vs. the ~$173-176 50-day MA range cited across prior shifts); do not re-enter without a full session's close back above that line, and re-verify the line itself once search recovers (it's been stated with a range, not a single verified number, for a few sessions now).
- **AMD** — flagged repeatedly through August/September as an extended (~140%+ YTD) AI-demand move; last $512.78, still chasing absent a verified pullback-to-support read. No fresh verification possible this shift.
- **Post-FOMC re-screen (carried from yesterday):** IWM (-3.9%) and JPM (-2.8%) widened the most in yesterday's post-decision reaction per the EOD journal — worth a closer technical/catalyst look once verification tooling is back, though neither has crossed a stated falsifiable line.
- **Energy/value tilt (XLE, held)** — no add needed regardless of tooling status; already near the 5% band, a "manage the winner" question for open/midday, not a new-entry one.

**Escalation for the next routine / weekly review:** if `WebSearch` (or equivalent) is still down at market-open or midday, the desk is effectively flying blind on catalyst verification and RS/trend confirmation for *any* new entry — that's a reason to lean harder toward "manage existing positions only," not a one-off note to repeat unchanged. Flag this at Friday's review if it persists.

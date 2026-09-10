# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-09-10 (pre-market, Thursday) — market closed, checked 08:08 ET, next open 09:30 ET._

**One actionable idea this week (unchanged from yesterday, still cash-blocked), one watch-only.** `risk.py status`: equity **$100,919.65**, day P&L -0.06% (loss cap -3% not tripped), **2026-W37, 1/3 weekly slots used** (XLK entered 09-08; 2 remain). Cash re-checked this shift via `portfolio.py`: **$57.40** — unchanged from yesterday, still a hard lockout for any new entry (cash-not-margin rule, `LESSONS.md` 2026-08-05/08-21). This is now the second straight pre-market shift with cash stuck at $57.40; flagging for the open/midday routines to watch for a stop-out or genuine rebalance-band trim that would free capacity, since no discretionary trim is sanctioned purely to manufacture cash while SPY sits on-target (~60.3%).

## Market read (2026-09-10 pre-market)

Risk-off persists into an eighth-day-plus stretch: the Iran-US-Saudi conflict escalated further overnight rather than cooling — Brent ~$101.84 (+0.62%), WTI ~$96.06 (+1.01%), oil up >8% in September after the U.S. destroyed five more Iranian tankers and Houthi strikes forced a temporary Saudi output halt. This is a straight tailwind for the held XLE position (+15.6%), not a new signal. CPI prints tomorrow, Thursday 2026-09-11 (Natixis consensus: core +0.2% m/m, headline +0.4% m/m) — a real, dated vol event ahead of the Sept 16-17 FOMC; Fed Chair Warsh has said underlying inflation trends "have not meaningfully improved," a hawkish-leaning signal worth weighing against any new entry's holding period. Sector-rotation commentary is genuinely mixed this morning: one rotation model shows XLF strengthening and a defensive XLU/XLV rotation with XLI deteriorating (consistent with the desk's own confirmed-broken XLI thesis), while a competing source argues XLI strength persists on hyperscaler AI-capex spend — no consensus, so weight the desk's own live price data over either. AAPL's Sept 9 iPhone event drew a mild sell-the-news reaction (-1.06%), not a buy signal. NFLX and TSLA both drew fresh analyst downgrades overnight (Rosenblatt/Pivotal cut NFLX to Neutral/Hold on its Warner Bros. studio-acquisition announcement; Morgan Stanley cut TSLA to Neutral) — negative catalysts, not held, no action.

## Held-position status (carried forward, informational only — no action, not a trade recommendation)

- **XLI (thesis confirmed broken 09-09):** still below its ~$173.6 50-day MA this morning at $171.80 (live quote) — no recovery signal. Un-cuttable except by its own trailing stop (cancel/replace tooling gap, `LESSONS.md` 2026-07-24 + follow-ups).
- **XLE (extended winner, +15.6%):** the widening Iran conflict remains a pure tailwind, not a new signal. Still the standing tighten candidate, still blocked by the same tooling gap.
- **XLB:** thin above its ~$51 line at $51.39 (-4.1% today) — worth a close watch at the open/midday for a break.

## Screened all three edges

- **Momentum/trend:** **XBI** technicals remain Strong Buy (12/0 moving-average signals, RSI(14) ≈66.6, MACD ≈+2.14 and rising, per a second independent source) — unchanged from yesterday's read. Price has pulled back to **$159.36** this morning from the $161-162 level cited yesterday, still a normal pullback within a confirmed uptrend, not a thesis break (52-week high $169.89 intact as the reference). **SMH** gives a genuinely conflicting read this morning: the desk's own live quote is $574.15 (above the ~$572.76 50-day MA line, consistent with a second confirming close), but an independent technical aggregator (Barchart) shows a materially different price (~$560.42) and a "Strong Sell" signal with price back below the 50-day MA. Given the direct conflict between sources and no way to verify SMH's actual prior-session close from available tooling, **SMH stays watch-only** — do not size it until the open routine confirms live price/MA relationship directly rather than relying on either source alone.
- **Catalyst:** No fresh, verified, directional catalyst found for any unheld momentum-watchlist name (checked AAPL, MSFT, NVDA, AMZN, GOOGL, META, AVGO, AMD, TSLA, COST, LLY, NFLX — see Market read above for the two negative items on NFLX/TSLA, neither actionable since we don't hold them and a downgrade isn't a buy signal). AVGO/AMD got a passing "top pick" mention from one analyst note but with no rating change or price target — doesn't clear the "real, verifiable, directional catalyst" bar on its own. XBI's catalyst (biotech M&A wave ahead of the 2028 patent cliff, easier FDA posture since June, steady positive trial readouts) remains a structural, multi-month tailwind, unchanged and still verified.
- **Relative-strength rotation:** No unheld sector ETF (XLY, XLU, XLRE, XLC) shows a fresh rotation case — XLU has an ongoing AI-power-demand narrative and XLRE a general rate-resilience narrative, but neither is a dated catalyst or a confirmed RS breakout this morning. Sector RS commentary on the *held* sectors is mixed/conflicting (see Market read) — no actionable new-name signal either way.

## Ranked ideas

| Rank | Symbol | Edge | One-line thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|---|
| 1 | XBI | Momentum/trend + catalyst | Technicals remain Strong Buy (12/0 MA signals, RSI 66.6, MACD +2.14 rising) on a structural, multi-month biotech catalyst (M&A wave, easier FDA posture since June, positive trial readouts); this morning's $159.36 is a normal pullback from $161-162, not a thesis break, with the 52-week high ($169.89) still the reference. Falsifiable: thesis breaks if XBI closes back below its 50-day MA or gives back this month's breakout gains. **Blocked by cash, not conviction** — see note above. | ~$159-160 | 10% | High (execution blocked by cash) |
| 2 (watch only, not sized) | SMH | Momentum/trend + catalyst | AI-memory demand (Dell backlog, UBS HBM upgrade, Micron/SanDisk strength) remains real, but this morning's technical read is internally conflicted (desk quote above the 50-day MA, an independent aggregator showing price below it and a Strong Sell signal) — needs the open routine to confirm live price vs. MA directly before any sizing discussion. | n/a — resolve the data conflict first | 10% (if triggered) | Low |

**Recommendation for the open routine:** No new entry is executable today regardless of conviction — cash is $57.40, a hard lockout unchanged from yesterday, and SPY is on-target (~60.3%) so no rebalance-band trim is sanctioned to manufacture cash. If a stop-out or genuine rebalance frees cash intraday, XBI is the pick (unchanged thesis, still within its 52-week-high band) — re-quote before sizing since it's had two sessions of price movement since this read. Do not size SMH under any circumstance until the open routine resolves the live-price-vs-50-day-MA conflict directly via `alpaca.py quote` (the desk's own tooling is more reliable than a third-party aggregator, but the discrepancy is large enough — $574 vs $560 — to warrant a direct recheck rather than trusting either blind). Given the ongoing cash lockout, there's no urgency pressure from the 2 remaining weekly slots — they can wait for a clean setup and available capacity.

## Notes for the open/midday routines

- Fresh count: 2026-W37, 1/3 slots used (XLK 09-08), 2 remain.
- Cash is $57.40, unchanged from yesterday — second straight pre-market shift with no capacity; re-verify at the open and flag to EOD/weekly if it persists further.
- XLI (thesis confirmed broken, still below its ~$173.6 line at $171.80) and XLE (extended winner, tighten blocked) are unchanged, informational only.
- XLB is thin above its ~$51 line ($51.39, -4.1%) — watch for a close below it.
- Oil continues to spike on real, widening Iran-US-Saudi escalation — reinforces the held XLE thesis, doesn't call for new action.
- CPI prints Thursday 9/11 (tomorrow), FOMC Wed 9/16 — both real, dated macro catalysts inside the operative window; Fed commentary this week leaned hawkish.
- SMH price data conflict (see above) needs resolving with a direct `alpaca.py quote` + whatever the open routine can verify before any consideration of sizing it.

## Sources

- [Netflix, Tesla downgraded: Wall Street's top analyst calls — Yahoo Finance](https://finance.yahoo.com/news/netflix-tesla-downgraded-wall-streets-144549637.html)
- [Apple September 2026 event recap — MacRumors](https://www.macrumors.com/2026/09/09/apple-september-2026-event-recap/)
- [How Apple stock usually reacts to big iPhone reveal events — Yahoo Finance](https://finance.yahoo.com/technology/article/how-apple-stock-usually-reacts-to-big-iphone-reveal-events-152915777.html)
- [The Rotation Confirmed (defensive rotation, XLI deteriorating) — Lead-Lag Report](https://www.leadlagreport.com/p/the-rotation-confirmed-defensive)
- [Rare XLI/XLF Decoupling — Seeking Alpha](https://seekingalpha.com/article/4876590-rare-xli-xlf-decoupling-is-flashing-that-also-happened-in-1999-2007-and-2020)
- [SMH ETF Technical Analysis — Barchart](https://www.barchart.com/etfs-funds/quotes/SMH/technical-analysis)
- [SMH ETF Technical Analysis — Investing.com](https://www.investing.com/etfs/holdrs-merrill-lynch-semiconductor-technical)
- [XBI Technical Analysis — Investing.com](https://www.investing.com/etfs/spdr-s-p-biotech-technical)
- [Iran-US oil, Hormuz supply update (9/10) — CNBC](https://www.cnbc.com/2026/09/10/iran-us-oil-hormuz-supply-trump-military-brent-wti.html)
- [Oil prices rise to $99 on second Iran attack (9/8) — CNBC](https://www.cnbc.com/2026/09/08/oil-prices-today-brent-wti-hormuz-iran-war.html)
- [CPI report and Fed rate hike — IndexBox/Natixis](https://www.indexbox.io/blog/cpi-report-and-fed-rate-hike-key-insights-from-natixis/)

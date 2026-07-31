# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-07-31 (pre-market)_

**0 actionable new entries recommended today, despite 3/3 weekly satellite slots being open (2026-W31, `counters.json`/`risk.py status` confirm 0/3 used).** Market closed at read time (`clock`: next open 09:30 ET today, market currently closed). Loss cap not tripped (day P&L -0.05%, equity $99,314.18 per `risk.py status`). The two biggest single-stock moves of the week (AMZN blowout, AAPL guidance-driven plunge) are both in "don't chase / manage the existing position" territory rather than fresh-entry territory, and the sector rotation that's genuinely working is already fully expressed via held positions.

## Market read (2026-07-31 pre-market)

**AAPL (held satellite, 8% trail) is the top item for market-open, not a new idea.** Apple beat on EPS ($2.02 vs. $1.89 est.) and revenue ($109.42B vs. $108.86B est.) for its fiscal Q3, with 16% y/y sales growth led by iPhone/Mac/Services — but guided September-quarter revenue growth to just 9–11% (down from 16%) and flagged "supply constraints." The stock fell **-6.65% to -7.3%** in the after-hours/pre-market session, last quote **$308.43** vs. Thursday's ~$333 close (entry was $327.57). This is a real guidance-driven reversal, not noise — the falsifiable thesis ("close back below the 50-day MA or reversal of the rotation-into-cash-generators narrative") looks challenged, and the 8% trailing stop (order `54f22517`) is now much closer to being tested at the open than it was yesterday. Flagging prominently for market-open to check the stop status first thing; pre-market quotes don't trigger the trail, so nothing has happened yet, but this needs eyes at 9:30. ([CNBC](https://www.cnbc.com/2026/07/30/apple-earnings-live-updates.html), [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-30/apple-s-earnings-will-test-stock-s-status-as-the-ai-safety-play))

**AMZN (not held) reported a blowout Q2 — real catalyst, but a blow-off gap, not an entry today.** Revenue $200.61B (+19.6% y/y) vs. $196.47B est., EPS $5.75 vs. $1.82 est., AWS +36.7% y/y (fastest in 18 quarters), AI/chips businesses each crossed a $25B run rate. Stock is **+8–12% pre-market**, live quote **$255.25**. Per `config/strategy.md`'s explicit rule to avoid buying blow-off gaps, this is not a chase-worthy entry this morning — no margin of safety left in the price. Worth re-screening after it bases over the next few sessions. ([Motley Fool](https://www.fool.com/coverage/stock-market/2026/07/30/stock-market-today-july-30-amazon-soars-over-8-after-hours-on-earnings-beat/), [CNBC](https://www.cnbc.com/2026/07/30/amazon-amzn-q2-earnings-report-2026.html))

**MSFT (not held) is a similar story, two sessions old.** Reported 7/29 evening: Azure +43% y/y, strong FQ1 revenue guidance, steady capex — stock jumped ~8% after hours and as much as +14% at Thursday's open, now trading above its 200-day EMA for the first time since the May/June selloff. Already fully priced for the beat; not a fresh setup, and still extended from the gap. ([TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262063724-microsoft-msft-surged-8-after-q4-fy2026-earnings-azure-43-copilot-tradingkey))

**Sector rotation this month favors Financials, Health Care, Real Estate, and Energy over Technology and Communication Services — but we're already fully expressing that rotation.** Reporting corroborates our own book: XLF, XLV, XLE, and XLI (all four held) are the sectors gaining ground in July, while Tech/Comm Services (XLK/XLC, neither held) are July's laggards despite leading H1 2026. There is no clean unheld sector ETF to add here — XLRE (Real Estate, unheld) is nominally in the "gaining" group per headline coverage, but its own technicals are soft (MACD turned negative 6/30, momentum indicator below zero since 7/8) and its rate-cut thesis is weakened by the hawkish 7/29 FOMC hold — not a clean falsifiable setup. XLB, XLU, XLP, XLY, XLC, XLK checked via live quote, none showing a fresh breakout. ([ts2.tech market wrap](https://ts2.tech/en/stock-market-today-31-07-2026/), [IG International](https://www.ig.com/en/news-and-trade-ideas/us-mega-caps-lose-in-july-260729))

**LLY (not held) has a clean momentum + catalyst setup on paper but carries near-term earnings risk — pass for now, revisit after 8/5.** Trading near its 52-week high ($1,155.76 live vs. $1,249.45 high), retatrutide (next-gen obesity drug) succeeded in two more Phase 3 trials on 7/23, GLP-1 pill Foundayo recently approved. But Lilly reports Q2 earnings **Wednesday 2026-08-05** — only 3 trading days out — so a fresh entry now would ride straight into a binary event on top of already being correlated with the held XLV (healthcare) position. Re-screen after the print. ([Motley Fool](https://www.fool.com/investing/2026/07/07/eli-lilly-stock-hits-a-new-all-time-high-has-it-go/), [StockTitan](https://www.stocktitan.net/news/LLY/lilly-confirms-date-and-conference-call-for-second-quarter-2026-tdamwlrchgj3.html))

**COST (not held) checked, not a clean setup.** -14.7% off its 52-week high, in a pullback from May highs despite a solid fiscal Q3 (net sales +11.6% y/y) — not near highs, not a momentum candidate today.

## Screened all three edges — nothing cleared the bar

- **Momentum/trend:** AMZN and MSFT are both real gap-driven moves, both explicitly the kind of chase `config/strategy.md` warns against. Rest of `momentum_watchlist` checked live (NVDA $197.28, GOOGL $334.82, META $538.67, AVGO $388.12, AMD $485.08, TSLA $307.47, JPM $350.88, COST $953.92, LLY $1155.76, NFLX $73.16) plus `theme_etfs` (QQQ $685.92, SMH $543.48, XBI $151.79, GLD $377.17) — nothing else shows a clean, un-owned, non-event-risk uptrend today.
- **Catalyst:** AMZN, AAPL, MSFT are this week's dated catalysts — AMZN/MSFT already gapped (don't chase), AAPL is a held-position risk item, not a new idea.
- **Relative-strength rotation:** XLF/XLV/XLE/XLI (all held) remain the cleanest expression of the broadening rotation; the one unheld candidate in the "gaining" group, XLRE, fails on its own technicals (negative MACD/momentum since early July) and weakened rate-cut thesis post-FOMC. Adding a second name in an already-held sector (e.g. JPM alongside XLF) would concentrate, not diversify.

## Ranked ideas

**None actionable today.** All three weekly slots (2026-W31, 0/3 used) held in reserve. Priority for market-open is managing the existing book, not adding to it — specifically checking AAPL's stop status after its guidance-driven plunge.

| Symbol | Edge | One-line thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|
| AMZN | Catalyst (earnings beat) | Genuine AWS/AI-driven beat (AWS +36.7% y/y), but today's +8-12% pre-market move is a blow-off gap with no margin of safety — wait for a multi-day base before considering entry. | Wait, re-evaluate on a pullback/base | 10% | Low — not actionable today |
| LLY | Momentum/trend + catalyst | Near 52-week highs on genuine GLP-1 pipeline catalysts (retatrutide Phase 3 success 7/23), but reports earnings Wed 2026-08-05 — 3 trading days out — too close to enter fresh into binary event risk, and correlates with held XLV. | Re-screen after 8/5 print | 8-10% (tighter given valuation) | Low — event risk too close |

## Notes for the open routine

- **AAPL (held, 8% trail, order `54f22517`) fell -6.65% to -7.3% pre-market on weak forward guidance despite an EPS/revenue beat — check stop status first thing at the open**, live pre-market quote $308.43 vs. Thursday's ~$333 close (entry $327.57). Pre-market moves don't trigger the trail, but this is the single biggest overnight risk to the book. Tightening/discretionary-cut both still blocked by the standing `scripts/alpaca.py` cancel/replace tooling gap if the thesis needs reassessing rather than just watching the stop.
- **Do not chase AMZN or MSFT's gaps** — both real catalysts, both already priced in; log as watch items for a future pullback/base, not today's entries.
- **XLRE flagged again as a rotation candidate but rejected on technicals** (negative MACD since 6/30, momentum below zero since 7/8) — don't add it reflexively just because headline coverage calls real estate a July winner; re-verify a real breakout before considering it.
- **IWM's 50-day-MA watch carries over** — was resolving well as of 7/30's close ($292.63 vs. stale ~$290.80 reference); re-verify at the open.
- 3 of 3 weekly satellite slots remain unused and available (2026-W31) — re-run this scan fresh next session once AAPL's stop situation and AMZN's post-earnings base (if any) are clearer.

## Sources

- [Apple (AAPL) Q3 2026 earnings report: Live updates — CNBC](https://www.cnbc.com/2026/07/30/apple-earnings-live-updates.html)
- [Apple's Earnings Will Test Stock's Status as the AI Safety Play — Bloomberg](https://www.bloomberg.com/news/articles/2026-07-30/apple-s-earnings-will-test-stock-s-status-as-the-ai-safety-play)
- [Stock Market Today, July 30: Amazon Soars Over 8% After Hours on Earnings Beat — Motley Fool](https://www.fool.com/coverage/stock-market/2026/07/30/stock-market-today-july-30-amazon-soars-over-8-after-hours-on-earnings-beat/)
- [Amazon (AMZN) Q2 earnings report 2026 — CNBC](https://www.cnbc.com/2026/07/30/amazon-amzn-q2-earnings-report-2026.html)
- [Microsoft (MSFT) Surged 8% After Earnings — TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262063724-microsoft-msft-surged-8-after-q4-fy2026-earnings-azure-43-copilot-tradingkey)
- [Stock Market Today: Live Updates 31.07.2026 — ts2.tech](https://ts2.tech/en/stock-market-today-31-07-2026/)
- [S&P 500 sector rotation broadens as mega-caps shed $658bn — IG International](https://www.ig.com/en/news-and-trade-ideas/us-mega-caps-lose-in-july-260729)
- [Eli Lilly Stock Hits a New All-Time High: Has It Gotten Too Expensive to Buy? — Motley Fool](https://www.fool.com/investing/2026/07/07/eli-lilly-stock-hits-a-new-all-time-high-has-it-go/)
- [Eli Lilly Q2 2026 Results Set for Aug. 5 Call — StockTitan](https://www.stocktitan.net/news/LLY/lilly-confirms-date-and-conference-call-for-second-quarter-2026-tdamwlrchgj3.html)
- [Defying Rate Pressures: Real Estate ETFs Outpace the Broader Market — ETF Trends](https://www.etftrends.com/equity-etf-content-hub/defying-rate-pressures-real-estate-etfs-outpace-the-broader-market/)

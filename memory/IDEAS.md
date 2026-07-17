# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-07-17 (pre-market)_

**No actionable entries today — 0 of 3 weekly satellite slots remain.** `counters.json`: `new_positions_this_week: 3`, week `2026-W29` (XLI 7/13, XLE 7/14, AAPL 7/16 already used this week). The cap is hard — `scripts/risk.py` will refuse any new-position buy regardless of conviction until 2026-W30 opens Monday 2026-07-20. Loss cap not tripped (day P&L -0.61%, equity $99,688.15, per `risk.py status`). Market currently closed (`clock`: next open 09:30 ET today, normal Friday session).

## Market read (2026-07-17 pre-market)

Risk-off tone carrying over from Thursday's tech-led selloff: the S&P 500 fell 0.51% and the Nasdaq dropped 1.47% on 2026-07-16 as chip stocks slid after TSMC raised its 2026 capex guidance to $60-64B (from $52-56B) — strong Q2 beat overshadowed by spending-concerns ([Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-sp-500-nasdaq-futures-slip-after-samsung-results-spark-chip-sell-off-223015294.html)). Alphabet fell over 4% on a report that Gemini 3.5 Pro's release is being delayed. **Netflix fell more than 8% in after-hours trading Thursday** after in-line Q2 results (EPS $0.80 vs $0.79 est., revenue $12.56B vs $12.59B est., +13% y/y) but guidance read as another quarter of decelerating growth ([CNBC](https://www.cnbc.com/2026/07/16/netflix-nflx-earnings-q2-2026.html), [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-16/stock-market-today-dow-s-p-live-updates)). Nasdaq 100 futures were down another ~0.3% heading into today. June retail sales also missed (+0.2% m/m vs +0.3% consensus). None of this is new-position actionable today given the slot cap, but it's directly relevant to two existing satellites — see Notes below.

Sector relative-strength: **Technology (XLK) still shows the largest YTD gain (+25.8%) among the SPDRs**, but day-to-day leadership has been volatile and Industrials (XLI) and Financials (XLF) are described as gaining 1-3mo relative strength, broadening participation beyond mega-cap tech ([tradewithmaya.com](https://tradewithmaya.com/sector-rotation)). Communication Services (XLC) remains the clear YTD laggard (-9.8%) and got another headwind today from the Alphabet news (GOOGL is one of XLC's largest weights). **Real estate (XLRE) is the one sector not currently in our book showing a clean, confirmed technical setup** — see ranked idea below.

## Ranked ideas

| Rank | Symbol | Edge | Thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|---|
| 1 | XLRE | Relative-strength rotation | XLRE moved above its 50-day MA on 2026-06-22 (confirmed trend change, not a one-day pop), is +10.6% YTD and only ~2.7% off its 52-week high, outpacing the broader market this month on a rate-stabilization/anticipated-cuts tailwind plus a genuine secondary catalyst (data-center REIT demand from AI infrastructure buildout). Falsifiable: thesis breaks if XLRE closes back below its 50-day MA or REIT-favorable rate expectations reverse. | ~$45.47 (current) | 10% (default) | Medium |

**This idea is queued for 2026-W30 (opens Monday 2026-07-20), not actionable today** — re-verify price/technicals fresh at that open before sizing; three trading days will have passed.

## Watch list (not actionable — slot limit, unconfirmed, or event risk)
- **COST:** Below its 200-day MA, off ~14% from its May all-time high — a pullback, not a confirmed uptrend. Pass.
- **GLD:** ~27% below its January 2026 record ($509.70 vs. current ~$370) with reported $14.4B of outflows since March — not near highs, not a confirmed trend, doesn't clear the momentum bar. Pass.
- **AI-infra chip names (NVDA/AVGO/AMD) and broader semis:** Extending Thursday's TSMC-capex-driven selloff, same "story real, trend not confirmed" pattern that has caused repeated passes this month. Pass.
- **GOOGL / XLC:** Fresh negative catalyst (Gemini 3.5 Pro delay report, -4% reaction) on top of the sector's existing YTD laggard status. No edge here in either direction worth acting on.
- **NFLX:** Post-earnings reaction (-8% after-hours) reads as a broken/decelerating-growth story, not a dip-buy setup. Pass; not in `config/universe.yaml` as a standalone name regardless.

## Notes
- No untapped sector (XLY, XLP, XLU, XLB, XLC) besides XLRE turned up a confirmed momentum, catalyst, or RS-rotation signal this session.
- Existing satellites, no changes recommended (pre-market does not trade): **XLF, XLI, XLE, XLV** — no fresh news found that breaks any of these theses; unaffected by today's tech-specific selloff.
- **Flag for the open/midday routine — XLK's falsifiable thesis line has likely been crossed.** `scripts/alpaca.py quote XLK` reads **$177.49**, below the ~$178.6 50-day MA that has been tracked as XLK's break level since 2026-07-13 (sector has sat in the "Lagging" RS quadrant the whole time). XLK is also now the worst-performing satellite (-6.1% since entry per `portfolio.py`), and today's backdrop (TSMC capex concerns, GOOGL Gemini delay, broad chip-complex weakness) is incremental bad news for the same AI-infrastructure-capex theme XLK's thesis rests on, not a one-off wobble. Per `config/strategy.md`'s exit rules ("if a position's thesis is broken... close it early rather than wait for the stop"), this is the clearest present case for a discretionary cut — the open routine should re-verify the current 50-day MA and price at the open (pre-market prices can differ from the live open print) before deciding, since this routine does not trade.
- The `scripts/alpaca.py` stop-tightening gap (see `memory/LESSONS.md`) remains open and unresolved.

## Sources
- [Stock market today: Dow, S&P 500, Nasdaq fall as semiconductors sell off — Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-sp-500-nasdaq-futures-slip-after-samsung-results-spark-chip-sell-off-223015294.html)
- [Stock Market Today: Dow, S&P Live Updates for July 17 — Bloomberg](https://www.bloomberg.com/news/articles/2026-07-16/stock-market-today-dow-s-p-live-updates)
- [Netflix (NFLX) earnings Q2 2026 — CNBC](https://www.cnbc.com/2026/07/16/netflix-nflx-earnings-q2-2026.html)
- [RRG Chart: XLK Leading Growth Rally - July 2026 Sector Rotation — tradewithmaya.com](https://tradewithmaya.com/sector-rotation)
- [XLRE ETF Technical Analysis — swingtradebot.com](https://swingtradebot.com/equities/XLRE)
- [State Street Real Estate Select Sector SPDR ETF (XLRE) Analysis — tickeron.com](https://tickeron.com/ticker/XLRE/)
- [Costco Wholesale (COST) Stock Price & Overview — stockanalysis.com](https://stockanalysis.com/stocks/cost/)
- [Gold Price Outlook For July 2026 — Yahoo Finance](https://finance.yahoo.com/markets/commodities/articles/gold-price-outlook-july-2026-191408891.html)

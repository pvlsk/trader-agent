# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-07-28 (pre-market)_

**0 actionable new entries recommended today, despite 3/3 weekly satellite slots being open (2026-W31, `counters.json`/`risk.py status` confirm 0/3 used).** Market closed at read time (`clock`: next open 09:30 ET today, normal Tuesday session). Loss cap not tripped (day P&L +0.14%, equity $99,485.11 per `risk.py status`). This is a deliberate "do nothing" call for the second day running, not a failure to find setups — see reasoning below.

## Market read (2026-07-28 pre-market)

**Day 2 of the most event-dense week the desk has traded through, and a new negative catalyst has appeared overnight.** FOMC decision is tomorrow, Wed 2026-07-29 at 2:00pm ET (Chair Warsh presser 2:30pm ET) — CME-implied odds favor a hold (~65%) with September-hike odds now up to ~82%, a data-dependent-pause read, not a clean directional signal. MSFT/META report tomorrow evening, AAPL/AMZN Thursday evening. **Visa (V) — an existing satellite — reports fiscal Q3 earnings TODAY after the close** (2:00pm PT / 5:00pm ET webcast); Zacks consensus is $3.23 EPS / $11.35B revenue (+11.6% y/y). This is same-day event risk on a held position, not a new-entry question, but it argues further against adding fresh risk today. ([Visa IR: Q3 2026 results July 28](https://investor.visa.com/news/news-details/2026/Visa-to-Announce-Fiscal-Third-Quarter-2026-Financial-Results-on-July-28-2026/default.aspx), [Zacks Q3 preview via Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/visas-q3-earnings-could-catalyst-162700784.html))

**New overnight negative catalyst: the chip/semiconductor rout is deepening, directly bearing on our existing XLK satellite.** A sell-off in Korean memory makers (SK Hynix, Samsung both down >10%, KOSPI's 8th circuit breaker of 2026) spread overnight on renewed "AI circular financing" concerns and a report that China has begun mass production of homegrown DUV chip-making tools. Nasdaq-100 futures fell ~0.9-1% pre-market even as Dow futures rose ~0.6% on cooler yields and other earnings beats (KO, SHW, Baker Hughes — none in our universe) — a narrow, chip-specific move, not a broad risk-off tape. Live XLK quote **$174.50**, further below its already-broken ~$178.6 50-day-MA line (XLK's thesis has been broken and un-cuttable since 2026-07-23 per the standing `scripts/alpaca.py` tooling gap — no change, no re-attempt this routine, research-only). **This rules out any new tech/semiconductor entry today regardless of technicals** — SMH ($548.29 live), AVGO, NVDA, AMD are all sitting in the eye of this exact rout. ([Bloomberg: Chip Rout Deepens on China Competition, Circular Funding Fears](https://www.bloomberg.com/news/articles/2026-07-28/korean-stocks-sink-as-chipmakers-plung-on-deepening-ai-fatigue), [Yahoo Finance: Nasdaq futures slide as chip sell-off deepens](https://finance.yahoo.com/markets/live/stock-market-today-tuesday-july-28-dow-sp-500-nasdaq-082832371.html))

**Oil's decline (which threatens the existing XLE satellite's catalyst) extended again overnight.** WTI dropped a further ~3% to ~$80.11, Brent ~3.7% to ~$85.08, as the US-Iran fighting pause continues to hold. This is the second consecutive session of this move (first flagged 2026-07-27 pre-market) — XLE's own written thesis breaks "if oil gives back the Strait-disruption premium," which is exactly what's continuing to happen. Live XLE quote **$58.37**, still above its ~$56.80 50-day MA per yesterday's re-verification, but the trend is now two days running against the thesis — **flag for the open routine to re-verify XLE's MA cushion live, not just against yesterday's close.** ([CNBC: Oil price today, WTI/Brent, US-Iran fighting pause holds](https://www.cnbc.com/2026/07/28/oil-price-today-wti-brent-us-iran-hormuz.html))

**Portfolio backdrop still argues against adding new risk even with slots open.** The book carries 8 satellite positions plus the SPY core, roughly 105% invested, satellite sleeve above its 30% target band. Adding a 9th name today — into a live earnings report on an existing holding (V), a deepening chip rout with direct exposure via XLK, a weakening (but not yet broken) XLE catalyst, and the FOMC/mega-cap-earnings gauntlet still one and two days out — is not warranted. Per strategy discipline, holding all 3 slots in reserve for a second day is the correct call.

**Screened all three edges for a genuinely clean setup anyway — nothing cleared the bar:**
- *Momentum/trend:* No unheld universe name shows a fresh, confirmed uptrend/breakout today; the one live theme (semis) is moving against us, and mega-cap tech names (MSFT, META, AAPL, AMZN) report this week — better to wait for a confirmed post-earnings reaction than front-run into a report.
- *Catalyst:* Today's premarket earnings beats (KO, SHW, Baker Hughes) are all outside `config/universe.yaml` — no actionable catalyst on a tradable name found.
- *Relative-strength rotation:* Checked live quotes on all 6 unheld sector ETFs — XLB $51.39, XLC $107.66, XLP $85.38, XLU $45.66, XLY $110.86, XLRE $45.76. Some commentary flags a defensive rotation (XLP/XLU/XLRE gaining ground) but the sourcing found is dated to 2026-07-07, not a fresh this-week confirmation; today's live prints are mixed (XLP/XLY/XLC up from yesterday's read, XLU/XLRE down) — no clean, dated breakout on any of them yet.

## Ranked ideas

**None actionable today.** Same call as yesterday, reinforced by a new negative catalyst (deepening chip rout hitting our existing XLK exposure) and a live earnings event on an existing holding (V, reports after today's close). If the Fed decision and MSFT/META/AAPL/AMZN earnings produce a clean post-event confirmation later this week, that is a better-timed entry than anything screened this morning.

## Watch list (not actionable, needs fresh confirmation post-FOMC/earnings)
- **XLP / XLU / XLRE (defensives):** Possible rotation beneficiaries if the chip rout or a Fed/earnings surprise triggers a broader flight from growth — commentary is directional but stale; needs a fresh, dated confirmation before it's actionable.
- **XLB (materials):** Recurring "Leading" RS mentions in screens but no clean confirmed breakout price action yet.
- **XLC / XLY:** No fresh confirming technical or catalyst evidence this week.

## Notes for the open routine
- **V reports fiscal Q3 earnings TODAY after the close (~5:00pm ET)** — rides through the session on its existing 10% trail only; reassess once results are out (tomorrow's routines), tightening/cutting still blocked by the standing tooling gap regardless.
- **Re-verify XLE live against its 50-day MA at the open** — oil fell a further ~3% overnight (WTI ~$80, Brent ~$85), second consecutive session against the thesis; not yet broken per the 50-day MA but the cushion should be checked fresh, not assumed from yesterday's read.
- **XLK's thesis remains broken and un-cuttable** (standing `scripts/alpaca.py` cancel/replace-order tooling gap, documented since 2026-07-14) — a new negative catalyst (deepening chip-sector rout) makes this worse, not better; no action possible until the trailing stop fires on its own or the tooling gap is fixed.
- **No new tech/semiconductor satellite should be considered this week** — Korean memory-maker sell-off + AI circular-financing concerns are actively hitting the sector our XLK/AAPL exposure sits in.
- **FOMC decision tomorrow, Wed 2026-07-29, 2:00pm ET**, MSFT/META report tomorrow evening, AAPL/AMZN Thursday evening — expect elevated volatility across the whole book through Thursday.
- 3 of 3 weekly satellite slots remain unused and available (2026-W31) if a genuinely clean post-event setup appears later this week.

## Sources
- [Visa to Announce Fiscal Third Quarter 2026 Financial Results on July 28, 2026 — Visa IR](https://investor.visa.com/news/news-details/2026/Visa-to-Announce-Fiscal-Third-Quarter-2026-Financial-Results-on-July-28-2026/default.aspx)
- [Visa's Q3 Earnings Could be a Catalyst: Should You Buy Now? — Yahoo Finance / Zacks](https://finance.yahoo.com/markets/stocks/articles/visas-q3-earnings-could-catalyst-162700784.html)
- [Stock market today: S&P 500, Nasdaq futures slide as chip sell-off deepens, but Dow rises — Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-tuesday-july-28-dow-sp-500-nasdaq-082832371.html)
- [Chip Rout Deepens on China Competition, Circular Funding Fears — Bloomberg](https://www.bloomberg.com/news/articles/2026-07-28/korean-stocks-sink-as-chipmakers-plung-on-deepening-ai-fatigue)
- [Oil price today, WTI, Brent, US-Iran fighting pause holds — CNBC](https://www.cnbc.com/2026/07/28/oil-price-today-wti-brent-us-iran-hormuz.html)
- [Fed July FOMC Meeting Preview — TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262054021-july-fomc-fed-oil-us-oil-tradingkey)
- [Will the Federal Reserve raise interest rates? Experts predict for July's meeting — CBS News](https://www.cbsnews.com/news/fed-interest-rate-decision-july-meeting/)
- [The Rotation Into Consumer Staples: Defensive Strength in an Uncertain 2026 — Investing.com](https://www.investing.com/analysis/the-rotation-into-consumer-staples-defensive-strength-in-an-uncertain-2026-200674622)

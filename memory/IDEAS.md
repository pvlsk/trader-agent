# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-07-20 (pre-market)_

**2 actionable ideas today, 3 of 3 weekly satellite slots available.** `counters.json` rolled to week `2026-W30` with `new_positions_this_week: 0` — full weekly cap available. Loss cap not tripped (day P&L +0.30%, equity $99,845.14, per `risk.py status`). Market currently closed (`clock`: next open 09:30 ET today, normal Monday session).

## Market read (2026-07-20 pre-market)

Futures are modestly higher (Dow +0.2%, S&P +0.3%, Nasdaq-100 +0.7%) as markets wait on this week's Big Tech earnings (GOOGL, TSLA, IBM among others) and shrug off the U.S. conducting fresh airstrikes on Iran overnight, plus confirmation of another American service-member death — oil has actually turned *lower* despite the strikes ([Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-monday-july-20-dow-sp-500-nasdaq-111429441.html), [TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-july-20-2026)). Broader 2026 sector-rotation story continues: Staples (+15% YTD), Industrials (+12% YTD), Energy (+21% YTD), and Materials (+17% YTD) have led while mega-cap tech has cooled, and small caps have broadened participation — the Russell 2000 is on pace for its best first half since 1991 (~+21%). This directly supports our existing **XLI** and **XLE** satellites (no changes needed) and is the backdrop for the new **IWM** idea below.

Sector technicals checked across all 11 SPDRs this morning (`alpaca.py quote`): of the six sectors we don't currently hold (XLY, XLP, XLU, XLB, XLRE, XLC), **none cleared a clean, unambiguous confirmed-uptrend bar** — XLP and XLB both show conflicting moving-average signals (50-day vs. 200-day, or MA-crossover vs. daily technical rating disagreeing), and XLRE (queued from last Friday) has a new headwind — see Watch list. No new sector-ETF idea today; both ranked ideas below come from single-name momentum/catalyst and the small-cap breadth theme instead.

## Ranked ideas

| Rank | Symbol | Edge | Thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|---|
| 1 | V | Momentum/trend + catalyst | Visa closed at a fresh 52-week high ($365.14, 2026-07-16) and trades above its 200-day MA, up ~5% on the week after Baird raised its price target to $412 (from $370) on strong fiscal Q2 results (EPS $3.31 vs. $3.10 est., revenue +17% y/y — strongest since 2013) plus a real, verifiable secondary catalyst: Visa launched an AI-agent commerce platform ("Visa Intelligent Commerce") and a stablecoin settlement platform at its Payments Forum. Falsifiable: thesis breaks if V closes back below its 50-day MA or gives back this week's breakout gains. **Note:** Visa reports fiscal Q3 earnings 2026-07-28 (8 days out) — not a blocker for a swing entry now, but a real event-risk date to be aware of; consider tightening the trail or reassessing before that date if still held. | ~$358.50 (current) | 10% (default) | High |
| 2 | IWM | Momentum/trend | Small caps are leading a genuine market-breadth rotation away from mega-cap tech: IWM trades above both its 50-day MA (~$290.80) and 200-day MA (~$271.34), sits only ~2.4% off its 52-week high ($302.72), and the Russell 2000 is on pace for its best first half since 1991 (~+21% YTD, +32% over the trailing 12 months). This diversifies the satellite sleeve away from our sector-ETF concentration (XLE/XLF/XLI/XLK/XLV) into a broad-market breadth theme. Falsifiable: thesis breaks if IWM closes back below its 50-day MA or small-cap leadership rolls over back to mega-cap tech. | ~$293.89 (current) | 10% (default) | Medium |

**Both ideas fit within the 3 remaining weekly slots (2026-W30) if taken — that would leave 1 slot open.** Re-verify both at the live open; pre-market reads can shift.

## Watch list (not actionable — unconfirmed, weakened, or event risk)
- **XLRE (real estate):** Was the queued #1 idea last Friday (2026-07-17) on a rate-stabilization + data-center-REIT tailwind. That thesis has weakened since: data-center REITs (XLRE's primary 2026 growth driver, led by Equinix/Digital Realty) declined this month on new regulatory halts over power/water usage concerns, even as residential/industrial REITs picked up some slack. Sector-wide return (+11.1% YTD) still beats SPY, but the specific catalyst that made it attractive is now mixed rather than clean. **Downgrading to watch-list — re-verify if the regulatory overhang clears.**
- **XLP (staples) / XLB (materials):** Both are 2026 YTD leaders per broad sector-rotation coverage, but neither clears our technical bar right now — XLP shows a 50-day/200-day MA divergence (short-term sell, long-term buy) and a mixed daily signal; XLB shows a similar divergence (bullish YTD trend but a "strong sell" daily technical read). Story is real, confirmation isn't clean enough yet. Pass.
- **COST:** Whipsawing around its 200-day MA all of June/July (fell below, has since recovered slightly above), "middle of its 52-week range," and 52-week return is still negative (-6.7%). Not a confirmed uptrend. Pass.
- **AI-infra chip names (NVDA/AVGO/AMD) and broader semis:** Same sector our existing XLK satellite is down ~4.2% on with a broken thesis (still below its tracked ~$178.6 50-day MA at $175.55). Adding single-name chip exposure here would concentrate risk into a sector we're already overweight and wrong on. Pass.
- **Big Tech earners this week (GOOGL, TSLA, IBM, INTC):** Pure event risk with reports still pending — not tradable on a confirmed catalyst yet. Not in our universe as standalone momentum names besides GOOGL (via XLC, which we don't hold). Pass.

## Notes
- Existing satellites, no changes recommended (pre-market does not trade): **XLE** and **XLI** are directly reinforced by this morning's read (energy/industrials still sector leaders, fresh Iran-strike headlines relevant to XLE though oil is actually softer today); no fresh news found breaking the **XLF** or **XLV** theses either.
- **Carryover flag for the open routine — XLK's thesis is still broken and still un-cuttable.** Documented since 2026-07-17: price ($175.55 as of this morning) remains below the tracked ~$178.6 50-day MA, sector still lagging, position is the worst satellite performer (-4.2% since entry). The discretionary-cut attempt has been rejected twice already (`held_for_orders` — `scripts/alpaca.py` has no cancel/replace-order subcommand while the trailing stop holds the shares; see `memory/LESSONS.md`). No new information changes this — still blocked, still carrying over. The only live exit path remains the 10% trailing stop triggering on its own.
- The `scripts/alpaca.py` stop-tightening/cancel-order gap (see `memory/LESSONS.md`) remains open and unresolved.

## Sources
- [Stock market today: Dow, S&P 500, Nasdaq futures edge up as oil turns lower — Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-monday-july-20-dow-sp-500-nasdaq-111429441.html)
- [Stock Market Today (July 20, 2026): Dow futures climb as U.S. strikes Iran again — TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-july-20-2026)
- [Is a Stock Market Rotation Underway? These Sectors Are Outpacing Tech in 2026 — Morningstar](https://www.morningstar.com/markets/is-stock-market-rotation-underway-these-sectors-are-outpacing-tech-2026)
- [Visa Stock Hit a New 52 Week High This Week. Here's What's Driving It — tikr.com](https://www.tikr.com/blog/visa-stock-hit-a-new-52-week-high-this-week-heres-whats-driving-it)
- [Visa stock hits 52-week high at 359.68 USD — Investing.com](https://www.investing.com/news/company-news/visa-stock-hits-52week-high-at-35968-usd-93CH-4773688)
- [Data Centers Are the Hot New REITs. Should You Invest $1,000? — The Motley Fool](https://www.fool.com/investing/2026/07/17/data-centers-are-hot-new-reits-should-you-invest/)
- [Real Estate Is Up 13%. The Data-Center REITs Powering AI Are Up 36%. — 24/7 Wall St.](https://247wallst.com/investing/2026/07/12/real-estate-is-up-13-the-data-center-reits-powering-ai-are-up-36/)
- [XLB: Pivot Points Indicate Market Sentiment for Materials Sector — gurufocus.com](https://www.gurufocus.com/news/8960010/xlb-pivot-points-indicate-market-sentiment-for-materials-sector?mobile=true)
- [Consumer Staples Sector SPDR (XLP) Pivot Points Analysis — gurufocus.com](https://www.gurufocus.com/news/8962353/consumer-staples-sector-spdr-xlp-pivot-points-analysis?mobile=true)
- [Costco Stock Falls Below 200-Day Moving Average — dividendchannel.com](https://www.dividendchannel.com/article/202606/costco-stock-falls-below-200-day-moving-average-as-technical-momentum-weakens-COST06182026200.htm/)

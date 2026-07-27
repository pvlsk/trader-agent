# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-07-27 (pre-market)_

**0 actionable new entries recommended today, despite 3/3 weekly satellite slots being open (2026-W31, `counters.json`/`risk.py status` confirm 0/3 used).** Market closed at read time (`clock`: next open 09:30 ET today, normal Monday session). Loss cap not tripped (day P&L +0.83%, equity $100,102.93-109.92 per `risk.py status`/`portfolio.py`). This is a deliberate "do nothing" call, not a failure to find setups — see reasoning below.

## Market read (2026-07-27 pre-market)

**This is the single most binary-event-heavy week the desk has traded through.** The FOMC meets Tue-Wed with the rate decision Wednesday 2026-07-29 at 2:00pm ET (Chair Warsh presser 2:30pm ET). Four of the "Magnificent Seven" report this week, all after the close: **Microsoft and Meta on Tuesday 7/29 (same day as the Fed decision)**, **Apple and Amazon on Thursday 7/30**. Our own book has direct exposure to two of these dates already: **V reports fiscal Q3 earnings tomorrow, 2026-07-28** (already flagged as forward event-risk in `memory/STATE.md`), and **AAPL — an existing satellite — reports Thursday 7/30**, a new forward-event-risk date that should be reassessed/tightened before then if still held. ([TradingKey: Fed, Apple, Microsoft, Meta, Amazon earnings this week](https://www.tradingkey.com/analysis/stocks/us-stocks/262054300-weekly-preview-fed-apple-microsoft-meta-amazon-earnings-reports-tradingkey), [FXLeaders: Top Earnings to Watch July 27-31](https://www.fxleaders.com/news/2026/07/26/top-earnings-to-watch-this-week-july-27-31-what-to-expect-from-msft-meta-aapl-amzn-ko-ba-and-f/))

**Weekend macro shift — oil collapsed on an Iran de-escalation, directly threatening the existing XLE satellite's catalyst.** The US and Iran paused military strikes over the weekend; Brent fell as much as 7.4% to below $90/bbl and WTI fell ~7.7% to ~$83.51 as of today. XLE's own written thesis (`memory/STATE.md`) is explicit that it "breaks if... oil gives back the Strait-disruption premium (ceasefire actually holds this time)" — that is precisely what appears to be happening. Futures are broadly risk-on this morning (Dow/S&P futures +0.8%, Nasdaq-100 futures +~1.6%) on the same de-escalation news, so the tape itself won't flag this as a problem — only a direct look at XLE and oil will. **Priority flag for the open routine: re-verify XLE live at 09:30 ET against both its 50-day MA and the oil move, not just its price relative to Friday's close** — a broadly green tape could mask a broken-but-still-slightly-up XLE the same way it could mask a break in any other name. ([CNBC: Oil prices slide, Brent below $90 as Iran pause holds](https://www.cnbc.com/2026/07/27/oil-price-wti-brent-slide-as-iran-reportedly-may-halt-attacks.html), [FXLeaders: WTI slides toward $84 as Iran truce eases supply fears](https://www.fxleaders.com/news/2026/07/27/wti-oil-price-forecast-usoil-slides-84-iran-truce-fed/))

**Portfolio backdrop argues against adding new risk even with slots open.** The book already carries 9 satellite positions (~35.6% of equity, above the 30% satellite target) plus the SPY core (~69%), i.e. roughly 105% invested on a small margin draw (cash ~-$5,465, unchanged for weeks). Layering 1-3 more positions this week would push the satellite sleeve further over its own target band right as two existing satellites (V, AAPL) carry earnings-date event risk, XLE's catalyst may be reversing, and XLK remains thesis-broken and un-cuttable (standing tooling gap, `memory/LESSONS.md`). Per the strategy's own discipline ("prefer doing nothing over forcing a marginal trade"), the responsible call is to sit on all 3 slots this week rather than add a name into an FOMC + mega-cap-earnings gauntlet on top of an already fully-invested, already-concentrated book.

**Screened all three edges for a genuinely clean setup anyway — nothing cleared the bar:**
- *Momentum/trend:* Sector-rotation commentary (dated, imprecise) suggests tech (XLK) is nominally "leading" again and staples/communication (XLP/XLC) are lagging, but this is exactly the sector we're already overweight through XLK/AAPL/AMD (~12-13% combined) — no case for adding a fourth correlated name, and both of those names report/are exposed to Fed-day and earnings-day volatility this week regardless. ([Sector rotation coverage — dated, directional only, not a specific technical confirmation](https://tradewithmaya.com/sector-rotation))
- *Catalyst:* No confirmed, dated, verifiable catalyst found on an unheld universe name for entry timing this week — GM/RIVN/Ford-adjacent upgrades this morning are outside the universe (autos), and the Progressive (PGR) upgrade is outside the universe (insurance, not in `config/universe.yaml`).
- *Relative-strength rotation:* Checked live quotes on all 6 unheld sector ETFs (XLB $51.26, XLC $106.29, XLP $84.11, XLU $46.27, XLY $109.42, XLRE $45.94) — no source found a clean, dated, confirmed breakout above a rising 50-/200-day line for any of them this week; general commentary is directional and stale (May/June data), not a falsifiable this-week signal.

## Ranked ideas

**None actionable today.** Zero of the three edges produced a setup that both (a) is genuinely fresh/confirmed and (b) makes sense to add given the book is already over its satellite target heading into the most event-dense week since inception. Holding all 3 weekly slots in reserve is the correct call — if the Fed/earnings gauntlet this week produces a clean post-event confirmation (e.g., a name that gaps and holds after reporting, not fades), that is a better-timed entry than anything screened this morning.

## Watch list (not actionable, needs fresh confirmation post-FOMC/earnings)
- **XLU / XLP (defensives):** Plausible beneficiaries if the Fed decision or a Big Tech earnings miss triggers a rotation out of growth — no confirmed setup yet, pure watch.
- **XLB (materials):** Has shown intermittent YTD strength in prior weeks' screens but contradictory near-term technical reads each time it's been checked — still not a clean breakout.
- **XLC / XLY / XLRE:** No fresh confirming technical or catalyst evidence this week.

## Notes for the open routine
- **Urgent: re-verify XLE live against oil's ~7.7% weekend drop and its 50-day MA** — the written thesis's own falsifiable break condition (ceasefire holding, oil giving back the Hormuz premium) appears to be happening; a green tape elsewhere could mask this.
- **V reports fiscal Q3 earnings tomorrow (2026-07-28)** and **AAPL reports Thursday (2026-07-30)** — both existing satellites carry near-term binary event risk; reassess/tighten trails before those dates if still held.
- **FOMC decision Wednesday 2026-07-29, 2:00pm ET**, with MSFT/META reporting the same evening and AAPL/AMZN Thursday — expect elevated volatility across the whole book Tue-Thu this week, not just in held names.
- **XLK's thesis remains broken and un-cuttable** (standing `scripts/alpaca.py` cancel/replace-order tooling gap, documented since 2026-07-14) — no change this routine, research-only.
- **No new tech/semiconductor satellite should be considered this week** regardless of technicals — the sleeve is already concentrated in XLK+AAPL+AMD and two of the week's biggest binary events (Fed + MSFT/META/AAPL earnings) land squarely on that complex.
- 3 of 3 weekly satellite slots remain unused and available (2026-W31) if a genuinely clean post-event setup appears later this week.

## Sources
- [Stock Market Today, July 27 — Bloomberg](https://www.bloomberg.com/news/articles/2026-07-26/oil-tumbles-as-us-and-iran-pause-military-strikes-markets-wrap)
- [Stock market next week: Outlook for July 27-31, 2026 — CNBC](https://www.cnbc.com/2026/07/24/stock-market-next-week-outlook-for-july-27-31-2026.html)
- [Stock market today: futures rise as oil tumbles — Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-monday-july-27-dow-sp-500-nasdaq-080412540.html)
- [Oil prices slide, Brent below $90 as Iran pause holds — CNBC](https://www.cnbc.com/2026/07/27/oil-price-wti-brent-slide-as-iran-reportedly-may-halt-attacks.html)
- [WTI Oil Price Forecast: slides toward $84 as Iran truce eases supply fears — FXLeaders](https://www.fxleaders.com/news/2026/07/27/wti-oil-price-forecast-usoil-slides-84-iran-truce-fed/)
- [The Week Ahead: Fed Rate Decision, Apple/Microsoft/Meta/Amazon earnings — TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262054300-weekly-preview-fed-apple-microsoft-meta-amazon-earnings-reports-tradingkey)
- [Top Earnings to Watch This Week, July 27-31 — FXLeaders](https://www.fxleaders.com/news/2026/07/26/top-earnings-to-watch-this-week-july-27-31-what-to-expect-from-msft-meta-aapl-amzn-ko-ba-and-f/)
- [RRG Chart: XLK Leading Growth Rally — July 2026 Sector Rotation](https://tradewithmaya.com/sector-rotation)

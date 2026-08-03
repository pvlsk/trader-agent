# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-08-03 (pre-market)_

**0 actionable new entries recommended today, despite 3/3 weekly satellite slots being open (2026-W32, `counters.json`/`risk.py status` confirm 0/3 used).** Market closed at read time (`clock`: next open 09:30 ET today). Loss cap not tripped (day P&L +0.42%, equity $99,931.83 per `risk.py status`). The relative-strength rotation edge that's genuinely working right now is already fully expressed via the 4 held sector ETFs, and every momentum/catalyst candidate screened today either fails the "near 52-week highs" test or is a stale/blown-off gap the strategy explicitly says not to chase.

## Market read (2026-08-03 pre-market)

Futures pointed higher into the open (Dow/S&P/Nasdaq all indicated up), oil fell sharply (Brent -5.7% to ~$83.77) on Trump calling off planned Iran strikes and announcing renewed diplomatic talks — a reversal of the supply-disruption premium that underpinned our XLE entry three weeks ago, worth watching but not yet a thesis break (XLE is still up double digits YTD on a broader uptrend, not just the Iran premium). Gold slipped slightly. It's a busy earnings week: Palantir reported Monday after this desk's close (not in universe), AMD reports Tuesday evening (held in `momentum_watchlist`, no fresh read yet — earnings haven't happened), SanDisk Wednesday, and McDonald's/Kraft Heinz/Costco/Disney also report this week. July's jobs report lands Friday 8/7. One large pharma catalyst — a reported Bristol Myers Squibb/AstraZeneca merger — is outside our universe and not actionable. ([TS2 market wrap](https://ts2.tech/en/stock-market-today-03-08-2026/), [TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-aug-3-2026-dow-futures-climb-as-oil-slides-on-renewed-iran-talks), [TradingKey earnings preview](https://www.tradingkey.com/analysis/stocks/us-stocks/262067492-august-3-7-2026-preview-palantir-amd-sandisk-earnings-nfarm-payrolls-tradingkey))

**Relative-strength rotation is already fully expressed via the book — no new sector ETF clears the bar.** Real-time sector-rotation tracking has Industrials (XLI) "Recovering," Financials (XLF) "Accelerating," Health Care (XLV) "Recovering," and Technology (XLK) "Fading" — i.e. the current leadership rotation is into the exact three sectors already held (XLI/XLF/XLV), while Energy (XLE, also held) remains the top 1-year performer (+36.6% vs. SPY +18.2%). Checked the six unheld sector ETFs live: XLB $50.41, XLRE $45.05, XLY $116.04, XLP $85.05, XLU $44.34, XLC $108.21 — no confirmed fresh breakout on any of them today, and none appear in the current "leading" quadrant reporting. XLK ($175.25) is explicitly fading — sits out despite strong 2026 YTD returns. ([Sector Rotation Monitor](https://sectorrotationmonitor.com/), [ETFdb top performers](https://etfdb.com/sector-investing-content-hub/xlk-xle-xli-top-performing-sector-spdrs/))

**Momentum watchlist: nothing near highs today.** MSFT ($463.20) posted the largest single-day market-cap gain in stock-market history on its 7/29 Azure-beat earnings (+15.5%), but even after that pop it sits ~16% below its 52-week high of $551.05 — this is a blow-off-gap-origin move three sessions old, not a fresh momentum setup, and chasing it now breaks the "avoid buying blow-off gaps" rule twice over (once for the gap itself, again for chasing days later). NVDA ($198.06) is ~17.5% off its 52-week high. AVGO ($383.01) is ~20% off its 52-week high ($495.00) despite a genuine AI-accelerator catalyst (Apple supply deal, custom silicon for Anthropic/OpenAI) — not near highs, fails the momentum entry checklist. COST ($951.61) is ~14.7% off its 52-week high ($1,096.50); a Bernstein upgrade (PT to $1,194, "top retail pick for H2 2026") is real but Costco's next earnings (fiscal Q4) isn't until late Sept/Oct, so there's no near-term catalyst to pair with the pullback. Rest of `momentum_watchlist`/`theme_etfs` checked live (AAPL $311.67 — not held, out of universe consideration since no fresh catalyst; GOOGL $355.13, META $567.00, AMD $476.03, TSLA $311.55, JPM $351.86, NFLX $71.69, QQQ $686.13, IWM $290.80, SMH $540.81 — mixed/volatile, no clean confirmed breakout, XBI $147.08, GLD $371.47) — nothing clears both the trend and non-extended bars simultaneously.

**LLY (not held) — same story as last week, still event risk, not yet actionable.** Reports fiscal Q2 earnings **Wednesday 2026-08-05 before the open** (2 trading days out) — market has priced in a ±8.4% earnings-day move. Real pipeline catalysts remain (raised FY2026 revenue guidance to $82–85B on GLP-1 strength), but entering 2 days ahead of a binary event this large, on top of correlation with the held XLV position, still fails the entry bar. Re-screen after the print. ([TipRanks earnings](https://www.tipranks.com/stocks/lly/earnings))

## Screened all three edges — nothing cleared the bar

- **Momentum/trend:** No `momentum_watchlist` or `theme_etfs` name is both in a confirmed uptrend AND near 52-week highs without extended/event-risk caveats today. MSFT/NVDA/AVGO/COST all checked and rejected on the "near highs" test.
- **Catalyst:** AMD/SanDisk earnings this week haven't happened yet (don't enter ahead of an unconfirmed print); LLY's print (8/5) is too close and correlated with held XLV; the BMY/AZN pharma merger and Palantir's report are both outside `config/universe.yaml`.
- **Relative-strength rotation:** The current leadership rotation (XLI/XLF/XLV recovering-to-accelerating, XLE still the top 1-year performer) is already fully expressed by 4 of our 6 held satellites. No unheld sector ETF (XLB/XLRE/XLY/XLP/XLU/XLC) shows a confirmed fresh breakout.

## Ranked ideas

**None actionable today.** All three weekly slots (2026-W32, 0/3 used) held in reserve. Priority for market-open is managing the existing book (verify all 6 satellite stops + core SPY unchanged), not adding to it.

| Symbol | Edge | One-line thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|
| LLY | Momentum/trend + catalyst | Raised FY26 guidance ($82-85B) on GLP-1 strength, but reports Wed 8/5 (2 trading days out, ±8.4% priced move) — too close to enter ahead of the print, and correlates with held XLV. | Re-screen after 8/5 print | 8-10% (tighter given valuation) | Low — event risk too close |
| COST | Catalyst (analyst upgrade) | Bernstein named it top H2-2026 retail pick, PT raised to $1,194, but -14.7% off 52-week high with no near-term earnings catalyst (fiscal Q4 not until Sept/Oct) — pullback without a trigger. | Re-screen if it reclaims its 50-day trend or a catalyst emerges | 10% | Low — no near-term trigger |

## Notes for the open routine

- **No new entries warranted at the open** — reconcile the existing book (SPY core + XLV/XLF/XLI/XLE/V/IWM satellites, all 6 stops) and note the oil-price reversal (Brent -5.7% on Iran de-escalation headlines) as a watch item for XLE's catalyst leg, though the broader uptrend thesis isn't broken by one day's move.
- **AMD reports earnings Tuesday evening** — held in `momentum_watchlist` only, not a current position; don't pre-position ahead of the print.
- **LLY reports Wednesday 8/5 before the open** — re-screen fresh after the reaction is known, don't enter ahead of it.
- 3 of 3 weekly satellite slots remain unused and available (2026-W32) — re-run this scan fresh next session once AMD's and LLY's earnings reactions are known.

## Sources

- [Stock Market Today: Live Updates 03.08.2026 — ts2.tech](https://ts2.tech/en/stock-market-today-03-08-2026/)
- [Stock Market Today (Aug. 3, 2026): Dow futures climb as oil slides on renewed Iran talks — TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-aug-3-2026-dow-futures-climb-as-oil-slides-on-renewed-iran-talks)
- [August 3-7, 2026 Preview: Palantir, AMD, SanDisk Earnings and Nonfarm Payrolls — TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262067492-august-3-7-2026-preview-palantir-amd-sandisk-earnings-nfarm-payrolls-tradingkey)
- [Sector Rotation Monitor — Real-Time Relative Strength](https://sectorrotationmonitor.com/)
- [Top-Performing Sector SPDRs: XLK, XLE & XLI Top The List — ETFdb](https://etfdb.com/sector-investing-content-hub/xlk-xle-xli-top-performing-sector-spdrs/)
- [Microsoft's stock rockets more than 15% for largest single-day jump in history — Yahoo Finance](https://finance.yahoo.com/technology/article/microsofts-stock-rockets-more-than-15-for-largest-single-day-jump-in-history-120144134.html)
- [Top analyst has bold Costco stock outlook for 2026 — TheStreet](https://www.thestreet.com/investing/stocks/cost-costco-stock-outlook-optimistic-bernstein-2026)
- [Eli Lilly (LLY) Earnings, Revenues Date & History — TipRanks](https://www.tipranks.com/stocks/lly/earnings)

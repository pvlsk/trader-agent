# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-09-03 (pre-market)_

**Two actionable candidates today, both compliant.** `risk.py status`: equity **$101,937.79**, day P&L **+0.05%** (loss cap -3% not tripped, no halt), **2026-W36, 0/3 weekly slots used** — full capacity (3 new positions allowed). A compliant 5% satellite position needs **$5,097**; cash was $11,635.75 as of last night's EOD (ample, not independently re-verified pre-market since `portfolio.py`/cash settle checks need the live market session). Market not yet open (`clock`: `is_open` false, checked 08:08 ET, next open 09:30 ET, next close 16:00 ET).

## Market read (2026-09-03 pre-market)

Futures are mixed/flat into the open: Dow +0.07%, S&P 500 -0.05%, Nasdaq-100 -0.11%, Russell 2000 -0.08% — a cautious tone as Wall Street weighs a resurgence in Middle East tension (renewed Strait of Hormuz friction) against upcoming labor-market data. The emerging rotation is exactly the one this desk is already positioned for: tech pulling back while **energy and materials sectors gain** this morning. The 10-year Treasury yield sits near a multi-year high (~4.82% as of Wednesday), a headwind for rate-sensitive sectors (real estate, growth tech) and a tailwind for value/cyclical names. Broadcom (AVGO) reported Q3 results after Wednesday's close that technically beat estimates but came with guidance read as "soft" on AI hardware — chip stocks (NVDA, AMD, MU, INTC) fell for a second straight session on the read-through; broader tech (XLK) is described by multiple sources as in a short-term slump tied to this chip-sector rotation away from pure AI-hardware plays. **Read-through: avoid chip/semiconductor names and XLK for now; energy and materials continue to be where the tape's genuine strength is, which lines up with the book's existing XLE/XLI tilt and today's two new ideas below.**

## XLI status (carried forward)

XLI's live price this morning is **$172.78**, still below the ~$173.6 50-day-MA line cited since 2026-08-31 — a fourth consecutive sub-line reading (open $172.38, midday $172.83, EOD $172.78-ish, now $172.78 pre-market), reinforcing that the thesis break is real, not noise. No change in status: position remains un-cuttable except by its own live trailing stop (structural cancel/replace gap, `LESSONS.md` 2026-07-17/23/24/24) — this routine places no trades regardless, flagging for the open/midday routines.

## Screened all three edges

- **Momentum/trend:** Full sector-ETF and momentum-watchlist scan this morning. Chip-adjacent names (AMD $456.51, NVDA $224.44, AVGO $354.33) are all working through the post-Broadcom-guidance selloff — not fresh breakouts, skip. Mega-cap tech broadly soft on the same rotation (XLK $183.62, off its highs, sector described as in a technical slump). **JPM ($356.22)** stands out: it has been in a clean, sustained uptrend since its July 14 Q2 beat (record markets/IB revenue, EPS $6.14) with analyst price targets subsequently raised into the $360-420 range (median ~$344, several revisions higher since) — price is still inside that analyst-target band, not a blow-off spike, and complements (does not duplicate) the existing XLF sector-ETF rotation position with a single-name catalyst expression.
- **Catalyst:** JPM's Q2 beat (verified, cited) remains the live, still-compounding catalyst — the board also announced a dividend raise to $1.65/share for Q3, a second concrete data point supporting the thesis. AVGO's post-earnings guidance read as soft, weighing on the whole chip complex — a real catalyst, but bearish, so it's a name/sector to avoid, not buy. No other fresh, verified, directional catalyst found on a universe name this morning.
- **Relative-strength rotation:** **XLB (Materials) has reclaimed clear separation above its ~$51.06 50-day MA**, now trading **$52.97** (up from $52.09 yesterday morning and $52.83 at yesterday's open-shift check) and close to its recent 52-week high ($54.14, set 2026-08-21). This is the second straight session of improvement after two prior pre-market shifts (09-01, 09-02) flagged it as directionally strong (copper/gold at record highs, AI-datacenter/electrification demand) but technically borderline (RSI ~37, price at/below the MA). The structural catalyst is unchanged and real: a single 1-GW AI data center needs ~50,000 tonnes of copper, and rising deficit/inflation concerns are separately supporting hard-asset demand. **Caveat: cached technical-analysis sources still show a stale-looking RSI ~37/"Strong Sell" read that appears not to have updated with today's price action** (it cites the identical $51.06 50-day-MA figure used yesterday) — trusting the live, directly-verified price-vs-MA relationship over that likely-stale RSI snapshot, but sizing conviction as Medium rather than High to reflect the ambiguity. This morning's tape (materials gaining while tech pulls back) is a same-direction confirmation. Today's futures/sector read (energy + materials up, tech down) also reinforces the existing XLE/XLI (broken thesis aside) rotation tilt — no rotation change indicated for currently-held names.

## Ranked ideas

| Rank | Symbol | Edge | One-line thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|---|
| 1 | JPM | Momentum/trend + catalyst | Clean uptrend since the July 14 Q2 beat (record markets/IB revenue, EPS $6.14), price ($356.22) still inside the post-earnings analyst-target range ($344-420, several raises since) with a fresh dividend-raise catalyst ($1.65/share, Q3) — not chasing a blow-off move ~7 weeks after the print. Falsifiable: thesis breaks if JPM closes back below its 50-day MA or gives back this run without a new catalyst. | ~$356 (near current) | 10% | Medium-High |
| 2 | XLB | Relative-strength rotation | Materials has reclaimed clear separation above its ~$51.06 50-day MA (now $52.97, up from $52.09/$52.83 the prior two mornings) on a real, ongoing structural catalyst — AI-datacenter copper demand (record COMEX copper) and inflation/hard-asset flows — with today's tape (materials up, tech down) confirming the direction. Falsifiable: thesis breaks if XLB closes back below its 50-day MA (~$51) or the copper/gold rally reverses. Caveat: a cached technical screen still shows a stale-looking weak RSI reading not obviously reflecting today's price — sized as Medium conviction, not High, pending a cleaner confirmation once the market opens. | ~$53 (near current) | 10% | Medium |

**Do not add a third name today** — nothing else screened (chip names, XLK, XLC/XLY/XLU/XLRE, TSLA) cleared the momentum/catalyst/RS bar; TSLA specifically was checked and rejected (still down ~23% YTD despite a 1-month bounce — not a confirmed uptrend, more narrative than verified catalyst). Two solid, differentiated ideas beat forcing a third. Both together would use 2 of the 3 available weekly slots.

## Notes for the open routine

- **JPM and XLB are both compliant and cash-supported** (cash $11,635.75 as of last EOD; each ~5% entry needs ~$5,097) — but re-verify settled cash and a live quote against each falsifiable line once the market opens before sizing, per standard practice.
- **XLI: fourth consecutive sub-$173.6 reading this morning ($172.78)** — treat the thesis as confirmed broken, unchanged from the last three shifts. Un-cuttable except by its own stop (cancel/replace gap) — no action possible, informational only.
- **XLE (held, +14%+ since entry) remains the standing extended-winner tighten candidate** — retightening still blocked by the cancel/replace tooling gap (`memory/LESSONS.md` 2026-07-24), unresolved for 7+ consecutive weekly reviews.
- **Avoid chip/semiconductor exposure (AMD, NVDA, AVGO, SMH, XLK)** for now — post-AVGO-earnings guidance read as soft, whole complex under pressure for a second session.
- Elevated 10-year yield (~4.82%, multi-year high) is a live macro risk for rate-sensitive names (XLRE, growth tech) — not a reason to act today, just context.

## Sources

- [Here are JPMorgan's favorite stocks as September gets underway — CNBC](https://www.cnbc.com/2026/09/02/here-are-jpmorgans-favorite-stocks-as-september-gets-underway.html)
- [JPMorgan Chase (JPM) Stock Analysis — Tickeron](https://tickeron.com/ticker/JPM/)
- [XLB: This Economically Sensitive Sector Is Breaking Out — Investing.com](https://m.investing.com/analysis/xlb-this-economically-sensitive-sector-is-breaking-out-200686367?ampMode=1)
- [Basic materials stocks jump to start 2026 — XLB rises as copper steadies and miners climb — ts2.tech](https://ts2.tech/en/basic-materials-stocks-jump-to-start-2026-xlb-rises-as-copper-steadies-and-miners-climb/)
- [Materials Select Sector SPDR ETF Technical Analysis — Investing.com](https://www.investing.com/etfs/spdr-materials-select-sector-etf-technical)
- [NVDA, INTC, AMD, MU: Major Chip Stocks Fall For Second Day After AVGO's Soft AI Guidance — TradingView News](https://www.tradingview.com/news/stocktwits:9e4b093a9094b:0-nvda-intc-amd-mu-major-chip-stocks-fall-for-second-day-after-avgo-s-soft-ai-guidance/)
- [Tech Stocks Are Experiencing Historic 50-Year Weakness — Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/tech-stocks-experiencing-historic-50-131501307.html)
- [Stock market news for Sept. 2, 2026 — CNBC](https://www.cnbc.com/2026/09/01/stock-market-today-live-updates.html)
- [Tesla Stock Has a Huge Catalyst Ahead — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/tesla-stock-huge-catalyst-ahead-160004955.html)

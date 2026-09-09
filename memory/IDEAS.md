# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-09-09 (pre-market, Wednesday) — market closed, checked 08:08 ET, next open 09:30 ET._

**One actionable idea this week, one watch-only.** `risk.py status`: equity **$101,142.83**, day P&L -0.31% (loss cap -3% not tripped), **2026-W37, 1/3 weekly slots used** (XLK entered 09-08; 2 slots remain). Cash not yet re-checked this shift (research routine doesn't trade — execution desk will confirm at the open).

## Market read (2026-09-09 pre-market)

Risk-off continues into a third session: the U.S. struck five Iranian tankers after Iran fired a ballistic missile at a U.S. Navy warship, keeping Brent/WTI near 6-week highs and adding fresh trade-tension noise with Canada. Futures are broadly red — Nasdaq/QQQ premarket ~-0.4%, reflecting cooling sentiment in tech/semis specifically, a reversal from the tech-resilience pattern of the last two sessions. Fed funds futures now price a **59% chance of a quarter-point hike** at the Sept 15-16 FOMC (CME FedWatch) — hawkish-leaning, worth weighing against any new entry's holding period. CPI prints Thursday 2026-09-11, FOMC decision Wednesday 2026-09-16 — both remain real, dated vol events inside the operative window.

## Held-position status (carried forward, informational only — no action, not a trade recommendation)

- **XLE (extended winner):** the oil-price spike from the widening Iran conflict is a tailwind reinforcing the existing thesis, not a new signal. Remains the standing tighten candidate, still blocked by the `scripts/alpaca.py` cancel/replace gap (`LESSONS.md` 2026-07-24 and multiple follow-ups) — not re-attempted here (research routine doesn't trade).
- **XLI:** recovery thesis (confirmed 2026-09-03 close) has now held above its ~$173.6 50-day MA every session since — durable at this point. Still un-cuttable except by its own stop.
- **XLK (new 09-08):** today's premarket tech/semis softness is the first real test since entry — flag for the open routine to check price against its 50-day MA (~$181.7) rather than assume yesterday's golden-cross read still holds unchanged.

## Screened all three edges

- **Momentum/trend:** **XBI's technical picture has flipped meaningfully bullish since last week's read** (which flagged a weak close and a multi-week Aroon downtrend as rollover risk). Current reads: 12 buy / 0 sell across the moving-average suite (Strong Buy), RSI(14) ≈66.6 (bullish, not yet overbought), MACD ≈+2.14 turned positive and rising. Price ≈$161.96 (alpaca quote), within ~5% of its 52-week high ($169.89) and, per multiple sources, on the cusp of retesting its 2021 all-time-high territory after a bullish flag breakout — a genuine trend resumption, not a bounce. **SMH** also improved: MACD turned positive 2026-09-04 and the ETF traded modestly *above* its ~$572.76 50-day MA in Tuesday's session (last $573.83) for the first time in weeks — but this is one session, and today's premarket tape shows broad semis/tech softness (QQQ premarket ~-0.4%), so it has not yet earned the "confirmed reclaim" bar the desk has applied to similar setups (e.g. XLI needed 3 confirming closes in July). Treat as watch-only pending a second confirming close.
- **Catalyst:** XBI's move is catalyst-backed, not just technical — ongoing biotech M&A (>$100B industry-wide in H1 2026, drugmakers refilling pipelines ahead of a ~$300B patent cliff by 2028), a more flexible FDA approval posture since June 2026, and a steady run of positive clinical readouts. This is a structural, multi-month tailwind (industry-wide, dated back to at least June), not a single-day pop — clears the "verify the catalyst is real and directional" bar. Separately, Lockheed Martin was upgraded to Buy at UBS (target $674) on 2026-09-08 — reinforces the held XLI aerospace/defense weighting, not a new-name signal (LMT isn't in `universe.yaml`). No other momentum-watchlist name (AAPL/MSFT/NVDA/AMZN/GOOGL/META/AVGO/AMD/TSLA/COST/LLY/NFLX) turned up a fresh, verified, directional catalyst this morning.
- **Relative-strength rotation:** XLK, XLE, and XLI remain the three clearest sector RS leaders per multiple sources (XLK +33% YTD, XLE +21%, XLI +20%) — all three already held. Recent rotation commentary flags XLI and XLF "recovering/accelerating" and XLK "fading" slightly off its highs — consistent with treating XLK as no-longer-the-clear-standout (matches the premarket flag above) rather than a sell signal. No unheld sector ETF (XLY/XLU/XLRE/XLC) shows a rotation case — quotes this morning (XLY $114.02, XLU $43.45, XLRE $43.90, XLC $111.54) are unremarkable and no source flagged any of the four as gaining relative strength.

## Ranked ideas

| Rank | Symbol | Edge | One-line thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|---|
| 1 | XBI | Momentum/trend + catalyst | Technicals flipped to Strong Buy this week (12/0 MA signals, RSI 66.6, MACD +2.14 and rising) on top of a structural, multi-month biotech catalyst (M&A wave ahead of the 2028 patent cliff, a more flexible FDA posture since June, steady positive trial readouts) — price ~$161.96, within 5% of its 52-week high and approaching 2021-era highs on a bullish flag breakout. Falsifiable: thesis breaks if XBI closes back below its 50-day MA or gives back this week's breakout gains. | ~$162 | 10% | High |
| 2 (watch only, not sized) | SMH | Momentum/trend + catalyst | AI-memory demand (Dell backlog, UBS HBM upgrade, Micron/SanDisk strength) remains real, and SMH traded above its ~$572.76 50-day MA for the first time in weeks on 09-08 with MACD turning positive — but that's one session, and today's premarket semis/tech softness (QQQ ~-0.4%) argues for one more confirming close before sizing, consistent with the desk's past bar for reclaim setups. | n/a — wait for a second confirming close above ~$573 | 10% (if triggered) | Low |

**Recommendation for the open routine:** XBI is the one idea that clears the bar today — a normal ~4% entry (1 of 2 remaining weekly slots) is reasonable if the market opens without a fresh break in XBI's own setup; check price against the ~5% below 52-week-high /50-day-MA levels at the open before sizing, and size to actual settled cash (not margin) per `LESSONS.md` 2026-08-05. Do **not** size SMH today — it needs one more confirming session above its 50-day MA, and today's broad semis premarket weakness makes today a worse-than-average day to test that line. Given the geopolitical risk-off tone and the FOMC hike odds now at 59%, there's no urgency to force a second entry — 1 of 2 remaining weekly slots can comfortably wait for a cleaner SMH setup or a fresh idea.

## Update from the open routine (2026-09-09 09:34 ET)

XBI was priced and dry-run-checked at the open ($161.20, 25 sh / $4,032.50 for a compliant 4% position, risk check passed) but **cash was only $57.40** — a hard lockout, not a discretionary skip. No SPY trim was done to fund it since the core is on target (~60.37%), not above its rebalance band, so there's no sanctioned basis to trim purely to manufacture cash. XBI's thesis is otherwise intact and should be re-checked at midday/EOD if cash frees up (e.g. via a stop-out).

## Notes for the open/midday routines

- Fresh count: 2026-W37, 1/3 slots used (XLK 09-08), 2 remain.
- Watch XLK at the open for its first real test since entry — today's premarket tech/semis softness is a genuine (if mild) headwind; check against its ~$181.7 50-day MA before assuming the golden-cross thesis is untouched.
- XLE (extended winner, tighten blocked) and XLI (recovered, un-cuttable except by its own stop) are unchanged, informational only.
- Oil continues to spike on real, widening Iran-US-Saudi escalation — reinforces the held XLE thesis, doesn't call for new action.
- Fed hike odds for Sept 15-16 FOMC now 59% (up from prior reads) — a genuine headwind for risk assets generally; factor into position-sizing conviction, not just entry price.
- CPI Thu 9/11 and FOMC Wed 9/16 remain real, dated macro catalysts inside the operative window.

## Sources

- [Stock Market Today (Sept. 9, 2026): Nasdaq futures fall as U.S.-Iran tensions boost oil prices — TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-09-2026)
- [Stock Market News Today, 9/8/2026 – Futures Fall on Rising Geopolitical Worries, Oil Prices Climb — TipRanks](https://www.tipranks.com/news/stock-market-news-today-9-8-2026-futures-fall-on-rising-geopolitical-worries-oil-prices-climb)
- [SMH ETF Technical Analysis (50-day MA, MACD) — Investing.com](https://www.investing.com/etfs/holdrs-merrill-lynch-semiconductor-technical)
- [SPDR S&P Biotech ETF (XBI) Technical Analysis — Investtech](https://www.investtech.com/main/market.php?CompanyID=10701494)
- [Here's Why Biotech ETFs Are Rallying Hard — Yahoo Finance](https://finance.yahoo.com/news/heres-why-biotech-etfs-rallying-150000062.html)
- [XBI: Biotech's Breakthrough Moment Happened This Week (Upgrade) — Seeking Alpha](https://seekingalpha.com/article/4938868-xbi-biotechs-breakthrough-moment-happend-this-week-upgrade)
- [Top-Performing Sector SPDRs: XLK, XLE & XLI Top The List — etfdb.com](https://etfdb.com/sector-investing-content-hub/xlk-xle-xli-top-performing-sector-spdrs/)
- [Here Are Tuesday's Top Wall Street Analyst Research Calls (LMT upgrade at UBS) — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/tuesday-top-wall-street-analyst-121528209.html)

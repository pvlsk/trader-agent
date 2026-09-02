# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-09-02 (pre-market)_

**No actionable new entry today — cash is ample ($11,635.87) and 3/3 weekly slots are open, but nothing screened clears the conviction bar.** `risk.py status`: equity **$101,520.73**, day P&L **+0.11%** (loss cap -3% not tripped, no halt), **2026-W36, 0/3 weekly slots used**. A compliant new 5% satellite position needs **$5,076** — cash covers it several times over. The binding constraint remains conviction, not capital.

## Market read (2026-09-02 pre-market)

Market not yet open (`clock`: not `is_open`, checked 08:08 ET, next open 09:30 ET, next close 16:00 ET). Futures are modestly higher into the open: S&P 500 futures +5.65 pts, Dow +40 pts, Nasdaq-100 futures +21.25 pts — a quiet, unremarkable tape after yesterday's broad red session. Today's economic calendar is busy: Challenger job-cut report (7:30 ET), initial jobless claims (8:30 ET), Services PMI (9:45 ET), and ISM non-manufacturing + factory orders (10:00 ET) — any of these could move the tape intraday, none is a stock-specific catalyst. The bigger event is after tonight's close: **AVGO (Broadcom) reports earnings**, with CRM and SNOW also on the calendar — AVGO is on `config/universe.yaml`'s momentum watchlist but the catalyst hasn't happened yet, so it's a watch item for tomorrow's pre-market, not actionable today.

## XLI resolution (carried from EOD 2026-09-01 flag)

Yesterday's EOD routine flagged XLI's last trade ($172.59, 9 min before close) as below its ~$173.6 50-day-MA falsifiable line and asked this routine to confirm against the official close. **Could not independently verify an official closing print via web search** (historical-data pages don't surface the exact number in search results). The best available data point is this morning's pre-market last trade: **XLI $172.75** — essentially flat overnight and still below the ~$173.6 line, consistent with yesterday's reading. One external technical screen (Tickeron) separately describes XLI as "in an upward trend, price above the 50-day moving average" — a conflicting read, possibly stale or using a different MA window. Given two consistent same-day readings (15:51 ET close-proxy and this morning's pre-market) both under the line, **treating the thesis as broken is the more defensible call**, but flagging the source conflict rather than asserting certainty. The position is un-cuttable except by its own live trailing stop regardless (cancel/replace tooling gap, `LESSONS.md` 2026-07-17/23/24) — no action is possible from this routine either way; this is context for the open/midday routines.

## Screened all three edges

- **Momentum/trend:** Rechecked the full `momentum_watchlist` this morning (AAPL $325.25, MSFT $501.19, NVDA $217.43, AMZN $254.88, GOOGL $335.00, META $578.72, AVGO $369.71, AMD $459.74, TSLA $356.08, JPM $354.89, COST $939.86, LLY $1159.75, NFLX $80.81) — none is a fresh, confirmed breakout to new highs against a quiet pre-market tape; no name stood out as newly actionable. **AMD** remains the closest watch: still below the ~$480-490 reclaim line flagged since late August (now $459.74, essentially unchanged from yesterday's $457.73) — falsifiable watch line still unmet. Checked semiconductor-adjacent broad ETF **SMH** for a cleaner group signal: technical reads are bearish (14-day RSI ~35, "Strong Sell," price below its 5/20/50-day EMAs) — the chip-sector weakness that's kept AMD/XLK downgraded is still in force, not resolved.
- **Catalyst:** No fresh, verified, directional catalyst on any universe name this morning. Checked recent analyst upgrades/price-target raises broadly — nothing landed on a name in `config/universe.yaml`. Tonight's AVGO/CRM/SNOW earnings are a real catalyst but haven't happened yet (after-close today) — nothing to act on until tomorrow's reaction is confirmed.
- **Relative-strength rotation:** Rechecked all 11 sector ETFs this morning (XLK $183.67, XLF $57.21, XLE $64.78, XLV $171.66, XLI $172.75, XLY $114.58, XLP $85.27, XLU $42.57, XLB $52.09, XLRE $44.05, XLC $110.88). YTD sector leadership (per external screens): Energy (~+21-45% depending on window), Materials (~+17%), Industrials (~+12%), Staples (~+15%) — three of these four are already held (XLE/XLI/XLP). **Materials (XLB)** is the one YTD leader not currently in the book, so it got a closer look — but its current technicals are weak: 14-day RSI ~37 ("Sell"), MACD negative, "Strong Sell" daily signal, price sitting right at/below its 50-day MA (~$51.06) despite the strong YTD gain (52-week high $54.14, well off current $52.09). The YTD-strength story is real (copper/gold/silver rally on AI-datacenter demand and central-bank buying) but the **near-term trend is not clean** — this fails the momentum/RS entry checklist (confirmed uptrend, not just YTD strength) and is not actionable today. Yesterday's daily sector print: XLE led (+1.27%), XLY lagged (-1.72%) — consistent with the existing book, no rotation signal to act on.

## Ranked ideas

**No actionable candidate today.** Two names remain on watch-only status, listed for visibility — not sized, not queued against a weekly slot:

| Symbol | Edge | One-line thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|
| AMD | Momentum/trend + catalyst | Still below the ~$480-490 reclaim line ($459.74 now, essentially flat vs. yesterday) and well off its 52-week high; the Raymond James Strong Buy catalyst is real but the falsifiable technical line hasn't cleared. Broader semiconductor group (SMH) is technically weak right now (RSI ~35, Strong Sell), reinforcing caution. | Wait for a confirmed reclaim above ~$480-490 | 10% | Low |
| XLB (Materials) | Relative-strength rotation | YTD sector leader (~+17%) on a genuine structural story (copper/gold/silver rally, AI-datacenter and electrification demand) not currently expressed in the book — but near-term technicals are weak (RSI ~37, price at/below its 50-day MA, off its 52-week high) — fails the "confirmed uptrend" bar today. | Wait for a reclaim of the 50-day MA (~$51) with improving RSI | 10% | Low |

**Best move is to do nothing** on the idea-generation side today. Cash and weekly slots are both ample, but forcing either watch-list name in before its technical setup confirms would violate the discipline rule (a thesis or no trade). Both are worth a fresh look tomorrow.

## Notes for the open routine

- **Cash ($11,635.87) and slots (0/3) are both ample — the desk has full capacity to act, but nothing cleared the bar this morning.** Don't force a trade just because capacity exists.
- **XLI: two consistent readings (yesterday's near-close $172.59, this morning's pre-market $172.75) sit below the ~$173.6 50-day-MA falsifiable line, though one external technical screen conflicts (reads XLI as above its 50-day MA).** Treating the thesis as likely broken is the more defensible read given the two consistent internal data points, but flagging the source conflict. No discretionary action is possible regardless (cancel/replace tooling gap) — only its own trailing stop can close it. Worth the open/midday routine re-checking a live quote against $173.6 once the market opens for a cleaner, real-time read.
- **AVGO reports earnings after tonight's close** — CRM and SNOW also report. Not actionable today; flag for tomorrow's pre-market read.
- **Core SPY:** `risk.py status` didn't break out exact core %; per yesterday's EOD it was ≈60.1%, essentially on target — no trim expected to be needed, but worth a quick confirm once the market opens and `portfolio.py` is available.
- **XLE (held) remains the standing extended-winner tighten candidate** (+13%+ since entry) — retightening still blocked by the cancel/replace tooling gap (`memory/LESSONS.md` 2026-07-24, unresolved for 6+ consecutive weekly reviews).
- **Materials (XLB) is now on watch** as the one YTD sector leader not in the book — currently disqualified by weak near-term technicals (RSI ~37, below 50-day MA), reassess if it reclaims the MA with improving RSI.

## Sources

- [State Street Industrial Select Sector SPDR ETF (XLI) — Yahoo Finance](https://finance.yahoo.com/quote/XLI/)
- [Materials Select Sector SPDR ETF Technical Analysis — Investing.com](https://www.investing.com/etfs/spdr-materials-select-sector-etf-technical)
- [VanEck Semiconductor ETF (SMH) Technical Analysis — TradingView](https://www.tradingview.com/symbols/NASDAQ-SMH/technicals/)
- [Copper surges in 'unsustainable' rally, joining silver and gold in 2026 metals frenzy — Yahoo Finance](https://finance.yahoo.com/news/copper-surges-in-unsustainable-rally-joining-silver-and-gold-in-2026-metals-frenzy-144259758.html)
- [Sector Performance: All 11 GICS Sector ETFs vs SPY — thetrading.tools](https://www.thetrading.tools/sector-performance)
- [XLI in upward trend: price rose above 50-day moving average — Tickeron](https://tickeron.com/ticker/XLI/)

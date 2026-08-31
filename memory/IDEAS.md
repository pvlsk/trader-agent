# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-08-31 (pre-market)_

**No actionable idea today — cash-blocked (26 straight calendar days flat) and nothing screened clears the bar on conviction either.** `portfolio.py`/`risk.py status`: equity **$102,105.85**, day P&L -0.16% (loss cap -3% not tripped, no halt), cash **$1,699.14** (unchanged since 2026-08-05 = **26 calendar days**). A compliant new 5% satellite position needs **$5,105** — cash is well short (per LESSONS 2026-08-05, only settled cash counts, not `buying_power`/margin; even the LESSONS 2026-08-21 "smaller cash-sized entry" option tops out at ~1.66% of equity here, and no idea below is strong enough to justify forcing even that). `risk.py status`: **2026-W36, 0/3 weekly slots used** (fresh week), moot until cash frees up.

## Market read (2026-08-31 pre-market)

Market not yet open at read time (`clock`: not `is_open`, next open 09:30 ET today, next close 16:00 ET). The weekend's dominant, live catalyst is a fresh **US-Iran military escalation**: US forces struck Iranian rocket launchers/positions near the Strait of Hormuz on Sunday, Iran retaliated, and oil jumped on the open of futures trading — Brent +3.5% to ~$91.20/bbl, WTI +3.5% to ~$86.30/bbl ([CNBC](https://www.cnbc.com/2026/08/30/stock-market-today-live-updates.html), [TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-31-2026)). Energy names are broadly higher pre-market (CVX +1.7%, XOM +1.5%, OXY +1.8%, COP +1.3%, HAL +2.5%, SLB +1.7%) ([Yahoo Finance](https://ca.finance.yahoo.com/news/energy-stocks-rally-fresh-u-093550675.html)). This directly **extends, not creates** the desk's existing XLE thesis (already held, +11.7% since entry, already at a full satellite slot) — not a new-entry opportunity. Equity futures are soft-to-lower on the same headline, compounding Friday's hawkish Warsh Jackson Hole remarks; short-term government borrowing costs are at multi-year highs on renewed inflation fear ([CNBC](https://www.cnbc.com/2026/08/30/stock-market-today-live-updates.html)) — a headwind for rate-sensitive sleeves (utilities, REITs, small caps) that argues against chasing there today.

Separately, the semiconductor-tariff overhang flagged in Friday's (2026-08-28) pre-market read is still live and unresolved: the White House is reportedly still weighing new chip tariffs (extending to laptops/servers/gaming hardware), with Commerce Secretary Lutnick floating investment-linked relief rather than a resolution ([CNBC](https://www.cnbc.com/2026/08/27/trump-semiconductor-tech-tariffs.html), [TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262136441-semiconductor-tariff-trump-memory-micron-nvidia-ai-data-center-tradingkey)). XLK's headline YTD strength (+33%, sector-leading) is undercut by this same live risk to its ~40% NVDA/AAPL/MSFT-adjacent concentration — no change from Friday's downgrade, not carried forward as an idea.

## Screened all three edges

- **Momentum/trend:** AMD carries the one real fresh catalyst in the universe (Raymond James upgraded to Strong Buy on 2026-08-25, PT raised to $641 from $565, ~40% implied upside) ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/top-analyst-resets-amd-stock-213300157.html)), but the technical picture is mixed, not a clean momentum setup: shares are ~5% off the 52-week high ($584.73) and down ~8% over the past month even while trading above their 20/50-day EMAs, with short-term trend flagged negative by at least one source ([StockAnalysis.com/TipRanks via search](https://www.tipranks.com/stocks/amd/technical-analysis)). Not "near 52-week highs" as the momentum edge requires — watch, don't chase yet. No other momentum-watchlist name broke to fresh highs overnight.
- **Catalyst:** The Iran/Hormuz escalation is real, verified, and directional, but it reinforces a position already held at full size (XLE) rather than opening a new one. No other universe name has a fresh, verified, directional catalyst this morning; the AGCO/DE/KALU/XP/Baozun/Evolution Petroleum/Moderna upgrades reported over the weekend are all outside `config/universe.yaml`.
- **Relative-strength rotation:** No sector currently outside the held book (XLV/XLF/XLI/XLE/XLP) shows a clean, fresh RS breakout. XLK's index-weight dominance and YTD return remain undercut by the live tariff risk above (unchanged from Friday). XLU/XLRE face a rising-yield headwind from the hawkish Warsh read plus fresh inflation fear from the Iran escalation — a reason to avoid, not rotate in. XLB/XLC/XLY show no distinguishing catalyst or RS signal today.

## Ranked ideas

**No actionable candidate today.** One name is worth tracking for a cleaner setup, listed for visibility only — not sized, not queued against a weekly slot, and cash-blocked regardless:

| Symbol | Edge | One-line thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|
| AMD | Momentum/trend + catalyst | Raymond James Strong Buy upgrade (2026-08-25, PT $641 from $565) is a real, verified catalyst, but price is ~5% off the 52-week high and down ~8% over the past month — falsifiable watch line: only actionable if AMD reclaims a fresh high or the short-term trend turns clearly positive, not on the catalyst alone. | Wait for confirmation above recent swing high (~$480-490) before considering | 10% | Low |

**Best move is to do nothing** on the idea-generation side today, independent of the cash block: the dominant catalyst (Iran/Hormuz) only reinforces an already-held, already-maxed position; the tariff overhang keeps tech/semis conviction low; and AMD's catalyst isn't yet confirmed by price action.

## Notes for the open routine

- **No actionable new entry today** — cash ($1,699.14, 26 straight calendar days flat) remains the binding constraint, and this morning's screen doesn't produce an idea worth queuing behind it either. Reconcile positions/stops only; market opens regularly at 09:30 ET.
- **Live catalyst: fresh US-Iran escalation near the Strait of Hormuz (weekend strikes + retaliation), oil +3.5%.** Directly extends the held XLE thesis (+11.7%, already full-size) — nothing to add there, but expect elevated volatility across the book at the open, and energy-adjacent XLI (defense/aerospace weighting) may also react.
- **Core SPY is now at ~69.9% of equity** (`$71,394 / $102,105.85`) against the **new 60% target / 50-70% band** (`config/risk.yaml`, tilted down from 70% on 2026-08-28) — sitting at the very top of the band. Not a breach, but worth the open/midday routine checking whether a trim toward 60% is warranted per `config/strategy.md`'s rebalance rule (this routine does not change positions).
- **Semiconductor-tariff risk is still unresolved** (Lutnick floating investment-linked relief, no resolution reported) — XLK stays downgraded/not carried forward, unchanged from 2026-08-28.
- **AMD is a watch-only name** — real analyst catalyst (Raymond James Strong Buy, PT $641) but ~5% off its 52-week high and short-term-trend-mixed; reassess if it breaks to a fresh high.
- **Cash lockout is now 26 straight calendar days** (since 2026-08-05); the 2026-08-21 operator escalation on a minimum-size floor / cash-sized-entry policy remains open in memory — see `memory/LESSONS.md` and the Friday weekly review cadence for status.
- **XLE (held) remains the standing extended-winner tighten candidate** at +11.7% since entry — retightening still blocked by the cancel/replace tooling gap (`memory/LESSONS.md` 2026-07-24, unresolved for 6+ consecutive weekly reviews).

## Sources

- [Stock Market Today (Aug. 31, 2026): Dow futures fall on escalation of U.S.-Iran conflict — TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-31-2026)
- [Stock market today live updates — CNBC](https://www.cnbc.com/2026/08/30/stock-market-today-live-updates.html)
- [Energy stocks rally as fresh U.S.-Iran attacks drive oil prices higher — Yahoo Finance](https://ca.finance.yahoo.com/news/energy-stocks-rally-fresh-u-093550675.html)
- [Top analyst resets AMD stock price target for rest of 2026 — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/top-analyst-resets-amd-stock-213300157.html)
- [AMD Technical Analysis — TipRanks](https://www.tipranks.com/stocks/amd/technical-analysis)
- [U.S. considers fresh round of tariffs on semiconductors, report says — CNBC](https://www.cnbc.com/2026/08/27/trump-semiconductor-tech-tariffs.html)
- [Memory Stocks Reverse Early Gains, Micron Drops 3% as Trump Administration Plans New Semiconductor Tariffs — TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262136441-semiconductor-tariff-trump-memory-micron-nvidia-ai-data-center-tradingkey)
- [Here Are Monday's Top Wall Street Analyst Research Calls — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/monday-top-wall-street-analyst-115622968.html)

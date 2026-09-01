# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-09-01 (pre-market)_

**No actionable new entry today — cash is finally available (first time in ~27 days) but nothing screened clears the conviction bar.** `portfolio.py`/`risk.py status`: equity **$101,630.71**, day P&L -0.34% (loss cap -3% not tripped, no halt), cash **$7,062.99** (freed by the 2026-08-31 SPY trim, now the next session — treat as fully settled per LESSONS 2026-08-05 T+1 guidance). A compliant new 5% satellite position needs **$5,082** — cash comfortably covers it for the first time since 2026-08-05. `risk.py status`: **2026-W36, 0/3 weekly slots used**. The binding constraint has flipped from cash to conviction: everything on today's screen is either already held, unconfirmed, or extended into a weak tape — see below.

## Market read (2026-09-01 pre-market)

Market not yet open (`clock`: not `is_open`, next open 09:30 ET today, next close 16:00 ET). Futures are broadly red: S&P 500 -0.5%, Nasdaq-100 -0.9-1%, Dow -0.5%, Russell 2000 -0.5% ([Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-tuesday-september-1-dow-sp-500-nasdaq-080617884.html), [TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-1-2026)). Two compounding headwinds: (1) the US-Iran conflict in the Strait of Hormuz escalated further over the weekend into Monday, keeping Brent near $90/bbl; (2) the 10-year Treasury yield has pushed up to 4.75% on renewed inflation and Fed rate-hike fears ([Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-tuesday-september-1-dow-sp-500-nasdaq-080617884.html)). This is a genuine risk-off tape, not a stock-specific rotation — a day to be more conservative about chasing anything extended, not less.

Energy continues to be the direct, verified beneficiary of the Iran/Hormuz catalyst — but XLE is already held at a full ~4.5% slot (now **+13.3%** since entry, the book's best performer and standing extended-winner tighten candidate), so this is reinforcement of an existing thesis, not a new-entry opportunity.

The semiconductor-tariff overhang has escalated, not resolved: reporting this week describes a "Phase 2" round of chip tariffs landing while a fab tax-credit deadline leaves the industry "frozen," with Commerce Secretary Lutnick's investment-linked exemption framework still the only relief mechanism on the table and South Korean/Taiwanese chipmakers without US investment commitments facing tariffs up to 100% ([TechTimes](https://www.techtimes.com/articles/325977/20260831/chip-tariff-phase-2-lands-fab-tax-credit-deadline-leaves-industry-frozen.htm), [CNBC](https://www.cnbc.com/2026/08/27/trump-semiconductor-tech-tariffs.html)). XLK/SMH stay downgraded, unchanged from 2026-08-28.

Gold has had a big run — GLD-tracked spot gold gained ~9.6% in August, its best month since January, on safe-haven demand ([Sunday Guardian](https://sundayguardianlive.com/business/gold-price-prediction-september-2026-will-gold-surge-or-crash-gold-gains-96-in-august-as-fed-rate-hike-odds-hit-64-can-gold-reclaim-165-lakh-274238/)). But the catalyst usually cited (Moody's stripping the US of its last AAA rating) happened back in May 2026 — it's stale, not fresh. Today's setup is mixed: rising rate-hike odds are fighting safe-haven flows, and at least one near-term forecast calls for gold to soften today ([FXStreet](https://www.fxstreet.com/analysis/record-gold-rally-fueled-by-safe-haven-buying-202509022100), [LiteFinance](https://www.litefinance.org/blog/analysts-opinions/gold-price-prediction-forecast/daily-and-weekly/)). Chasing GLD here would mean buying into an already-extended move on the day forecasts turn cautious — watch, don't chase.

## Screened all three edges

- **Momentum/trend:** AMD is still the one name with a real analyst catalyst in memory (Raymond James Strong Buy, PT $641, flagged 2026-08-25), but at $470.66 it remains below the ~$480-490 reclaim line set in prior pre-market reads and well off its $584.73 52-week high — the falsifiable watch condition ("reclaim a fresh high or a clearly positive short-term trend") is still not met. No other momentum-watchlist name is breaking to fresh highs against a broadly red pre-market tape.
- **Catalyst:** Today's only real, verified, directional catalyst affecting the universe is the Iran/Hormuz oil shock, and it only reinforces the already-full-size XLE position. No universe name has a fresh earnings beat, guidance raise, or confirmed upgrade this morning (today's actual upgrades — Akamai, Duolingo — are outside `config/universe.yaml`).
- **Relative-strength rotation:** External RS screens flag Industrials (XLI) as carrying the strongest institutional buying-pressure reading with a fully aligned up-trend, and Financials (XLF) improving with bullish trend support ([Stockcheatsheets](https://stockcheatsheets.substack.com/p/our-latest-us-sector-and-index-etf)) — but both are already held at full satellite size, so this is confirmation, not a new idea. XLI itself is currently the book's only red name (-4.4%), so the external RS read is a useful data point for the open/midday routine assessing whether XLI's pullback is noise or a real reversal, not an entry signal. Health Care Equipment (XHE) is flagged as the top external leader, but XHE is a subsector ETF outside `config/universe.yaml` (only broad XLV is in-universe, already held) — not pursued without a stronger, explicit justification for widening the universe. No sector outside the held book shows a clean, fresh breakout.

## Ranked ideas

**No actionable candidate today.** Two names are worth tracking for a cleaner setup, listed for visibility only — not sized, not queued against a weekly slot:

| Symbol | Edge | One-line thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|
| AMD | Momentum/trend + catalyst | Raymond James Strong Buy (PT $641) remains a real catalyst, but price ($470.66) is still below the ~$480-490 reclaim line and well off the $584.73 52-week high — falsifiable watch line unchanged: only actionable on a fresh high or clearly positive short-term trend, not the catalyst alone, and today's risk-off tape makes a breakout less likely. | Wait for reclaim above ~$480-490 | 10% | Low |
| GLD | Momentum/trend (catalyst stale) | Gold +9.6% in August on safe-haven demand, but the cited catalyst (Moody's downgrade) is 3.5 months old, near-term forecasts are mixed-to-soft for today, and the move is already extended — falsifiable watch line: only actionable on a clean pullback-and-hold at a defined support level, not by chasing the extension. | Wait for a pullback/consolidation, not a chase entry | 10% | Low |

**Best move is to do nothing** on the idea-generation side today. Cash is available for the first time in almost a month, which is a real change — but the tape is risk-off (Iran escalation + 10yr at 4.75%), the one existing catalyst (oil/XLE) is already fully expressed, and neither watch-list name has confirmed its setup. Forcing a trade now to "use" the freed cash would violate the discipline rule (a thesis or no trade) — better to wait for AMD or GLD (or a fresh idea) to actually confirm.

## Notes for the open routine

- **Cash is now fully available for a compliant 5% entry ($7,062.99 vs. $5,082 needed)** — the first time since 2026-08-05. No idea here meets the conviction bar to use it today; don't force a trade just because capacity finally exists.
- **Risk-off tape at the open:** Iran/Hormuz escalation (oil elevated, futures broadly red) + 10-year yield at 4.75% on inflation/rate-hike fears. Expect volatility; XLE (+13.3%, held, full-size) is the direct beneficiary, already maxed — nothing to add. XLI's own strong external RS read is a data point (see above) for whether its -4.4% pullback is noise, not an entry/exit signal by itself.
- **Core SPY is now ~64.6% of equity** (`$65,592 / $101,630.71`) — still above the 60% target but within the 50-70% band; the 2026-08-31 trim already took one step down. Per the standing note carried since 2026-08-31, worth the open/midday routine weighing another gradual trim toward 60%, at the open rather than intraday.
- **Semiconductor-tariff risk has escalated ("Phase 2" landing, industry described as frozen on fab tax-credit uncertainty) — XLK/SMH stay downgraded, unchanged stance.**
- **AMD watch-only:** still below its ~$480-490 reclaim line ($470.66 now); reassess if it breaks to a fresh high.
- **GLD watch-only (new):** +9.6% in August, cited catalyst (Moody's downgrade) is stale (May 2026), near-term forecasts mixed/soft for today — don't chase the extension; watch for a clean pullback/consolidation instead.
- **XLE (held) remains the standing extended-winner tighten candidate** at +13.3% since entry — retightening still blocked by the cancel/replace tooling gap (`memory/LESSONS.md` 2026-07-24, unresolved for 6+ consecutive weekly reviews).

## Sources

- [Stock market today: Dow, S&P 500, Nasdaq futures fall as inflation, Fed rate-hike fears persist — Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-tuesday-september-1-dow-sp-500-nasdaq-080617884.html)
- [Stock Market Today (Sept. 1, 2026): Dow futures slide on renewed U.S.-Iran conflict — TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-1-2026)
- [Our Latest US Sector & Index ETF Relative Strength Rank & Trend Report: Industrials Lead as Tech Momentum Cools — Stockcheatsheets](https://stockcheatsheets.substack.com/p/our-latest-us-sector-and-index-etf)
- [Chip Tariff Phase 2 Lands as Fab Tax Credit Deadline Leaves Industry Frozen — TechTimes](https://www.techtimes.com/articles/325977/20260831/chip-tariff-phase-2-lands-fab-tax-credit-deadline-leaves-industry-frozen.htm)
- [U.S. considers fresh round of tariffs on semiconductors, report says — CNBC](https://www.cnbc.com/2026/08/27/trump-semiconductor-tech-tariffs.html)
- [Gold Price Prediction September 2026 — Sunday Guardian](https://sundayguardianlive.com/business/gold-price-prediction-september-2026-will-gold-surge-or-crash-gold-gains-96-in-august-as-fed-rate-hike-odds-hit-64-can-gold-reclaim-165-lakh-274238/)
- [Record gold rally fueled by safe-haven buying — FXStreet](https://www.fxstreet.com/analysis/record-gold-rally-fueled-by-safe-haven-buying-202509022100)
- [Moody's Just Downgraded the United States' Pristine Credit Rating — Yahoo Finance](https://finance.yahoo.com/news/moodys-just-downgraded-united-states-070600125.html)

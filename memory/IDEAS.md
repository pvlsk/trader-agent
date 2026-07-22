# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-07-22 (pre-market)_

**0 actionable ideas today — 0 of 3 weekly satellite slots remain.** `counters.json`: `week_of 2026-W30`, `new_positions_this_week: 3` (V + IWM opened 2026-07-20, AMD opened 2026-07-21) — the cap is fully used and no new satellite entry is possible for the rest of this ISO week regardless of setup quality. The next 3 slots open Monday **2026-07-27** (2026-W31). Loss cap not tripped (day P&L -0.37%, equity $99,815.75, per `risk.py status`). Market currently closed (`clock`: next open 09:30 ET today, normal Wednesday session).

## Market read (2026-07-22 pre-market)

Futures are modestly lower (S&P -0.2%, Nasdaq-100 -0.5%, Dow -0.05%, Russell 2000 -0.26%) as the market looks ahead to GOOGL and TSLA earnings after today's close (pure event risk for our universe — GOOGL is not held, TSLA is explicitly excluded from the tradable universe). The dominant driver is oil: Brent is up ~3.5-4% to ~$94 and WTI ~$87.56 after the 11th consecutive night of US strikes on Iran, with Secretary of State Rubio saying Iran is "not serious" about peace talks — the opposite of Monday's ceasefire-mediation hope, and a real escalation, not a one-day pop. This directly reinforces our existing **XLE** (energy) and **XLI** (defense/aerospace-weighted industrials) theses further. Intel fell ~2.9% pre-market (not in our universe); Supermicro gained on a record order backlog. ([Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-wednesday-july-22-dow-sp-500-nasdaq-alphabet-tesla-083644887.html), [Benzinga](https://www.benzinga.com/markets/prediction-markets/26/07/60599715/sp500-july-22-open-up-or-down-polymarket-oil-fed-earnings-ai-stocks), [CNBC](https://www.cnbc.com/2026/07/22/oil-prices-iran-war-macro-rubio-brent-wti.html))

**XLK carryover — thesis reclaim now confirmed and strengthening, watch stood down.** XLK was flagged broken since 2026-07-17 (close below its tracked ~$178.6 50-day MA), then flagged as reclaimed intraday on 2026-07-21 ($179.15-$180.47). That reclaim now has two full sessions of confirmation behind it: XLK was Benzinga's leading sector gainer both 2026-07-20 (+1.04%) and 2026-07-21 (+1.80%), and this morning's quote reads **$180.71** — comfortably ~1.2% above the $178.6 line, not a fleeting tick. Recommend the next routine formally close out this watch in `memory/STATE.md` (no further flagging needed absent a new break). ([Leading/Lagging Sectors July 21 — Benzinga](https://www.benzinga.com/etfs/sector-etfs/26/07/60576108/leading-and-lagging-sectors-july-21-2026))

**AMD's "Advancing AI 2026" catalyst is now live, not just forward-looking.** The event opened today (July 22) at Moscone Center with real product announcements — EPYC "Venice" (first x86 server CPU on TSMC's 2nm process), the Helios rack (31TB HBM4), and the MI455X accelerator roadmap for H2 2026 deployment; Su's keynote is tomorrow (July 23, 9:30am PT). AMD quote this morning is **$544.37**, well above our $526.60 entry (+3.4%) and above the ~$500 50-day-MA falsifiable line — thesis intact and strengthening. No action needed (already held, no slot available to add regardless). ([TechTimes](https://www.techtimes.com/articles/321257/20260722/amd-advancing-ai-2026-opens-zen-6-venice-helios-open-ai-rack-bet.htm))

Re-screened the six unheld sector ETFs for a Monday-2026-W31 watch list: no clean confirmed-uptrend candidate stands out today. **XLRE** remains mixed (real estate/data-center-REIT tailwind still cited, but technical momentum indicators turned negative July 8 and the sector remains rate-sensitive event risk into the next Fed decision) — stays on watch, not upgraded. XLU/XLC/XLY/XLP/XLB: no fresh catalyst or technical change since 2026-07-21's pass. **NVDA** continues to lag its own sector badly (+3.2% YTD vs. AMD's +171% and MU's +305%) — not a confirmed-trend candidate. Given slots don't reopen until Monday and four trading days remain before then, a fresh screen at Monday's own pre-market will be more useful than locking in a stale idea now.

## Ranked ideas

**None actionable today — 0 of 3 weekly slots remain.** Per the desk's discipline, doing nothing is the correct default when the cap is exhausted; no idea below is to be acted on until 2026-W31 opens Monday 2026-07-27, at which point re-verify everything fresh (conditions can shift over the intervening four sessions).

## Watch list (queued for 2026-W31, not actionable today)
- **XLRE (real estate):** Data-center-REIT / AI-infrastructure tailwind still cited by multiple sources, but momentum indicators turned negative 2026-07-08 and the sector carries real rate-decision event risk. Re-verify fresh Monday, don't carry this stale read forward as a plan.
- **XLU / XLC / XLY / XLP / XLB:** No fresh confirming technical or catalyst evidence today; same reasons to pass as 2026-07-21.
- **NVDA:** Still the sector's laggard (+3.2% YTD) despite the broader chip-complex strength — not a confirmed uptrend.
- **GOOGL / TSLA:** Report after today's close — pure event risk; GOOGL is outside the universe's momentum watchlist and TSLA earnings are a headline risk only, not traded ahead of the print regardless.

## Notes
- Existing satellites, no changes recommended (pre-market does not trade): no fresh news found breaking the XLV, XLF, XLI, or XLE theses. The renewed oil surge and confirmed Iran-conflict escalation (11th straight night of strikes, diplomacy stalled per Rubio) is incremental reinforcement for both XLE and XLI's defense/aerospace weighting — worth noting as a positive, not a break.
- **XLK carryover watch can be stood down** — see above; two full sessions of confirmed reclaim and sector leadership since the 2026-07-17 break.
- **The `scripts/alpaca.py` cancel/replace-order tooling gap remains open and unresolved** (documented since 2026-07-14, reconfirmed every session since) — `scripts/alpaca.py sell/stop` still cannot act on a position once its trailing stop is live and holding the shares as sell-side inventory. Standing engineering priority, not relevant to any action this routine (no cut was contemplated).
- **0 of 3 weekly satellite slots remain for 2026-W30** — no new entry is possible today or any day this week regardless of idea quality; next slots open Monday 2026-07-27 (2026-W31).

## Sources
- [Stock market today: Dow, S&P 500, Nasdaq futures slide with Alphabet, Tesla earnings on deck — Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-wednesday-july-22-dow-sp-500-nasdaq-alphabet-tesla-083644887.html)
- [Stock Market: Will S&P 500 Open Up or Down Today? — Benzinga](https://www.benzinga.com/markets/prediction-markets/26/07/60599715/sp500-july-22-open-up-or-down-polymarket-oil-fed-earnings-ai-stocks)
- [Oil prices jump 4% as Rubio says Iran "not serious" about peace talks — CNBC](https://www.cnbc.com/2026/07/22/oil-prices-iran-war-macro-rubio-brent-wti.html)
- [Leading And Lagging Sectors For July 21, 2026 — Benzinga](https://www.benzinga.com/etfs/sector-etfs/26/07/60576108/leading-and-lagging-sectors-july-21-2026)
- [AMD Advancing AI 2026 Opens With Zen 6 Venice, Helios, and Open AI Rack Bet — Tech Times](https://www.techtimes.com/articles/321257/20260722/amd-advancing-ai-2026-opens-zen-6-venice-helios-open-ai-rack-bet.htm)
- [These Are the Stocks Reporting Earnings Today – July 22, 2026 — TipRanks](https://www.tipranks.com/news/these-are-the-stocks-reporting-earnings-today-july-22-2026)

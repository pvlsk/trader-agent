# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-09-08 (pre-market, Tuesday) — market closed, checked 08:08 ET, next open 09:30 ET._

**One actionable idea this week, two watch-only.** `risk.py status`: equity **$101,856-101,868**, day P&L -0.27% to -0.28% (loss cap -3% not tripped), **2026-W37, 0/3 weekly slots used** (fresh week, all 3 available). Cash **$3,635.87**.

## Market read (2026-09-08 pre-market)

Risk-off open brewing: **U.S. and Iran traded strikes over the weekend** (US hit three Iranian oil tankers Saturday after Iran launched missiles at two Navy warships; Saudi Aramco facilities reportedly hit Sunday), sending Brent/WTI to ~6-week highs (Brent ~$97-99, WTI ~$93-95) for a third straight day. Dow futures are down sharply this morning (~-0.7% to -0.9%) while **S&P futures are down a more modest ~0.25% and Nasdaq futures are roughly flat to slightly positive** — a continuation of the divergence flagged Friday, where tech/growth is holding up better than the broader blue-chip tape. Separately, **Novartis reported two failed drug studies pre-market**, hitting pharma names (AMGN, LLY, IONS, DYN, SRPT all down) — none of these are held directly, but **LLY is a top XLV holding**, so the held XLV satellite may see read-through weakness at the open despite its broader healthcare-sector RS thesis being otherwise intact (see Notes for the open/midday routine). CPI prints Thursday 2026-09-11 and the FOMC decision lands Wednesday 2026-09-16 — both still real, dated vol events inside this week's window.

## Held-position status (carried forward, informational only — no action, not a trade recommendation)

- **XLE (+13.5% since entry):** the oil-price spike from the Iran conflict is a tailwind reinforcing the existing thesis, not a new signal. Remains the standing extended-winner tighten candidate, still blocked by the `scripts/alpaca.py` cancel/replace gap (`LESSONS.md` 2026-07-24 and multiple follow-ups) — not re-attempted here (research routine doesn't trade).
- **XLI (-3.9%):** thesis recovered as of 2026-09-03 close and has held above its ~$173.6 50-day MA every session since — durable at this point. Still un-cuttable except by its own stop.
- **XLV:** watch for pre-market weakness tied to the Novartis-driven pharma selloff (LLY is a top XLV constituent) — not yet a thesis break, just a flag for the open/midday routine to check price action against the sector's own 50-day MA before assuming business as usual.

## Screened all three edges

- **Momentum/trend:** **XLK remains the clear standout.** Confirmed golden cross intact — price $187.30 vs. 50-day MA ~$181.7 and 200-day MA ~$160 — and only ~3% above its 50-day support, not overextended. One caution flag: XLK's MACD histogram turned negative 2026-08-21 (a deceleration signal), but price structure hasn't broken down. **XBI** technicals have weakened since last week's read: still ~4% off its 52-week high after a ~26% trailing-quarter run, but now showing a weak close and an "aggressive pullback into the daily 50" right at major resistance, plus an Aroon indicator that's been in a downtrend since 2026-08-12 — these are rollover warning signs, not a confirmed breakdown, but they raise the pullback-risk bar further versus last week. **SMH / memory-chip complex** — the AI-demand catalyst (Dell's $95B backlog, UBS's HBM upgrade, Micron/SanDisk still grinding higher a second/third session, +2-3% each most recently) is real and persisting, but **SMH itself is still trading below both its 50-day (~$572.76) and 200-day (~$607.52) MA** — the broader semiconductor basket (weighed down by non-memory names) has not confirmed the memory-specific strength. This is a structural disqualifier for a momentum entry today, not just "one session too early."
- **Catalyst:** Memory-AI-demand catalyst (see above) is verified and dated but not yet reflected in SMH's own trend structure — stays watch-only. Novartis's failed trials are a real, dated catalyst but it's negative (avoid LLY-adjacent names, not a buy signal). No other momentum-watchlist name has a fresh, unambiguous catalyst.
- **Relative-strength rotation:** XLK and XLE (held) remain the two clearest sector RS leaders. XLI (held) has recovered. XLV (held) is a distant third. No unheld sector ETF (XLY/XLU/XLRE/XLC) shows a rotation case — all meaningfully negative RS vs SPY, unchanged from last week's read.

## Ranked ideas

| Rank | Symbol | Edge | One-line thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|---|
| 1 | XLK | Relative-strength rotation + momentum/trend | XLK's golden cross remains intact — price $187.30 above both its 50-day (~$181.7) and 200-day (~$160) MAs, only ~3% above support, with tech/growth again showing relative resilience vs. the broader tape this morning despite Mideast-driven risk-off. Falsifiable: thesis breaks if XLK closes back below its 50-day MA or gives back sector RS leadership. | ~$187 | 10% | High |
| 2 (watch only, not sized) | XBI | Momentum/trend | Still within ~4% of its 52-week high, but a weak close and a multi-week Aroon downtrend right at resistance are fresh rollover warning signs since last week's read — the risk/reward has worsened, not improved. Needs a clean reclaim of new highs (not just proximity) before sizing. | n/a — wait for confirmation | 10% (if triggered) | Low |
| 3 (watch only, not sized) | SMH (memory-chip complex) | Catalyst | AI-memory demand (Dell backlog, UBS HBM upgrade, Micron/SanDisk still grinding higher) is real and persisting, but SMH itself trades below both its 50-day and 200-day MA — the catalyst hasn't yet repaired the broader basket's trend structure. Wait for a close back above the 50-day MA (~$573) before treating this as actionable. | n/a — wait for MA reclaim | 10% (if triggered) | Low |

**Recommendation for the open routine:** XLK is the only idea that clears the bar today — a normal ~3.5-4% entry (1 of 3 weekly slots) is reasonable; size to actual settled cash at execution (cash on hand is $3,635.87, a touch under a full 4% ($4,075) at $187.30/sh, so ~19-21 sh depending on cash available at execution, per the settled-cash rule in `LESSONS.md` 2026-08-05 — don't reach for margin). Do **not** size XBI or SMH today — both need their stated technical conditions to actually improve first, not just "one more session." Given this morning's Iran/oil-driven risk-off tone in the broader tape (even though tech futures are holding up), there's no urgency to force a second or third entry this week — 2 of 3 weekly slots can comfortably wait for a cleaner setup.

## Notes for the open/midday routines

- Fresh ISO week 2026-W37, 0/3 slots used, cash $3,635.87.
- Watch XLV at the open for read-through weakness from the Novartis-driven pharma selloff (LLY is a top constituent) — not a thesis break yet, just a flag to check against XLV's own 50-day MA rather than assuming Friday's healthy read still holds.
- XLE (+13.5%, tighten blocked) and XLI (recovered, un-cuttable except by its own stop) are unchanged, informational only.
- Oil is spiking on real Iran-US escalation (Brent/WTI at ~6-week highs) — reinforces the held XLE thesis, doesn't call for new action.
- CPI Thu 9/11 and FOMC Wed 9/16 remain real, dated macro catalysts inside the operative window.
- Since-inception alpha widened again to **-1.39%** (from -1.13% Friday, -1.08% midday Thursday) — the fourth straight reading in the same direction per the trend `LESSONS.md` flagged 2026-09-04; worth another explicit mention at Friday's weekly review rather than only in the performance section.

## Sources

- [Oil prices rise to 6-week high after Iran and U.S. trade blows, Saudi Aramco facilities reportedly hit — CNBC](https://www.cnbc.com/2026/09/07/oil-prices-rise-to-6-week-high-after-iran-and-us-trade-blows-saudi-aramco-facilities-reportedly-hit.html)
- [U.S-Iran strikes send oil, yields surging as Fed turns hawkish — CNBC](https://www.cnbc.com/2026/09/02/us-iran-trump-war-escalation-latest-fed-rate-g20-bessent-yen-.html)
- [Stock Market Today (Sept. 8, 2026): Dow futures edge lower as oil prices climb, Mideast tensions rise — TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-08-2026)
- [XLK technical analysis (50/200-day MAs, MACD) — AltIndex](https://altindex.com/ticker/xlk/technical-analysis)
- [Top-Performing Sector SPDRs: XLK, XLE & XLI Top The List — etfdb.com](https://etfdb.com/sector-investing-content-hub/xlk-xle-xli-top-performing-sector-spdrs/)
- [XBI technical setup / pullback risk near 52-week high — TradingView / Yahoo Finance](https://finance.yahoo.com/news/biotech-etfs-hovering-around-52-130000773.html)
- [SMH technical analysis: price below 50-day/200-day MA — Barchart.com](https://www.barchart.com/etfs-funds/quotes/SMH/technical-analysis)
- [Micron vs. Sandisk: 1 AI Memory Winner... — Motley Fool, 2026-09-08](https://www.fool.com/investing/2026/09/08/micron-vs-sandisk-1-artificial-intelligence-ai-mem/)

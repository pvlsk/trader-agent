# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-08-05 (pre-market)_

**1 actionable idea today (LLY, catalyst edge), contingent on confirming the gap at/near the open — not chasing if it's already run too far. 3/3 weekly satellite slots open (2026-W32, `counters.json`/`risk.py status` confirm 0/3 used), but real capital room is the binding constraint, not the weekly cap.** Market closed at read time (`clock`: next open 09:30 ET today). Loss cap not tripped. Equity $102,547.38, cash $5,795.47 (`portfolio.py`). Satellite sleeve is currently ~24.0% of equity (XLV+XLF+XLI+XLE+V+IWM ≈ $24,665) against a 30% target — only about **$6,099 of headroom** before the sleeve overshoots its target, i.e. realistically room for **one** new ~4-5% position this week even though all 3 weekly slots are technically open.

## Market read (2026-08-05 pre-market)

S&P 500 futures +0.3-0.4%, Nasdaq-100 flat, after Tuesday's broad rally (+1.79% on S&P) on strong earnings, easing oil, and US-Iran optimism. Polymarket implied 87% odds of a higher open. NVDA gaining pre-market on a partner's strong monthly sales read-through; Arista Networks +14% pre-market on a strong Q3 revenue forecast (neither in universe). ([Stock Market Today — Bloomberg](https://www.bloomberg.com/news/articles/2026-08-04/stock-market-today-dow-s-p-live-updates), [Will S&P 500 Open Up or Down Today? — Benzinga](https://www.benzinga.com/markets/prediction-markets/26/08/60938801/will-sp500-open-up-or-down-august-5-polymarket-record-high-ai-earnings-iran))

**AMD reported after Tuesday's close: beat on every line but the stock still fell ~8% after hours** — EPS $1.66 vs $1.55 est, revenue $11.54B vs $11.31B est (+50% y/y), Data Center revenue +107% y/y to $6.7B, Q3 guidance raised to ~$13B. Investors sold anyway on a "bar too high" read (AMD was already +140% YTD coming in). Not held (watchlist only) — this is a **sell-the-news, not a buy signal**; no pre-positioning. It also argues against chasing the semis bounce (XLK $186.86, SMH $566.17) flagged as tentative in yesterday's IDEAS — that bounce was explicitly pre-positioning into this print, and the print didn't confirm a clean reversal. Semis screen skip again today. ([AMD Earnings Beat Estimates and Stock Falls 8% — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/amd-earnings-beat-estimates-stock-205710559.html), [AMD earnings report Q2 2026 — CNBC](https://www.cnbc.com/2026/08/04/amd-earnings-report-q2-2026.html))

**LLY reported this morning before the open and beat decisively, raising full-year guidance.** EPS $8.38 vs $6.07 consensus (+38% beat); revenue $22.97B vs $20.93B consensus; FY26 revenue guidance raised to $85-87B (from $82-85B), driven by Zepbound/Mounjaro (GLP-1) demand. Reported premarket gain +5%+ off Tuesday's $1,111.28 close. **Caveat: Alpaca's `quote` endpoint currently shows LLY at $1,117.47 — only ~+0.6% over Tuesday's close, not the ~+5% reported in the news wires**, likely because paper-account quotes aren't reflecting the live premarket tape yet this early. **Do not treat either number as the real open print — the open routine must re-check the actual pre-open/opening quote and only enter if the gap is confirmed and isn't already a blown-off spike well past a sane entry.** This is a real, verified catalyst (guidance raise, not just an EPS beat) and correlates positively with held XLV (healthcare), whose thesis has also been improving (-0.5% since entry as of this morning vs -1.8% yesterday). ([Eli Lilly (LLY) earnings Q2 2026 — CNBC](https://www.cnbc.com/2026/08/05/eli-lilly-lly-earnings-q2-2026.html), [Eli Lilly Beats Expectations in Strong Q2 CY2026 — StockStory](https://stockstory.org/us/stocks/nyse/lly/news/earnings/eli-lilly-nyselly-beats-expectations-in-strong-q2-cy2026-full-year-outlook-slightly-exceeds-expectations))

**Relative-strength rotation: XLP (consumer staples, not held) is at a fresh 52-week high and flagged as "Leading" in current rotation coverage, alongside XLI and XLE which we already hold.** XLP last $85.33, up ~9.5% YTD, low beta (0.47) — a genuinely different, more defensive expression of the sector-rotation edge than our existing cyclical/energy-heavy tilt (XLI/XLE/XLF). Distinct source also flags XLB (materials, $52.01, not held) as Leading. Neither is as strong a catalyst as LLY and there likely isn't cash/room for more than one new name this week — ranked below LLY, flagged as backup only. ([Consumer Staples ETF (XLP) Hits a New 52-Week High — Yahoo Finance](https://finance.yahoo.com/news/consumer-staples-etf-xlp-hits-181206804.html), [The 2026 Market Rotation Suggests A Quiet Shift — FXCM](https://www.fxcm.com/markets/insights/the-2026-market-rotation-suggests-a-quiet-shift-with-loud-implications/))

**Momentum watchlist: nothing else clears the bar.** Live quotes checked (AAPL $308.25, MSFT $497.40, NVDA $215.46, AMZN $277.38, GOOGL $380.41, META $599.38, AVGO $414.88, AMD $479.57 — down from Tuesday's close on the after-hours drop, TSLA $325.80, JPM $357.52, COST $948.08, NFLX $74.01) — no other name shows a clean, non-extended breakout distinct from the earnings-week noise already covered above. QQQ $721.17, XBI $152.47, GLD $385.16 also checked, nothing actionable. XLK $186.86, XLY $118.27, XLU $44.10, XLRE $45.15, XLC $112.02 checked, no fresh leadership signal.

## Screened all three edges

- **Momentum/trend:** No unheld name is in a confirmed, un-extended uptrend today; AMD's post-earnings drop confirms the semis bounce flagged yesterday was not a real reversal — skip again.
- **Catalyst:** LLY's beat-and-raise this morning is the one verified, actionable catalyst in the universe — pending confirmation of the actual (not stale) opening quote at market-open. AMD's beat-but-sold-off print is not a buy signal.
- **Relative-strength rotation:** XLP (staples) and XLB (materials) both flagged as current RS leaders we don't hold — XLP is the stronger, more differentiated candidate (defensive tilt vs. our existing cyclical-heavy book) but ranked below LLY given limited room.

## Ranked ideas

| Symbol | Edge | One-line thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|
| LLY | Catalyst | Beat Q2 EPS by 38% ($8.38 vs $6.07 est) and raised FY26 revenue guidance to $85-87B on GLP-1 (Zepbound/Mounjaro) demand; correlates with held XLV, whose thesis is improving. Falsifiable: thesis breaks if LLY gives back today's gain and closes back below Tuesday's $1,111.28 pre-earnings close, or below its 50-day MA. | Confirm actual opening price at market-open — do not chase if premarket has already run past a sane entry (verify the real gap, Alpaca's stale pre-open quote read only +0.6%, news wires read +5%+) | 8% (earnings-driven, elevated event volatility — precedent: AAPL/AMD entries both used 8%) | High, contingent on entry confirmation |
| XLP | Relative-strength rotation | Consumer staples at a fresh 52-week high, flagged as current RS-leading sector, low-beta/defensive — a differentiated rotation expression vs. the book's existing cyclical tilt (XLI/XLE/XLF). Falsifiable: thesis breaks if XLP closes back below its 50-day MA or rotation leadership flips back to cyclicals. | ~$85.30 (near current quote), verify against live open | 10% | Medium — backup only, likely no room left this week if LLY is taken |

## Notes for the open routine

- **LLY is the one actionable idea, but the open routine must re-verify the real opening price first** — Alpaca's current quote ($1,117.47) and the news-reported premarket move (+5%+) disagree; don't enter off either number blind, confirm the live open print and skip if it's already a blown-off gap.
- **Real capital constraint: ~$6,099 of satellite headroom before the 30% target is hit** — LLY alone (~4%, ~$4,100) would leave little room for XLP too; treat XLP as backup only, not a same-day double-entry, unless LLY is skipped.
- **AMD (not held) fell ~8% after a beat-and-raise** — sell-the-news, not a buy signal; also invalidates the tentative semis (XLK/SMH) bounce thesis flagged yesterday. Skip semis again.
- 3 of 3 weekly satellite slots remain unused (2026-W32) — the binding constraint today is cash/target allocation, not the weekly cap.

## Sources

- [Stock Market Today, Aug 5 — Bloomberg](https://www.bloomberg.com/news/articles/2026-08-04/stock-market-today-dow-s-p-live-updates)
- [Will S&P 500 Open Up or Down Today? — Benzinga](https://www.benzinga.com/markets/prediction-markets/26/08/60938801/will-sp500-open-up-or-down-august-5-polymarket-record-high-ai-earnings-iran)
- [AMD Earnings Beat Estimates and Stock Falls 8% — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/amd-earnings-beat-estimates-stock-205710559.html)
- [AMD earnings report Q2 2026 — CNBC](https://www.cnbc.com/2026/08/04/amd-earnings-report-q2-2026.html)
- [Eli Lilly (LLY) earnings Q2 2026 — CNBC](https://www.cnbc.com/2026/08/05/eli-lilly-lly-earnings-q2-2026.html)
- [Eli Lilly Beats Expectations in Strong Q2 CY2026 — StockStory](https://stockstory.org/us/stocks/nyse/lly/news/earnings/eli-lilly-nyselly-beats-expectations-in-strong-q2-cy2026-full-year-outlook-slightly-exceeds-expectations)
- [Consumer Staples ETF (XLP) Hits a New 52-Week High — Yahoo Finance](https://finance.yahoo.com/news/consumer-staples-etf-xlp-hits-181206804.html)
- [The 2026 Market Rotation Suggests A Quiet Shift With Loud Implications — FXCM](https://www.fxcm.com/markets/insights/the-2026-market-rotation-suggests-a-quiet-shift-with-loud-implications/)

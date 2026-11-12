# IDEAS — 2026-11-12 pre-market (07:07 ET)

_Market closed; next open 09:30 ET, close 16:00 ET. Equity $101,486, day P&L -0.18% (cap ok), 5 positions, **W46 0/3 slots used.** Cash $23,114 (~22.8%). Since inception +1.49% vs SPY +1.91% → alpha -0.43%. **Actionable today: 1 (LLY, medium conviction, conditional on the open).**_

## Stop check
`orders` at ~07:07 ET: all 4 satellite stops are live, `new` and qty-matched (V 8% `f583ac37` q11, XLF `9d41c3f6` q71, XLV `f6e70576` q24, XLP `9f108b55` q48). No vanishes.

## Market read
Futures are mixed and lean lower: Nasdaq-100 -0.6% to -0.8%, S&P -0.3% to -0.4%, Dow about flat. The driver is **Nvidia, down >6% premarket** on WSJ/Reuters reports that its board is meeting to discuss Jensen Huang's future as CEO. No decision has been announced, so this is an open binary event risk for the AI/semis complex. CoreWeave/Nebius are -5 to -7%, while AMD (+3%) and AVGO (+2.5%) are catching a rotation bid. On the other side, **Eli Lilly is +2.8–3% premarket after China approved orforglipron (Foundayo)**, the first GLP-1 weight-loss pill approved there, ahead of Novo. Indicative lasts: SPY $760.13, QQQ $689.28, SMH $507.98, IWM $283.05, GLD $365.20, XLE $63.36. Tape: defensives/healthcare leading, AI complex in turmoil. This is no day to add semis.

Sources: [CNBC live updates 11-11](https://www.cnbc.com/2026/11/11/stock-market-today-live-updates.html) · [Globe and Mail: Nasdaq futures fall as Nvidia turmoil rattles AI stocks](https://theglobeandmail.com/investing/markets/inside-the-market/market-news/article-premarket-nasdaq-futures-fall-as-nvidia-turmoil-rattles-ai-stocks) · [Investing.com: Premarket movers — Nvidia sinks; Lilly gains on China approval](https://in.investing.com/news/stock-market-news/premarket-movers-nvidia-sinks-lilly-gains-on-china-approval-5699023) · [Reuters via Investing.com: China approves Lilly's orforglipron](https://www.investing.com/news/stock-market-news/china-approves-eli-lillys-weight-loss-pill-orforglipron-5020481) · [MarketScreener](https://www.marketscreener.com/news/china-approves-eli-lilly-s-weight-loss-pill-orforglipron-ce785ed8d88eff2d) · [TradingKey: AMD +24% in five days](https://www.tradingkey.com/analysis/stocks/us-stocks/262301807-stock-amd-a-microsoft-meta-oracle-nvda-coreweave-tradingkey)

## Sector RS proxy (anchor → today's indicative last)
| Sector | Anchor → now | Read |
|---|---|---|
| XLV | $164.87 (07-07) → $188.98, +14.6% | Leader (held) |
| XLE | $57.01 (07-14) → $63.36, +11.1% | Strong; **now just above the 11-04 exit (~$63.11)** pre-market |
| XLP | $85.34 (08-05) → $91.44, +7.1% | Leader (held) |
| XLF | $55.55 (07-08) → $58.61, +5.5% | Modest leader (held) |
| SPY | $745.87 (07-07) → $760.13, +1.9% | Benchmark |
| XLB | $53.29 (09-03) → $53.00, -0.5% | Lagging |
| XLI | $182.04 (07-13) → $170.94, -6.1% | Lagging |
| XLK | $188.34 (09-08) → $174.35, -7.4% | Lagging (bounced from $168.95 yesterday) |
| XLY/XLU/XLRE/XLC | no anchor | 120.98 / 43.83 / 44.58 / 108.63, roughly flat vs yesterday |

## Ranked candidates
| # | Symbol | Edge | One-line falsifiable thesis | Suggested entry | Trail | Conviction |
|---|---|---|---|---|---|---|
| 1 | **LLY** | Catalyst + momentum | China's approval of orforglipron (first GLP-1 pill there, ahead of Novo) is a real, durable demand catalyst on a stock already above its prior record (~$1,321) and in the leading sector (healthcare). Thesis breaks if LLY gives back the whole approval gap (trades below yesterday's close) or closes below ~$1,380. | **3 sh (~4.2%, ~$4.3k)** at the open via `buy LLY --pct 4 --trail-percent 10` (dry-run first; 5% cap = $5,074 ≈ 3 sh). **Conditions:** take it only if the opening gain vs the prior close is **≤ ~+5%** (the premarket read is +2.8–3%) and it isn't fading below the prior close in the first minutes. **Skip if it gaps >+5%** (blow-off; same rule that skipped LLY on 08-05). | 10% | Medium |
| — | XLE | RS rotation (watch) | Re-entry trigger is a **close** above ~$63.1 (11-04 exit) plus a real catalyst. Pre-market $63.36 is above the level, but there's no close confirmation and no catalyst found (oil news searches returned nothing dated). **Not actionable at the open.** Re-check at EOD: if it closes above $63.1, flag it for tomorrow's pre-market. | — | 8% if taken | Watch |

Healthcare concentration note: LLY is a top XLV holding, so LLY + XLV ≈ 8.7% of equity in healthcare. That's acceptable given healthcare is the #1 RS sector, but don't add a third healthcare name this week.

## Screened and rejected (per the W44 lesson: why each failed)
- **NVDA ($168):** -6% premarket on the CEO-removal reports, with an unresolved binary event. Fails: no trend, event risk.
- **AMD ($554):** +24% in 5 days and +3% more premarket on rotation from NVDA. That's a blow-off chase, still below our 10-12 exit (~$593). Fails: extended/blow-off.
- **AVGO ($346), SMH ($508), QQQ, XLK, MSFT:** the semis/AI complex is in event turmoil and XLK RS still lags (-7% from the Sept anchor). Fails: RS plus event risk.
- **XLE:** see the watch row. No close confirmation and no catalyst.
- **GLD ($365):** down from $369 yesterday, no catalyst, no trend data. Fails: no evidence.
- **JPM ($343):** still below the 09-03 entry and the prior stop-out. Fails: trend.
- **COST, AAPL, AMZN, GOOGL, META, TSLA, NFLX ($64.55, appears split-adjusted):** no verified catalyst found today and no history to confirm trend. Fails: no evidence.
- **IWM, XBI, XLI, XLB, XLY, XLU, XLRE, XLC:** lagging or flat RS, no anchor uptrend. Fails: RS.

## Bottom line for the open
1. Verify the 4 stops (orders vs positions) first.
2. LLY is the only candidate, conditional on the gap rules above. If the conditions fail, do nothing and keep cash. That's fine.
3. No averaging down. No semis today. 2 W46 slots stay in reserve after LLY.
4. Open shift is still reported as firing pre-market (needs 14:33 UTC). If it fires while the market is closed again, the LLY idea rolls to midday only if the gap conditions still hold.

Tooling gap (still open): there's no `bars` subcommand, so the 50/200-day checks rely on web search. LLY's trend was confirmed against its prior record (~$1,321, FXEmpire) and the June 52-week high ($1,166, MarketBeat), not computed MAs.

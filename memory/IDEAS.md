# IDEAS — 2026-11-13 pre-market (07:07 ET, Friday)

_Market closed; next open 09:30 ET, close 16:00 ET. Equity $101,447, day P&L +0.19% (cap ok), 6 positions, **W46 1/3 slots used (2 left).** Cash $18,768 (~18.5%). Since inception +1.45% vs SPY +1.54% → alpha -0.10%. **Actionable today: 0. Best move is to do nothing new.** The one live decision is LLY (see below)._

## Stop check
`orders` at ~07:07 ET: all 5 satellite stops are live, `new` and qty-matched (LLY 10% `43903482` q3, XLP `9f108b55` q48, V 8% `f583ac37` q11, XLF `9d41c3f6` q71, XLV `f6e70576` q24). No vanishes.

## Market read
Futures are roughly flat to slightly up (S&P +0.1–0.2%, Dow +0.1–0.2%, Nasdaq-100 -0.1% to +0.1%). The Nvidia story resolved into a leadership change: Jensen Huang is out, and former CFO Colette Kress is interim CEO. NVDA is bouncing a little premarket ($167.10) after Thursday's drop, but the AI/semis complex is still an open governance story. Microsoft is the only Mag-7 name lower premarket, after a major Outlook/Teams/Copilot outage. Macro focus is inflation and PPI data. Notable premarket movers are all outside our universe (Cerebras +19% on Q3 and a Microsoft deal, Nu +3%, Modine). Indicative lasts: SPY $757.37, QQQ $689.38, SMH $504.43, IWM $278.42, GLD $354.83 (down from $365 two days ago), XLE $64.31. It's a Friday before a weekend, with no fresh catalyst in our universe, so there's no reason to force an entry.

Sources: [Yahoo Finance live, Fri 11-13: futures edge higher as Nvidia tumult deepens](https://finance.yahoo.com/markets/live/stock-market-today-friday-november-13-dow-sp-500-nasdaq-nvidia-110151154.html) · [Globe and Mail premarket: Nasdaq futures dip as Nvidia tumult keeps investors on edge](https://www.theglobeandmail.com/investing/markets/inside-the-market/market-news/article-premarket-world-shares-log-modest-losses-as-investors-assess-impact-on/) · [Investing.com premarket movers: Modine surges; Cerebras jumps on Microsoft deal](https://www.investing.com/news/stock-market-news/premarket-movers-modine-surges-cerebras-jumps-on-microsoft-deal-5024934) · [Benzinga: Cerebras +19% premarket](https://www.benzinga.com/markets/equities/26/11/63230833/cerebras-stock-surges-premarket-q3-results-microsoft-deal) · [CNBC live 11-12](https://cnbc.com/2026/11/12/stock-market-today-live-updates.html)

## LLY — explicit hold/cut call (requested by the 11-12 EOD)
- **Facts:** Indicative $1,430.99 premarket (position mark $1,427, -1.5% vs the $1,448.79 entry). That is **below the $1,437.29 11-11 close, its thesis line #1** ("gives back the whole approval gap"). LLY goes **ex-dividend today** (~$1.7/sh quarterly, amount not re-verified), which explains roughly $1.7 of the gap. Ex-div adjusted, line #1 sits at about $1,435.5, and LLY is still below it. It is far above line #2 (close below ~$1,380) and the trail (~$1,305, 10% off the high-water mark).
- **Honest read:** Line #1 is breached, so the thesis is weakened. The catalyst itself (China approval) is intact and nothing new has gone against it. The breach is about 0.3–0.5% on a price giveback in a soft tape, not a catalyst failure.
- **Call: HOLD, with an explicit line.** A discretionary cut is blocked anyway, because the stop holds all 3 shares (cancel/replace gap, `LESSONS.md` 2026-07-24), so the exit is the stop. Pre-commitment for the open, midday and EOD shifts: **if LLY *closes* below ~$1,380 (line #2), log the thesis as fully broken. If the tooling gap is ever fixed, cut it that day.** Do not average down, and don't add a 3rd healthcare name. If LLY reclaims ~$1,437 on a close, line #1 is restored. Grade the entry timing honestly in the W46 review: we bought the fade of a gap.

## Sector RS proxy (anchor → today's indicative last)
| Sector | Anchor → now | Read |
|---|---|---|
| XLV | $164.87 (07-07) → $187.83, +13.9% | Leader (held) |
| XLE | $57.01 (07-14) → $64.31, +12.8% | Strong; **2nd session above the ~$63.11 11-04 exit** (11-12 EOD snapshot $64.75) |
| XLP | $85.34 (08-05) → $91.07, +6.7% | Leader (held) |
| XLF | $55.55 (07-08) → $58.20, +4.8% | Modest leader (held), soft |
| SPY | $745.87 (07-07) → $757.37, +1.5% | Benchmark |
| XLB | $53.29 (09-03) → $52.32, -1.8% | Lagging |
| XLI | $182.04 (07-13) → $169.42, -6.9% | Lagging |
| XLK | $188.34 (09-08) → $173.73, -7.8% | Lagging |
| XLY/XLU/XLRE/XLC | no anchor | 120.44 / 43.82 / 44.34 / 107.58, all slightly lower vs yesterday |

## Ranked candidates
| # | Symbol | Edge | One-line falsifiable thesis | Suggested entry | Trail | Conviction |
|---|---|---|---|---|---|---|
| — | **None actionable** | — | No new name clears the bar today. Holding cash is the call. | — | — | — |
| W1 | XLE | RS rotation (watch) | Price now confirms (above the ~$63.1 exit for 2 sessions; #2 RS sector by our anchor proxy), but the **catalyst leg is still unverified**: oil-price searches returned only stale results (latest dated Brent ~$115 on 10-28; OPEC+ reported preparing to stop raising output targets, undated). **Not actionable today** (Friday, weekend gap risk, half the trigger missing). If Monday's pre-market can cite a dated oil/OPEC catalyst and XLE still holds > $63.1, it becomes a ~4% entry with an 8% trail. | Mon pre-market re-check | 8% if taken | Watch |

## Screened and rejected (per the W44 lesson: why each failed)
- **NVDA ($167):** CEO exit, Kress interim CEO. That's an unresolved governance event, and there's no trend. Fails: event risk.
- **AMD ($585):** +24%+ in a week on rotation, just below our 10-12 exit (~$593). Fails: extended/blow-off chase.
- **SMH ($504), AVGO, QQQ, XLK:** the semis/AI complex is still in NVDA turmoil, and XLK RS is -7.8% vs its anchor. Fails: RS plus event risk.
- **MSFT:** down premarket on a major Outlook/Teams/Copilot outage, a negative catalyst. Fails: catalyst against.
- **GLD ($354.8):** -2.8% in two sessions, falling. Fails: trend.
- **LLY (add):** already held, below thesis line #1. No averaging down. Fails: rule.
- **XBI, other healthcare:** a 3rd healthcare name breaks the concentration note. Fails: concentration.
- **JPM, V-adjacent financials:** XLF is soft (-0.7% vs yesterday's mark), and JPM is below its prior stop-out. Fails: trend.
- **AAPL, AMZN, GOOGL, META, TSLA, NFLX, COST:** no dated catalyst found today. Fails: no evidence.
- **IWM ($278, down from $283 two days ago), XLI, XLB, XLY, XLU, XLRE, XLC:** lagging or slipping RS. Fails: RS.
- **CBRS, NU, MOD (premarket movers):** outside the universe, and these are earnings gaps (blow-off risk). Fails: universe plus gap rule.

## Bottom line for the open
1. Verify the 5 stops (orders vs positions) first.
2. **No new entries today.** Keep the 2 W46 slots unused. Going into the weekend in cash is fine.
3. LLY: hold to the stop, watch the ~$1,380 close line. No averaging down.
4. The open shift is still reported as firing pre-market (needs 14:33 UTC). Nothing is lost today if it skips again, since nothing is actionable.
5. EOD/Friday: W46 weekly review due after the close.

Tooling gaps (still open): there is no `bars` subcommand (so 50/200-day checks rely on web search) and no `cancel` subcommand (blocks discretionary cuts and tightening; `LESSONS.md` 2026-07-24).

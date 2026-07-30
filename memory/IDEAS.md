# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-07-30 (pre-market)_

**0 actionable new entries recommended today, despite 3/3 weekly satellite slots being open (2026-W31, `counters.json`/`risk.py status` confirm 0/3 used).** Market closed at read time (`clock`: next open 09:30 ET today). Loss cap not tripped (day P&L -0.83%, equity $98,688.51 per `risk.py status`). Yesterday's hawkish FOMC reaction plus tonight's AAPL/AMZN earnings make this another high-event-risk day; no screened setup clears the bar for adding fresh risk into it.

## Market read (2026-07-30 pre-market)

**Yesterday's FOMC decision landed hawkish.** The Fed held rates steady, but three FOMC members (Hammack, Kashkari, Logan) dissented in favor of a hike — a two-sided outcome that was flagged pre-market as unusually live. The market sold off hard into the close: S&P -1.52%, Nasdaq -1.74%, Dow -2.19%, with the 10-year yield jumping to 4.67%. ([TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-july-29-2026stock-market-today-july-29-2026), [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/stock-market-today-july-29-212135780.html))

**MSFT and META reported last night, with a stark split.** Microsoft beat on cloud/Azure strength and is up **+8.3% pre-market** (capex +70% to $41B, but profits still grew). Meta missed badly — EPS $6.18 vs. $7.22 expected, opex +55% to $42B, next-quarter revenue guided below consensus — and is down **-10%**. Futures are recovering this morning (Dow +0.4%, S&P +0.6%, Nasdaq +1.4%), largely on the MSFT print. ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-29/microsoft-meta-earnings-face-a-market-growing-skeptical-of-ai), [XTB](https://www.xtb.com/en/market-analysis/chalk-and-cheese-meta-and-microsoft-earnings-round-up))

**AAPL (held satellite) and AMZN both report tonight after the close.** Wall St. expects AAPL EPS ~$1.89 on ~$108.65B revenue (watching iPhone revenue, memory-cost margin pressure, Apple Intelligence progress); AMZN consensus EPS ~$1.81 with AWS growth as the swing factor. This is the second half of the Big Tech earnings gauntlet and the single biggest event risk for the book tonight — AAPL rides in on its existing 8% trail only (tightening/discretionary-cut both still blocked by the standing `scripts/alpaca.py` cancel/replace tooling gap). ([AppleInsider](https://appleinsider.com/articles/26/07/27/what-wall-street-expects-from-apples-q3-2026-earnings-on-july-30), [Investing.com](https://www.investing.com/news/stock-market-news/apple-amazon-stryker-and-more-set-to-report-earnings-thursday-93CH-4821461))

**Sector rotation: industrials and financials continue gaining relative strength, consistent with held theses.** XLK still leads YTD sector returns (buoyed by AAPL/semis) despite the recent chip wobble; industrials (XLI, held) and financials (XLF, held) are gaining 1- and 3-month RS as the rally broadens past mega-cap tech; communication services (XLC) and staples (XLP) show relative weakness — the former reinforced by last night's Meta miss. Nothing here argues for a new position; it supports the two sector ETFs already held. ([etfdb.com](https://etfdb.com/sector-investing-content-hub/xlk-xle-xli-top-performing-sector-spdrs/))

**The AI-semiconductor complex remains choppy, not trending.** A recent session saw AMD -10%/NVDA -2% on AI-capex-spending-ROI skepticism; the group has been attempting a recovery since but there's no clean, confirmed uptrend to buy — live quotes this morning: NVDA $189.46, AMD $424.68, AVGO $367.07, SMH $520.22. This rules out a fresh semiconductor entry and gives no new reason to view XLK (already thesis-broken, un-cuttable per the tooling gap) more favorably. ([Yahoo Finance: AI chip stocks tumble](https://finance.yahoo.com/technology/ai/articles/ai-chip-stocks-tumble-nvidia-195907285.html))

**No fresh, dated, in-universe analyst upgrade found.** Today's notable upgrades (Bloom Energy, CarMax, Ford) are all outside `config/universe.yaml`.

## Screened all three edges — nothing cleared the bar

- **Momentum/trend:** MSFT's +8.3% pre-market gap is a real, verified beat-driven catalyst, but it's a blow-off gap on the print itself — `config/strategy.md` explicitly cautions against chasing blow-off gaps, and there is no margin of safety left in the entry price this morning. Checked the rest of `momentum_watchlist` (NVDA, AMZN, GOOGL, AVGO, AMD, TSLA, JPM, V, COST, LLY, NFLX) plus `theme_etfs` (QQQ, IWM, SMH, XBI, GLD) — nothing else shows a clean, un-owned uptrend; AMZN is in pre-earnings territory (reports tonight), the chip names (NVDA/AMD/AVGO/SMH) are still choppy, not trending.
- **Catalyst:** MSFT (see above, not actionable as a chase) and tonight's AAPL/AMZN prints (not yet known) are the only dated catalysts in the universe; nothing both real and actionable today.
- **Relative-strength rotation:** XLI and XLF (both held) continue to be the cleanest expressions of the broadening-rotation theme; live quotes checked on unheld sector ETFs (XLB $51.73, XLRE $45.96, XLC $109.57, XLU $44.90, XLP $87.32) — none shows a fresh breakout against SPY this week, and XLC/XLP are actively the weakest, not candidates. Adding a second industrials/financials name (e.g. JPM) would concentrate rather than diversify the existing XLF/XLI exposure.

## Ranked ideas

**None actionable today.** Given (1) yesterday's hawkish-FOMC selloff, (2) AAPL/AMZN earnings tonight (the second half of this week's Big Tech gauntlet, with AAPL already a held position), (3) MSFT's move being a blow-off gap rather than a basing breakout, and (4) no fresh rotation or momentum setup clearing the bar without duplicating existing sector exposure, the correct call is to hold all 3 weekly slots in reserve.

| Symbol | Edge | One-line thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|
| MSFT | Catalyst (earnings beat) | Genuine Azure/cloud-driven beat, but today's +8.3% pre-market move is a blow-off gap with no margin of safety — wait for a pullback toward the pre-earnings range or a multi-day base, do not chase at the open. | Wait, re-evaluate on a pullback | 8% (tighter than default given gap size) | Low — not actionable today |
| JPM | Relative-strength rotation | Financials continue gaining 1-/3-month RS alongside our held XLF, but this duplicates existing sector exposure rather than diversifying it. | ~$345 (near current) | 10% | Low — overlaps existing XLF position |

## Notes for the open routine

- **AAPL (held, 8% trail) reports tonight after the close, alongside AMZN** — expect the tape (and AAPL specifically) to gap tomorrow morning; the position rides in on its existing trail only, tightening/discretionary-cut both still blocked by the standing tooling gap.
- **Do not chase MSFT's pre-market gap** — real catalyst, but priced in already; if it pulls back and bases over the coming sessions it could become a legitimate momentum candidate later.
- **Meta's miss reinforces XLC/communication-services weakness** — no action needed (not held), but relevant context for the rotation read.
- **IWM's 50-day-MA watch carries over from EOD** (live quote flagged at $288.63 vs. a stale ~$290.80 reference) — un-cuttable regardless of the read (tooling gap), its own 10% trail is the only real exit.
- 3 of 3 weekly satellite slots remain unused and available (2026-W31) — re-run this scan fresh tomorrow once tonight's AAPL/AMZN prints are known; don't assume today's read still holds.

## Sources

- [Stock Market Today (July 29, 2026): Dow tumbles 800 points as Fed holds interest rates steady — TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-july-29-2026stock-market-today-july-29-2026)
- [Stock Market Today, July 29: Stocks Slide on Hawkish Fed and Increased Middle East Tensions — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/stock-market-today-july-29-212135780.html)
- [Microsoft, Meta Earnings Face a Market Growing Skeptical of AI — Bloomberg](https://www.bloomberg.com/news/articles/2026-07-29/microsoft-meta-earnings-face-a-market-growing-skeptical-of-ai)
- [Chalk and Cheese: Meta and Microsoft earnings round up — XTB](https://www.xtb.com/en/market-analysis/chalk-and-cheese-meta-and-microsoft-earnings-round-up)
- [What to expect from Apple's earnings 3Q 2026 — AppleInsider](https://appleinsider.com/articles/26/07/27/what-wall-street-expects-from-apples-q3-2026-earnings-on-july-30)
- [Apple, Amazon, Stryker, and more set to report earnings Thursday — Investing.com](https://www.investing.com/news/stock-market-news/apple-amazon-stryker-and-more-set-to-report-earnings-thursday-93CH-4821461)
- [Top-Performing Sector SPDRs: XLK, XLE & XLI Top The List — etfdb.com](https://etfdb.com/sector-investing-content-hub/xlk-xle-xli-top-performing-sector-spdrs/)
- [AI Chip Stocks Tumble as Nvidia, AMD Lead Market Selloff Over Spending Fears — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/ai-chip-stocks-tumble-nvidia-195907285.html)

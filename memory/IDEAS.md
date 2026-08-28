# IDEAS — ranked trade candidates (drafted pre-market)

_Last updated: 2026-08-28 (pre-market)_

**No actionable idea today — cash-blocked (23 straight calendar days flat) and, on top of that, no idea screened clears the bar.** `portfolio.py`/`alpaca.py account`: equity **$102,508.45**, day P&L +0.06% (loss cap -3% not tripped, no halt), cash **$1,699.14** (unchanged since 2026-08-05 = **23 calendar days**). A compliant new 5% satellite position needs **$5,125** — cash is well short (per LESSONS 2026-08-05, only settled cash counts, not `buying_power`/margin). `risk.py status`: **2026-W35, 0/3 weekly slots used**, moot until cash frees up or the operator answers the 2026-08-21 minimum-size escalation (still open as of last night, now due for today's 2026-08-28 weekly review).

## Market read (2026-08-28 pre-market)

Market closed at read time (`clock`: next open 09:30 ET today, closes 16:00 ET). Futures are roughly flat to slightly soft (Nasdaq-100 -0.3%) heading into the day's dominant catalyst: **Fed Chair Kevin Warsh delivers his Jackson Hole keynote at 10:00 AM ET**, with markets pricing a 33.7% chance of a September hike per CME FedWatch and looking for clarity after his last-meeting stance created confusion ([Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-friday-august-28-dow-sp-500-nasdaq-fed-warsh-jackson-hole-081514091.html), [Benzinga](https://www.benzinga.com/markets/equities/26/08/61486721/stock-market-today-sp-500-nasdaq-100-futures-slip-ahead-of-kevin-warshs-jackson-hole-speech-mrvl-pypl-iren-gap-in-focus)). This is a binary-ish macro event that can whipsaw the whole tape within the first half hour of trading — a bad window to open a fresh satellite position into, independent of the cash block.

Overnight earnings were mixed and mostly outside our universe: Marvell (MRVL, unheld) beat but guided gross margin light and dropped ~8% on **renewed semiconductor-tariff risk** (Politico/Benzinga report the White House is weighing new Section 232-style tariffs on chips and chip-containing goods — laptops, servers, gaming consoles); PayPal (unheld) plunged ~16% on a killed buyout rumor; Affirm (unheld) and Elastic (unheld) jumped on strong guides. None are in `config/universe.yaml`, so none are actionable regardless of cash.

## Screened all three edges

- **Momentum/trend:** Nothing new in the universe broke to fresh highs overnight; the held book's trend leaders are unchanged from yesterday (XLE +9.3%, V +6.1%, XLV +4.4% since entry).
- **Catalyst:** **Downgrading yesterday's XLK idea.** The NVDA-beat tailwind that made XLK attractive Wednesday night is now competing with a fresh, real headwind: the same semiconductor-tariff risk that hit MRVL yesterday. Multiple sources ([The Star](https://www.thestar.com.my/tech/tech-news/2026/08/27/us-weighs-a-new-round-of-tariffs-on-semiconductors-politico-reports), [Benzinga](https://www.benzinga.com/markets/tech/26/08/61456385/trump-weighs-new-semiconductor-tariffs-that-could-hit-ai-data-center-servers-laptops-and-gaming-consoles-report)) report the administration is actively weighing new chip tariffs, and XLK carries ~40% concentration in NVDA/AAPL/MSFT — exactly the names most exposed. This is a live, unresolved catalyst working *against* the thesis, not confirmation of it. No other universe name has a fresh, verified, directional catalyst this morning.
- **Relative-strength rotation:** Independent RS reporting ([stockcheatsheets.substack.com](https://stockcheatsheets.substack.com/p/our-latest-us-sector-and-index-etf), [investinglive.com](https://investinglive.com/stocks/stock-market-sector-rotation-update-industrials-join-technology-in-cooling-off/)) confirms the book's own performance pattern: **Energy, Financials, and Healthcare are the current RS leaders — all three already held** (XLE, XLF, XLV). **Technology and Industrials are both described as "cooling off"** — XLI is unheld-adjacent... no, XLI is held and is in fact the book's only red name (-1.8%), consistent with this call; XLK (unheld) losing momentum plus the tariff overhang above is a second, independent reason to leave it off the list today. No leadership rotation into a name we don't already hold.

## Ranked ideas

**No actionable candidate today — not just cash-blocked, but nothing clears the bar on thesis quality either.**

| Symbol | Edge | One-line thesis | Suggested entry | Trail % | Conviction |
|---|---|---|---|---|---|
| — | — | No idea both (a) outside the already-held book and (b) supported by a live, verified, un-contradicted catalyst or RS trend today. | — | — | — |

**Best move is to do nothing** on the idea-generation side today, independent of the cash block: RS leadership sits entirely inside positions already held (XLE/XLF/XLV), the one live catalyst candidate (XLK) now has a real headwind attached (chip-tariff risk) that wasn't present Wednesday night, and the day's dominant event (Warsh's 10:00 AM ET speech) argues for letting the open routine reconcile rather than chase a pre-speech gap even if cash allowed it.

## Notes for the open routine

- **No actionable new entry today** — cash ($1,699.14, 23 straight calendar days flat) remains the binding constraint, and this morning's screen doesn't produce a idea worth queuing behind it either. Reconcile positions/stops only; market opens regularly at 09:30 ET.
- **Fed Chair Warsh speaks at Jackson Hole 10:00 AM ET today** — the day's dominant catalyst, expect elevated volatility in the first 30-60 min after; none of the 8 held positions are direct rate-sensitive plays, but SPY and the broad tape will move on the headline.
- **XLK idea from 2026-08-27 is downgraded, not carried forward** — new overnight semiconductor-tariff risk (MRVL guided light and fell ~8% on it) undercuts the NVDA-beat catalyst; XLK is ~40% concentrated in the exact names (NVDA/AAPL/MSFT) most exposed to a chip tariff.
- **XLE (held) remains the extended-winner tighten candidate** at ~+9.3% since entry — retightening still blocked by the cancel/replace tooling gap (`memory/LESSONS.md` 2026-07-24, unresolved for 6+ consecutive weekly reviews).
- **Cash lockout is now 23 straight calendar days** (since 2026-08-05); the 2026-08-21 operator escalation on a minimum-size floor / cash-sized-entry policy is still unanswered — today's 2026-08-28 weekly review is the scheduled checkpoint to push it again.

## Sources

- [Stock market today: Dow, S&P 500, Nasdaq futures hold steady as focus turns to Kevin Warsh's Jackson Hole speech — Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-friday-august-28-dow-sp-500-nasdaq-fed-warsh-jackson-hole-081514091.html)
- [Stock Market Today: S&P 500, Nasdaq 100 Futures Slip Ahead of Kevin Warsh's Jackson Hole Speech — Benzinga](https://www.benzinga.com/markets/equities/26/08/61486721/stock-market-today-sp-500-nasdaq-100-futures-slip-ahead-of-kevin-warshs-jackson-hole-speech-mrvl-pypl-iren-gap-in-focus)
- [Stocks making the biggest moves premarket: PayPal, Affirm Holdings, Gap, Marvell Technology & more — CNBC](https://www.cnbc.com/2026/08/28/stocks-making-the-biggest-moves-premarket-pypl-afrm-gap-mrvl.html)
- [MRVL Stock Reverses Below $240 After Marvell Fiscal Q2 Earnings as Chip Tariff Risks Rise — FX Leaders](https://www.fxleaders.com/news/2026/08/27/mrvl-stock-reverses-below-240-after-marvell-fiscal-q2-earnings-as-chip-tariff-risks-rise/)
- [US weighs a new round of tariffs on semiconductors, Politico reports — The Star](https://www.thestar.com.my/tech/tech-news/2026/08/27/us-weighs-a-new-round-of-tariffs-on-semiconductors-politico-reports)
- [Trump Weighs Semiconductor Tariffs on Laptops, Servers, and More — Benzinga](https://www.benzinga.com/markets/tech/26/08/61456385/trump-weighs-new-semiconductor-tariffs-that-could-hit-ai-data-center-servers-laptops-and-gaming-consoles-report)
- [Our Latest US Sector & Index ETF Relative Strength Rank & Trend Report: Industrials Lead as Tech Momentum Cools — stockcheatsheets.substack.com](https://stockcheatsheets.substack.com/p/our-latest-us-sector-and-index-etf)
- [Stock market sector rotation update: Industrials join Technology in cooling off — investinglive.com](https://investinglive.com/stocks/stock-market-sector-rotation-update-industrials-join-technology-in-cooling-off/)

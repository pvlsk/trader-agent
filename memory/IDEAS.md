# IDEAS — 2026-10-13 pre-market (08:07 ET)

_Market closed at 08:07 ET; next open 09:30 ET. Equity $102,279.52, day P&L +0.09% (cap ok), 7 positions (SPY core + 6 satellites), **week 2026-W42, 0/3 slots used.** Cash ~$15.2k (~14.9%). **Actionable today: none.**_

## ⚠️ Priority for the open routine
**XLE's trailing stop (`1b112315`, qty 70) is GONE from open orders** — `orders` shows only 5 stops (XLF, XLV, XLK, XLP, V). It was live at 10-12 EOD. No fill/position change (XLE still 70 sh, ~$4,648, +16.4%, last $66.03). 3rd vanished-stop incident (XLV 10-06, XLF 10-07). XLE is currently UNPROTECTED. At the open: re-verify with `orders`, then re-place `python3 scripts/alpaca.py stop XLE --trail-percent 10` (or tighter, ~8%, given +16% gain) if still absent.

## Market read
Indicative pre-market last prices: SPY $777.96 (flat/slightly down vs 10-12 pre $778.60), XLK $196.27, XLV $171.98 (leader, up), XLE $66.03 (up ~1.5%), XLF $55.05, XLP $84.40, XLI $169.12, XLY $112.28, XLU $41.62, XLB $49.44, XLRE $41.92, XLC $111.44. No fresh catalyst verified (no dated news fetched). Healthcare/energy lead among held names; staples/financials roughly flat vs entry. Ranking vs SPY unchanged from prior days: tech and healthcare leading, no new sector breaking out.

## Ranked candidates
**None actionable.** No verified catalyst; leaders (XLK, XLV, XLE) already held. Keep all 3 W42 slots open. Cash is a position; satellite sleeve (~24%) below 40% target is a result of stop-outs, not a mandate to force fills.

Conditional (low conviction, unchanged): XLU only if it confirms top-3 RS vs SPY after the open (needs written thesis, <=3-4% size, 10% trail).

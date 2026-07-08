# STATE — live portfolio (source of truth for what we hold and why)

_Last updated: 2026-07-08 (market-open routine, executed)_

## Core
| Symbol | Target % | Actual % | Notes |
|---|---|---|---|
| SPY | 70% | ~69.4% | 93 sh @ $745.88 avg. Buy-and-hold, no trailing stop. Established 2026-07-07. Within band, no top-up needed today. |

## Satellite positions
| Symbol | Entry date | Size % | Entry $ | Trail % | Edge | One-line thesis | Status |
|---|---|---|---|---|---|---|---|
| XLV | 2026-07-07 | ~3.9% | $164.87 | 10% | Relative-strength rotation | XLV is the #1 relative-strength SPDR sector, at new highs (+10.4% 60d, +7.8% 20d) — healthcare leadership. RS crossed above 70 (overbought) as of 2026-07-08; watch for a tighter trail at midday if it extends further. | Open, trailing stop live |
| XLF | 2026-07-08 | ~3.95% | $55.55 | 10% | Relative-strength rotation | Rotation out of tech into financials into bank earnings season (JPM/WFC/BAC/C report 2026-07-14); verified same-day that price ($55.44-55.55) trades well above both the 50-day (~$52.42) and 200-day (~$52.60) MAs with a new 52-week high this week, resolving yesterday's conflicting technical reads in favor of the bullish thesis. | Open, trailing stop live |

## Open stops / orders
- XLV: trailing_stop sell, 10%, GTC (order 1d53e9c2), qty 24. Live.
- XLF: trailing_stop sell, 10%, GTC (order 4c22f833), qty 71. Live.

## Notes for the next routine
- **2026-07-08 market-open, executed:** verified XLF's conflicting technical reads via WebSearch before entering — confirmed price ($55.44-55.55) is well above both the 50-day (~$52.42) and 200-day (~$52.60) MAs with a new 52-week high this week, so the bullish rotation thesis stands. Bought XLF, ~3.95% (71 sh @ ~$55.55), 10% trailing stop attached (order 4c22f833).
- Passed on XLE (blow-off-gap risk from the Iran-ceasefire oil spike, not a confirmed trend) and on the momentum watchlist (all under pressure from the geopolitical + AI-chip sentiment shock) — consistent with `memory/IDEAS.md`.
- XLV unchanged today (down slightly, not extending further) — left its 10% trailing stop as-is; RS >70 overbought flag from pre-market still applies if it runs further on a later session.
- 2 of 3 weekly satellite slots now used (ISO week 2026-W28); 1 remains.
- Core SPY at ~69.4% of equity, within the 70% target band — no top-up needed today.
- **Operational incident (self-corrected):** the first `buy XLF` invocation ran via a `python3 ... || python ...` shell fallback pattern. The `python3` call succeeded in submitting the market buy but then failed to attach the trailing stop (race: tried to submit the stop before the buy had registered as filled, got a transient 403 "cannot open a short sell while a long buy order is open"), which made the whole command exit non-zero — so the `||` fallback re-ran the *entire* buy command, submitting a second live 71-share buy order. Both filled, leaving a 142-share XLF position (~7.9% of equity, over the 5% cap) and double-incrementing `new_positions_this_week`. Caught it immediately via `positions`/`orders`, sold 71 shares back down to the intended 71-share (~3.95%) position, attached the trailing stop, and hand-corrected `counters.json` from 3 back to 2 new-positions-this-week. See `memory/LESSONS.md` — do not use shell `||` fallback around any order-submitting command.

# STATE — live portfolio (source of truth for what we hold and why)

_Last updated: 2026-07-07 (initial deploy + validation trades)_

## Core
| Symbol | Target % | Actual % | Notes |
|---|---|---|---|
| SPY | 70% | ~69.4% | 93 sh @ $745.88 avg. Buy-and-hold, no trailing stop. Established 2026-07-07. |

## Satellite positions
| Symbol | Entry date | Size % | Entry $ | Trail % | Edge | One-line thesis | Status |
|---|---|---|---|---|---|---|---|
| XLV | 2026-07-07 | ~4.0% | $164.87 | 10% | Relative-strength rotation | XLV is the #1 relative-strength SPDR sector, at new highs (+10.4% 60d, +7.8% 20d) — healthcare leadership. | Open, trailing stop live |

## Open stops / orders
- XLV: trailing_stop sell, 10%, GTC (order 1d53e9c2), qty 24. Live.

## Notes for the next routine
- Account initialized 2026-07-07. Inception baseline: $100,000; SPY $745.87 (see counters.json).
- 1 of 3 weekly satellite slots used (ISO week 2026-W28).
- XLV was a system-validation entry grounded in a real momentum/RS probe; it is a legitimate on-thesis position, not a throwaway — manage it normally (trailing stop, cut if healthcare loses leadership).
- Next pre-market run should generate fresh ideas; ~2 satellite slots remain this week.
- Other names flagged strong in the 2026-07-07 probe (for context): LLY, V, JPM, AAPL, and sectors XLF/XLV at new highs.

# STATE — live portfolio (source of truth for what we hold and why)

_Last updated: 2026-07-07 (initial deploy + validation trades; pre-market notes added same day)_

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
- 1 of 3 weekly satellite slots used (ISO week 2026-W28); 2 remain.
- XLV was a system-validation entry grounded in a real momentum/RS probe; it is a legitimate on-thesis position, not a throwaway — manage it normally (trailing stop, cut if healthcare loses leadership). XLV thesis reconfirmed in the 2026-07-07 pre-market run: still a one-month sector leader, top holdings (LLY/JNJ/ABBV) near all-time highs.
- **Pre-market run 2026-07-07 (for the 2026-07-08 open) — see `memory/IDEAS.md` for full detail.** Top actionable ideas for the open routine, using the 2 remaining weekly slots: (1) **XLF** — relative-strength rotation, 5-week win streak into record territory; (2) **V** — momentum/catalyst, JPMorgan's top financials pick, near highs. Note both ideas concentrate in financials (V is a top-5 XLF holding) — size conservatively if taking both.
- Explicitly **not** actionable this week: JPM (earnings 7/14, event risk inside a typical swing hold — revisit after the print) and AAPL (real iPhone-foldable catalyst but already +12% in 5 sessions, 1.5% off all-time highs, elevated valuation — extended, don't chase).
- Semiconductors/broad tech (XLK, SMH, AMD, NVDA, AVGO, MSFT) hit a global valuation-reset selloff on 2026-07-07 (Samsung earnings miss vs. high expectations triggered the cascade) — no momentum/catalyst edge there right now, avoid catching the falling knife.
- Market was closed at run time (after-hours, next open 2026-07-08 09:30 ET) — this was a research-only run, no trades placed.

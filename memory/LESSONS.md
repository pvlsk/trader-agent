# LESSONS — durable rules the desk has learned (consult before trading)

Seeded with priors from the strategy. Add to this whenever a trade teaches something. Keep each lesson as a rule that changes future behavior.

## Starting priors
- **The core is the edge.** 70% in SPY means we start each week nearly matching the index. Don't jeopardize that reliability chasing satellite thrills.
- **Cut fast, let winners run.** Trailing stops exist so losers are small and winners are large. Never widen a stop; never average down.
- **A thesis or no trade.** If you can't write one falsifiable line for why, skip it. Boredom is not a signal.
- **Respect the caps.** The 5%/position, 3-per-week, and 3% daily loss cap are the difference between a strategy and gambling. The script enforces them — treat a rejection as wisdom, not an obstacle.
- **Beating SPY is hard.** Most active trading underperforms. Assume the burden of proof is on every satellite trade to justify its risk over just holding the index.
- **Don't revenge-trade.** After a stop-out, the next trade must clear the same bar as any other. Emotion is the enemy.

## Learned lessons
- **Never wrap an order-submitting command in a shell `||` fallback.** On 2026-07-08 a `python3 scripts/alpaca.py buy XLF ... || python scripts/alpaca.py buy XLF ...` pattern (used to try `python3` then fall back to `python`) caused a duplicate live buy: the first invocation submitted the market order successfully but exited non-zero when the trailing-stop attach step hit a transient race ("cannot open a short sell while a long buy order is open"), so the `||` triggered the second invocation, which submitted a second full buy order. Result: a satellite position at ~7.9% of equity (over the 5% cap) and a double-counted weekly slot, both caught and corrected after the fact only by manually checking `positions`/`orders` against intent. Fix: run buy/sell/stop commands as a single invocation (pick one interpreter and commit to it, e.g. probe with `python3 --version` once, or just run `python3 ...` and report failure rather than silently retrying with a fallback). If a command exits non-zero after "submitted" appears in its output, check live `positions`/`orders` before doing anything else — do not assume it's safe to retry.

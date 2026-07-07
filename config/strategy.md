# Strategy Spec — trader-agent

**Mission:** beat SPY total return over the long run on an Alpaca paper account, then graduate to real money only after a sustained, disciplined track record.

## Structure: core–satellite

| Sleeve | Target | What it is |
|---|---|---|
| **Core** | ~70% | Buy-and-hold **SPY**. This structurally guarantees we nearly match the index. No trailing stop. Rebalanced toward 70% only when it drifts outside the band. |
| **Satellite** | ~30% | Tactical swing trades that try to add alpha on top of the core. Every satellite entry gets a trailing stop. |

Because 70% is passive index, the most we can *underperform* by is roughly the drag of the satellite sleeve — and the upside is real if the satellite adds alpha. That asymmetry is the whole point.

## The three edges (satellite only)

1. **Momentum / trend.** Buy liquid names/ETFs in confirmed uptrends (price above rising 50-day and 200-day averages, near 52-week highs, strong recent relative strength). Let winners run under a trailing stop; never average down.
2. **Catalyst-driven.** Act on discrete, verifiable catalysts surfaced pre-market: earnings beats with guidance raises, analyst upgrades, sector-moving news. Enter only after confirming the catalyst is real and the reaction has direction; avoid buying blow-off gaps.
3. **Relative-strength rotation.** Rank the 11 SPDR sector ETFs by trailing relative strength vs SPY (e.g. 1–3 month). Tilt the satellite toward the top 2–3 sectors; rotate out as leadership changes.

## Position sizing & cadence

- **Max 5% of equity per satellite position** (~$5k on $100k) → satellite holds ~6 names at full size. Diversified by design.
- **Max 3 new satellite positions per ISO week.** (`scripts/risk.py` enforces both.)
- **Trailing stop on every satellite entry**, default 10% (tighten to ~6–8% on extended winners at midday).
- **3% daily loss cap:** if the account is down ≥3% on the day, no new entries until the next session. Existing stops still work.
- Prefer **holding periods of days to weeks** (swing). Avoid intraday round-trips (keeps us clear of the Pattern Day Trader rule when we go real-money).

## Entry checklist (satellite)
- Symbol is in `config/universe.yaml` (or a clearly justified equivalent), liquid, not an option/leveraged product.
- A real reason from one of the three edges, written as a one-line thesis.
- Sizing ≤5%, weekly slot available, loss cap not tripped. (The script will refuse otherwise.)
- Trailing stop attached at entry.

## Exit rules
- **Trailing stop** is the primary exit — it cuts losers and lets winners run automatically.
- **Midday discretionary cut:** if a position's thesis is broken (catalyst failed, breaks key support, sector rolls over), close it early rather than wait for the stop.
- **Rotation:** when a held sector loses leadership, rotate into the new leader on the next open, within cadence limits.
- Never turn a swing trade into a "bagholder" investment. If the reason you bought is gone, the trade is over.

## Benchmark & grading
- `scripts/portfolio.py` reports return since inception vs SPY over the same window (alpha). This is the scorecard.
- Weekly (Friday) self-grade weighs: (1) return vs SPY that week, (2) risk discipline (did we respect every guardrail), (3) process quality (were theses sound, were exits obeyed). A great process with a slightly down week still earns a good grade; reckless gambling that happened to win does not.

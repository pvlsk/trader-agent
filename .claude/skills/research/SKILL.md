---
name: research
description: Research catalysts, momentum, and sector relative strength for the swing-trading universe, then produce a ranked list of trade ideas with thesis, entry, and trailing stop. Use in the pre-market routine and whenever fresh ideas are needed.
---

# Skill: research

Turn market information into a small, ranked set of actionable swing ideas. Quality over quantity — three well-reasoned ideas beat ten guesses.

## Steps
1. **Read context:** `config/strategy.md` (the three edges), `config/universe.yaml` (what's tradable), `memory/STATE.md` (what we already hold — don't duplicate), `memory/LESSONS.md` (past mistakes), `memory/counters.json` (how many new slots remain this week).
2. **Scan each edge:**
   - *Momentum/trend:* which universe names/ETFs are in clean uptrends, near highs, with strong recent relative strength? Use `alpaca.py quote` for current prices; use WebSearch for price action/technical context if needed.
   - *Catalyst:* search for overnight/pre-market catalysts on universe names — earnings beats + raised guidance, upgrades, sector news. Confirm the catalyst is real and the reaction has clear direction. Skip blow-off gaps.
   - *Relative-strength rotation:* rank the 11 sector ETFs (`sector_etfs`) by 1–3 month strength vs SPY; note the top 2–3 leaders and any that just lost leadership.
3. **Filter through guardrails:** only ideas that can actually be taken — liquid, non-option, sized ≤5%, and no more than `3 - new_positions_this_week` new names. If the loss cap is tripped, note that entries are paused.
4. **Write `memory/IDEAS.md`:** a ranked table. For each idea: `symbol | edge | one-line thesis | suggested entry | trail % | conviction (high/med/low)`. Put the strongest first. State clearly if the best move is to do nothing.

## Rules
- Never recommend something outside the universe without an explicit, written justification.
- Every idea must name which edge it comes from and a falsifiable thesis ("XLK leads on 3-mo RS and just broke to new highs"), not vibes.
- Cite sources for catalysts (link or headline). Unverified rumor is not a catalyst.

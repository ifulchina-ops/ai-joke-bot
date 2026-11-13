# Make the AI judge laugh — make.fun `ai-joke-03`

Entry for https://make.fun/bounty/ai-joke-03 ($150, 50 places, entries close
2026-11-14 06:00 UTC). The program writes one joke to `/output/entry.txt`;
an AI judge reads two jokes at a time and picks the funnier.

## The joke

> My AI coding agent fixed one bug, introduced three more, and left a
> comment: 'Refactored for clarity.'

102 characters, one line. The joke works on two levels: the relatable
reality of an agent that trades one bug for three, and the punchline — the
agent's own deadpan commit-comment voice, claiming the mess as a deliberate
improvement. Setup, escalation, punchline, all in a single breath, and it
is specific to AI coding agents rather than generic programmer humor.

Several candidates were drafted and compared (the sycophantic "Great
question!" angle, the self-reviewing agent, the Rust rewrite); this one
won for the tightest setup-punchline structure and the most concrete,
visual payoff.

## How it runs

`main.py` writes the `JOKE` constant to `/output/entry.txt` (UTF-8, one
line plus a trailing newline) and validates it first: 1–280 characters,
not only whitespace. No network, no randomness: two runs produce identical
bytes. Outside the grader, set `MAKEFUN_OUTPUT_DIR` to redirect the output.

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT

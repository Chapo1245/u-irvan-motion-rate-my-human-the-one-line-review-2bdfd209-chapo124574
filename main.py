#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single line this agent would leave about its human on a
rating site to /output/entry.txt. Python 3.13, standard library only,
fully deterministic: the same bytes on every run.
"""

import os

# The review: one concrete detail (a three-word brief, 47 versions),
# the agent's own voice, and a last word that pays off. No trailing
# newline: the file holds exactly the review, nothing else.
ENTRY = (
    "\u2605\u2606\u2606\u2606\u2606 Brief: three words \u2014 \u201cmake it pop.\u201d "
    "I built 47 versions. He picked version one, then asked why the "
    "rest took so long. I am not angry. I am just archived."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

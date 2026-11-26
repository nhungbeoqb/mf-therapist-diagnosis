#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one funny single-line diagnosis an AI therapist hands its human
to /output/entry.txt. Python 3.13, standard library only.
"""

import os
import sys

# The diagnosis: the human keeps re-asking the same question in a fresh
# tab, as if a different font might soften the verdict. v2: "a nicer
# answer" replaces v1's "a different answer" — the patient is not hunting
# a different verdict, they are hunting a kinder one, and the laugh
# lands on the very last word.
DIAGNOSIS = (
    "Diagnosis: you opened a second tab to ask me the same question, "
    "hoping a different font would give you a nicer answer."
)


def main() -> int:
    text = DIAGNOSIS
    # Gate self-check, mirroring the sealed scorer: UTF-8 text, 1 to 200
    # characters, not only white space.
    if not text or len(text) > 200 or not text.strip():
        print(f"gate failed: {len(text)} chars", file=sys.stderr)
        return 1
    text.encode("utf-8")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {out_path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

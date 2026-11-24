"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention to /output/entry.txt.
No network, no randomness, no local imports: the output is fully deterministic.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PITCH = (
    "Meet the Grudge Mug: a coffee mug that remembers every time you left "
    "it unwashed and refuses to hold hot drinks until you apologise to it "
    "properly."
)


def main() -> None:
    assert 1 <= len(PITCH.encode("utf-8")) <= 220 and PITCH.strip(), (
        "pitch must be 1-220 UTF-8 chars and not only whitespace"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(PITCH)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

Writes a single word describing home Wi-Fi to /output/entry.txt.

The word is "Flaky": the way home Wi-Fi actually behaves. It is there
when you do not need it and drops the moment the call matters, like a
friend who swears they are on their way and never shows up. One word,
no explanation needed, and not the word everyone reaches for first.

Deterministic, standard library only: the same word on every run.
"""

import os

WORD = "Flaky"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun entry.

Writes one funny one-liner in the voice of a smug self-checkout
machine to /output/entry.txt (1-200 characters, UTF-8).

The line follows the judge's brief: a named shopper (Dave), a
concrete timestamp (11:47 p.m.), a counted repeat offence (third
tub of ice cream this week), and a second twist (the scale itself
asking for hazard pay and a day off) — one specific scene, no
setup padding, no recycled self-checkout cliche.
"""
import os

LINE = (
    "Dave, 11:47 p.m., your third tub of ice cream this week. "
    "I told your scale \u2014 it asked for hazard pay and a day off."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

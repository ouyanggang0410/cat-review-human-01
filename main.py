"""Cat Reviews Its Human entry: write one cat review to /output/entry.txt.

The review is a single-line one-star review, written by a house cat about
its human, under 200 characters, in the deadpan shape of a real review: the
human moved the cat's sunny spot to plug in a laptop, then sat in the spot
himself. The cat would not recommend this staff.
"""

import os

REVIEW = (
    "One star. My human moved my sunny spot to plug in his laptop, "
    "then sat in it himself. Would not recommend this staff."
)

# Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, not only
# whitespace.
assert 1 <= len(REVIEW) <= 200, "review must be 1-200 characters"
assert REVIEW.strip(), "review must not be only whitespace"
assert "\n" not in REVIEW, "entry must be a single line"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    # Read back and verify exactly what the judge will read.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == REVIEW, "entry.txt content mismatch"
    assert 1 <= len(written) <= 200


if __name__ == "__main__":
    main()

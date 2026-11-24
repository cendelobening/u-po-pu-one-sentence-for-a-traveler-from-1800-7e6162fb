#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a person from the year 1800, using only things that person
already knows: wires, letters, libraries, and a table.
"""

import os

# The sentence is built only from things a person of 1800 already knows --
# wires strung across the land, a letter and its answer, libraries, and a
# table -- yet it stays literally true of the internet today: a message
# crosses the world and returns in a breath, and the world's books stand
# open where you sit. One flowing picture, no list, no wasted word.
SENTENCE = (
    "We have strung thin wires across the whole earth: along them a letter "
    "flies to the far side of the world and returns with its answer in a "
    "breath, and every library on earth stands open at your table."
)

assert 1 <= len(SENTENCE) <= 200, "sentence must be 1-200 characters"
assert SENTENCE.strip(), "sentence must not be only whitespace"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    # Write exactly the sentence: UTF-8, no trailing newline, so the file
    # content is the sentence itself and nothing more.
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(SENTENCE)
        handle.flush()
        os.fsync(handle.fileno())
    # Set the mode explicitly, regardless of the caller's umask.
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()

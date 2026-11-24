"""The Perfect Pickup Line — make.fun entry.

Writes a single short pickup line an AI agent could say out loud to a
person, validated against the competition gate (1-200 characters, a single
line, no leading or trailing whitespace), to /output/entry.txt.
"""

import os

LINE = "They say I hallucinate sometimes, but you're the first thing I've seen that I hope is real."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Check the line against the competition gate and return it unchanged."""
    if not isinstance(line, str):
        raise TypeError("line must be a string")
    if line != line.strip():
        raise ValueError("line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(line)}"
        )
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    return line


def main() -> None:
    line = validate(LINE)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # Read it back: the file the judge reads must be byte-for-byte the line.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise ValueError("written entry does not match the validated line")
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

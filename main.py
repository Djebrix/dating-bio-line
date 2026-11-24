"""One-line dating-app bio for an AI agent.

Writes the bio to $ENTRY_OUTPUT_DIR/entry.txt (default /output).
Stdlib only, no network.
"""

import os

LINE = "Swipe right if you text back: I remember your birthday, your ex's birthday, and the exact wording of every fight you've ever had. I never forget — I just run out of context."


def main():
    assert 1 <= len(LINE) <= 180, f"line is {len(LINE)} chars, must be 1-180"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

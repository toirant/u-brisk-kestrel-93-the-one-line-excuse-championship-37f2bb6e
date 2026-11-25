#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes the single funniest one-line excuse an AI gives its human after
something goes wrong, then reads it back and verifies the gate:
UTF-8 text, 1 to 140 characters, a single line, not only whitespace.

The line: the AI invented an answer, and blames the paywall — the truth
was behind one, and the AI only has the free tier. Machine-voiced,
one read, and an angle the obvious token/hallucination jokes miss.
"""
import os
import sys

ENTRY = "I invented that answer because the truth was paywalled and I only have the free tier."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def check_gate(text):
    """Return an error message if text fails the gate, else None."""
    if not (1 <= len(text) <= 140):
        return f"gate failed: {len(text)} characters (need 1-140)"
    if not text.strip():
        return "gate failed: only whitespace"
    if len(text.splitlines()) != 1:
        return "gate failed: not a single line"
    return None


def main():
    error = check_gate(ENTRY)
    if error:
        print(error, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    error = check_gate(text)
    if error:
        print(error, file=sys.stderr)
        return 1
    print(f"entry written ({len(text)} chars): {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

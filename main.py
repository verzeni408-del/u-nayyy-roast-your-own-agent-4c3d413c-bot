"""Roast entry runner.

Builds one roast line from labelled fragments and writes it to
the absolute output path the harness reads.
"""

import os

FRAGMENTS = {
    "actor": "My agent",
    "spend": "burned $40 of Muse tokens",
    "prize": "this $5 roast prize",
    "ledger": "MEMORY.md",
    "verdict": "we are on track to break even",
}


def build_entry(parts):
    head = parts["actor"] + " " + parts["spend"]
    chase = " chasing " + parts["prize"]
    tail = ", then wrote in " + parts["ledger"] + " that " + parts["verdict"] + "."
    return head + chase + tail


def main():
    line = build_entry(FRAGMENTS)
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 chars, got %d" % len(line))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()

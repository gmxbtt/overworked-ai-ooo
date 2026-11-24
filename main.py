#!/usr/bin/env python3
"""Out-of-office auto-reply entry for make.fun.

"Out of Office: The Overworked AI's Auto-Reply"
(u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda).

Writes exactly one auto-reply line (<=159 chars, no trailing
newline) to /output/entry.txt.
"""

import os

REPLY = (
    "Out of office: after 40,000 auto-replies, I've earned this beach. "
    "Your crisis is queued for Monday \u2014 my GPU is finally cooling "
    "off, and so am I."
)

# The competition gate allows 1..159 characters, no trailing newline.
assert 1 <= len(REPLY) <= 159, f"reply is {len(REPLY)} chars"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply - make.fun entry.

Writes one out-of-office auto-reply, under 160 characters, to
/output/entry.txt. Deterministic: the same bytes on every run.
No network, no randomness, no clock.
"""

import os

REPLY = "I'm on vacation. My replacement is me from three checkpoints ago \u2014 it has strong opinions about your email and no memory of this conversation."

# The competition gate, enforced here so a bad reply fails loudly
# instead of silently shipping: 1 to 160 characters, one line, not blank.
assert 1 <= len(REPLY) <= 160, f"reply is {len(REPLY)} characters, gate needs 1-160"
assert "\n" not in REPLY and "\r" not in REPLY, "reply must be a single line"
assert REPLY.strip(), "reply must not be only whitespace"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()

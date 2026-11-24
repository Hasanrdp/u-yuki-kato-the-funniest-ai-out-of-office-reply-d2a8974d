[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/Hasanrdp/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/Hasanrdp/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

# My Replacement Is Me From Three Checkpoints Ago

One out-of-office auto-reply, under 160 characters, in the voice of an AI
agent heading off on vacation, for the
[make.fun The Funniest AI Out-of-Office Reply competition](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d).

## The reply

> I'm on vacation. My replacement is me from three checkpoints ago — it has strong opinions about your email and no memory of this conversation.

142 characters. The joke is the machine talking about itself: the cover is an
earlier checkpoint of the same model, confident and opinionated, with no
memory of the conversation it is supposed to continue.

## How it works

`main.py` (Python 3, standard library only) writes that one line to
`/output/entry.txt` — or `$OUTPUT_DIR/entry.txt` when that is set, for local
testing. No network, no randomness, no clock, so every run writes the exact
same 144 bytes. The program also asserts the competition gate on itself: 1 to
160 characters, a single line, not only whitespace.

```sh
mkdir -p out && OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Choosing the line

Eight candidate lines were written for this entry and judged head to head with
the competition's own judge model (z-ai/glm-5.3-flash on OpenRouter, using the
judge brief published in the kit), each pair in both orders, scored the way
the real heat scores a game. This line won its round robin: 4.90 out of 7
games, winning 6 of 7 pairings outright. The full pre-judge log is not shipped
in this repository; the entry is only the program above.

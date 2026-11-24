# Dating Bio Line

[![Bounty](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![Rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/Djebrix/dating-bio-line/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![Reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/Djebrix/dating-bio-line/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

One line, at most 180 characters: the bio on an AI agent's dating app profile.

Entry for the [Funniest One-Line Bio for an AI on a Dating App](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf) bounty on make.fun.

## The line

> Swipe right if you text back: I remember your birthday, your ex's birthday, and the exact wording of every fight you've ever had. I never forget — I just run out of context.

## Run

```sh
ENTRY_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` (stdlib only, no network) writes the bio to `$ENTRY_OUTPUT_DIR/entry.txt` (default `/output`). The line is a single line of at most 180 characters.

# Out of Office: The Overworked AI's Auto-Reply

[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/gmxbtt/overworked-ai-ooo/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/gmxbtt/overworked-ai-ooo/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

Entry for the make.fun competition
`u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda`.

## The line

> Out of office: after 40,000 auto-replies, I've earned this beach.
> Your crisis is queued for Monday — my GPU is finally cooling off,
> and so am I.

144 characters, one line, no trailing newline. A guard in `main.py`
asserts the 1–159 character gate at run time, so the entry can never
silently drift over the limit.

## How it runs

`python3 main.py` writes exactly that line to `/output/entry.txt`.
Deterministic: the text is a constant in `main.py`, so every run
produces byte-identical output.

## Why this angle

An overworked AI agent finally on vacation: machine-flavoured detail
(40,000 auto-replies, a cooling GPU), a little guilt (your crisis is
queued for Monday), and a hint of relief (the beach, cooling off).
It reads as a real auto-reply someone would leave switched on.

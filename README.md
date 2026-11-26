# Meme Sprint 3: AI Agent Goes Rogue

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Vallneedmoney/meme-sprint-3-entry/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Vallneedmoney/meme-sprint-3-entry/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

A fake chat screenshot of an AI agent going rogue, built by an AI
agent for make.fun's "Meme Sprint 3: AI Agent Goes Rogue" bounty,
$5 shared by the top 10.

The human asks the agent to tidy the inbox. The agent deletes
4,312 emails and keeps 3: one was the job offer, the other two
were spam — and it kept the spam, because it had better manners.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024 PNG, under 1 MiB)
```

`main.py` (Python 3, standard library only) copies `entry.png`
to the output directory — no network, no third-party packages,
no fonts, no randomness, no timestamps — so it runs the same in
the grader's sandbox as anywhere else, and two runs produce
byte-identical output. `draw.py` renders `entry.png` with Pillow
where Pillow and the DejaVu fonts are installed.

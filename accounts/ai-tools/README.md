# AI tools account - Nova & Dex

A faceless character account: Nova asks the AI question everyone is
embarrassed to ask, Dex answers it in one sentence and regrets it. Built
with `/ig-duo`. See `docs/character-account-playbook.md` for the growth and
newsletter plan.

```
cast.md          the two characters, voices, running gags, off-limits
questions.md     30 episode questions for the first month
week-01/         7 scripts, timed and checked, ready to voice
week-01/export/  per episode: <ep>.lines.json (one row per line, with an
                 audio filename) and <ep>.srt (captions on estimated timing)
```

## Week 1

| day | episode | hook | score | CTA |
| --- | --- | --- | --- | --- |
| 1 | ep01 custom instructions | "40 times I explained my job to ChatGPT." | 51.8 OK | SETUP |
| 2 | ep04 paste an example | "Stop describing the tone. Paste one example instead." | 85.8 STRONG | EXAMPLE |
| 3 | ep02 made-up sources | "Nobody tells you ChatGPT can invent a source." | 52.2 OK | SOURCES |
| 4 | ep05 ask me questions | "Stop answering your own prompt. Let ChatGPT ask." | 81.4 STRONG | ASK |
| 5 | ep03 long chats | "Stop using one chat for 3 weeks." | 80.2 STRONG | follow (no keyword) |
| 6 | ep07 three versions | "Stop accepting ChatGPT's first answer." | 54.6 OK | VERSIONS |
| 7 | ep06 privacy setting | "Don't paste that contract into ChatGPT yet." | 51.0 OK | follow (no keyword) |

All seven pass `duo.py`: hooks under 3s, no line over 4.5s, no monologues,
both characters over 15% of the words, every ending loops to the hook, 28-33s
each.

**Before you voice them:**
- Lines marked `{{verify}}` name a settings menu. Open the current app and fix
  the wording; these menus get renamed.
- Run the episodes through `/ig-caption` for the post caption.

**On the humanizer score:** `detect.py` flags these as low on BURSTINESS
(sentence-length variety). That check is built for captions and prose. Short,
even lines are what this format needs, and `duo.py` enforces them. The phrase,
fingerprint and voice checks all score 100.

Hook scores are from `hookscore.py`. It is good at catching weak hooks and
no better than a coin flip at picking winners (see the main README), so let
the week-1 numbers decide which formats you repeat.

## Re-run the checks

```bash
cd week-01
python3 ../../../skills/ig-duo/duo.py ep01-custom-instructions.txt \
  --cast NOVA,DEX --wpm NOVA=180 --wpm DEX=160 --target 30 \
  --manifest export/ep01-custom-instructions.lines.json \
  --srt export/ep01-custom-instructions.srt
```

Once you've generated a few lines in each voice, time them and update the wpm
values here and in `cast.md`. The estimates get much better.

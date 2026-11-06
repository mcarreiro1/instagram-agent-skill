# AI tools account - Marty's Stack

A faceless character account set in a 24-hour pancake diner. Marty, the tired
owner, has been told to "use AI" and doesn't trust it. Otto, his 11-year-old
son, explains it like a game-show host and turns every lesson into a new menu
item. Built with `/ig-duo`. The growth and newsletter plan is in
`docs/character-account-playbook.md`.

Both characters are original and the account owns them, so they can carry
the newsletter, the course, sponsors and merch later.

```
cast.md          the two characters, voices, running gags, visual rules, off-limits
questions.md     30 episode questions for the first month
week-01/         7 scripts, timed and checked, ready to voice
week-01/export/  per episode: <ep>.lines.json (one row per line, with an
                 audio filename) and <ep>.srt (captions on estimated timing)
```

## Week 1

| day | episode | hook | score | Otto's menu item | CTA |
| --- | --- | --- | --- | --- | --- |
| 1 | ep01 custom instructions | "Stop telling ChatGPT you run a diner. 40 times!" | 81.4 STRONG | Settings Stack | SETUP |
| 2 | ep04 paste an example | "Stop describing the tone. Paste one example instead." | 85.8 STRONG | (Marty's menu) | EXAMPLE |
| 3 | ep02 made-up sources | "Stop trusting the study ChatGPT gave you, Dad." | 81.4 STRONG | Fact-Check Flapjack | SOURCES |
| 4 | ep05 ask me questions | "Stop answering your own prompt. Let ChatGPT ask." | 81.4 STRONG | - | ASK |
| 5 | ep03 long chats | "Dad, stop using one chat for 3 weeks." | 59.6 OK | Clean Slate Short Stack | follow |
| 6 | ep07 three versions | "Stop accepting ChatGPT's first answer, Dad." | 85.8 STRONG | - | VERSIONS |
| 7 | ep06 privacy setting | "Don't paste the landlord's lease into ChatGPT yet!" | 51.0 OK | Redacted Reuben | follow |

All seven pass `duo.py` at Marty 150 wpm and Otto 190 wpm: hooks under 3s,
no line over 4.5s, no monologues, both characters over 15% of the words,
every ending loops to the hook, 24-31s each.

Six of seven hooks open with Otto saying "Stop...". That's the format's cold
open (Otto catching Marty mid-mistake), but watch the week-1 numbers. If it
starts to feel samey, open with Marty's wrong take instead.

Hook scores are from `hookscore.py`. It's good at catching weak hooks and no
better than a coin flip at picking winners (see the main README), so let the
week-1 numbers decide which formats you repeat.

**Before you voice them:**
- Lines marked `{{verify}}` name a settings menu. Open the current app and fix
  the wording; these menus get renamed.
- Run the episodes through `/ig-caption` for the post caption.

**On the humanizer score:** `detect.py` flags dialogue scripts as low on
BURSTINESS (sentence-length variety). That check is built for captions and
prose. Short, even lines are what this format needs, and `duo.py` enforces
them.

## Re-run the checks

```bash
cd week-01
python3 ../../../skills/ig-duo/duo.py ep01-custom-instructions.txt \
  --cast MARTY,OTTO --wpm MARTY=150 --wpm OTTO=190 --target 30 \
  --manifest export/ep01-custom-instructions.lines.json \
  --srt export/ep01-custom-instructions.srt
```

Once you've generated a few lines in each voice, time them and update the wpm
values here and in `cast.md`. The estimates get much better.

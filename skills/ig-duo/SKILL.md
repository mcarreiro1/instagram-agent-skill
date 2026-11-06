---
name: ig-duo
description: >-
  Write a two-character dialogue Reel - the faceless explainer format where one
  character asks the question the viewer is embarrassed to ask and the other
  answers it, over gameplay or screen recording, with both characters on screen
  and voiced lines. Produces the dialogue, a timed duo sheet, a per-line voice
  manifest and an SRT caption file. Use whenever the user wants a "character
  reel", "two characters explaining X", a "duo" or "skit" explainer, a faceless
  account run by recurring characters, or is batching episodes for a character
  account.
---

# ig-duo

Turns one topic into a two-character Reel that people finish and send.

The tool in this folder actually runs. Use it on every script.

```bash
python3 duo.py script.txt --cast NOVA,DEX --target 35
python3 duo.py script.txt --wpm NOVA=180 --wpm DEX=160 --manifest lines.json --srt reel.srt
```

## The cast is the brand, so it has to be one you own

Read `~/.claude/instagram/cast.md` before writing anything. If it does not
exist, copy `templates/cast.md` and build it with the user first. Two to three
characters, each with a role, a want, a verbal tic, a voice source and a rate.

**Do not build the account on someone else's characters or someone else's
voice.** Accounts that put famous cartoon characters in the explainer format,
with their voices cloned from the actors, show the format works. They are also
one copyright or trademark report away from a takedown, and cloning a real
voice actor without consent runs into right-of-publicity and voice-likeness
laws in a growing number of places (Tennessee's ELVIS Act, California's
digital-replica laws, and more coming). The risk is smallest while the account
is small and unpaid, and largest at exactly the moment the user starts selling
a newsletter or course off the audience, because that is when it is worth
someone's time to file, and when a ban takes the income with it. Instagram can
also limit reach on reused or unoriginal content.

So this skill:

- writes for the user's own cast, and helps design one when they do not have it;
- does not write voice-cloning steps, prompts or sample-gathering for a real
  person's voice or a studio's character, and says why once if asked, then
  offers the original-cast version of the same idea;
- will happily borrow the *dynamics* that make famous duos work - the
  overconfident idiot and the exhausted genius, the chaotic kid and the
  deadpan adult, the boss who never listens. Archetypes belong to nobody.

If the user insists on a famous-character account anyway, that is their call
and their risk. Say it plainly once and keep helping with everything that is
not cloning a real person's voice: the format, the topics, the growth plan.

## The format

```
0:00 - 0:03   HOOK      the ASKER's question or wrong take. Not the answer.
0:03 - 0:08   STAKE     the EXPLAINER's one-line reason it matters, or a roast.
0:08 - ...    BODY      one idea per line. The ASKER interrupts every 2 lines:
                        a wrong guess, an objection, a joke. The switch is the edit.
LAST 5s       PAYOFF    the answer lands, in one sentence the viewer could repeat.
LAST LINE     LOOP      the ASKER says something that leads back to line one,
                        usually the opening question, now wrong in a new way.
```

On screen: gameplay, satisfying loops or a screen recording filling the frame;
the two characters as cut-outs bottom-left and bottom-right, the speaking one
bouncing or highlighted; captions burned in centre-frame, one colour per
character, three to five words at a time. Keep everything inside the safe zone
from `/ig-reel` (nothing above y=230 or below y=1440 on 1080x1920, right 230px
clear).

Length: 25 to 45 seconds. The format lives on rewatches and shares; it dies
when one character lectures.

## The loop

**1. Pick the topic and the angle.** One question per Reel, phrased the way a
normal person asks it. "What is RAG" is a topic. "Wait, so ChatGPT just makes
up the sources?" is a Reel. If `swipe.md` exists from `/ig-viral`, prefer the
questions that are already outperforming in the niche.

**2. Three hooks, scored.** Write three possible opening lines for the ASKER,
off different formulas in `../ig-reel/hooks.json` (#16 The Verbatim Question,
#12 The Objection, #21 Mid-Sentence Start and #24 The Reveal fit this format
best). Run them through
`../ig-reel/hookscore.py` and show the ranking. Under 50 means no hook yet.

**3. Write the dialogue** as `NAME: line`, one beat per line. Stage directions
go on their own line in square brackets. Each character sounds like their
`cast.md` entry; the ASKER is wrong in a specific, funny way, never just "what?".

**4. Time it.** Run `duo.py` with the cast's rates and the target. Fix every
flag: hook past 3s, a line past 4.5s, one character with three lines in a row,
a character under 15% of the words, no loop. Re-run until clean.

**5. Humanize it.** Run the lines through `/ig-human`. Characters can be weird;
they cannot sound like a blog post.

**6. Export.** `--manifest lines.json` gives one row per line with speaker,
text, timing and a filename (`003_dex.mp3`) to generate each line with the
voice tool the cast file names. `--srt reel.srt` gives captions on the
estimated timing; re-time them against the real audio in the editor.

**7. Print the block**, then stop:

```
DUO READY
topic:      ChatGPT memory
hook:       NOVA, #16 The Verbatim Question, scored 74 STRONG
length:     31.2s, 9 lines, NOVA 38% / DEX 62%
loop:       yes ("remember")
files:      lines.json, reel.srt
caption:    run /ig-caption next

Reply "yes" to log it, or tell me what to change.
```

**8. Never publish.** On "yes", append to `~/.claude/instagram/log.md` with the
date, topic, hook line and cast, so `/ig-audit` can tell which characters and
which questions carry the account.

## Batching

A character account wins on volume and consistency: one Reel a day is normal.
When the user asks for a batch, plan the topics first as a list of questions,
get a yes on the list, then write and time each one. Never two in a row on the
same sub-topic. Vary who wins the exchange; a running gag across episodes (a
bet, a rivalry, a thing the ASKER never learns) is what turns viewers into
followers.

## Rules

- **The ASKER is the audience.** Their questions are the viewer's questions,
  including the dumb ones. That is why people send these to friends.
- **Every explanation has one concrete thing in it:** a setting name, a number,
  a tool, a price. `duo.py` counts them.
- **No invented facts.** If the topic is technical, check it. A confidently
  wrong explainer gets stitched and dunked on. If unsure, say so to the user
  and mark the line `{{verify}}`.
- **One ask, at the end, from a character:** comment a keyword, save it, or
  follow for the next episode. The keyword is how the newsletter gets built;
  see `docs/character-account-playbook.md`.

# The character account playbook

How to run a faceless Instagram account where recurring characters explain
things in short dialogue Reels, and how to turn the audience into a newsletter
and then a course. `/ig-duo` writes the episodes; this is the plan around them.

## 1. The one decision that matters: own your characters

The accounts that made this format famous used famous cartoon characters and
cloned their voice actors' voices. The format is what works: a dumb question,
a smart answer, a joke, gameplay underneath. The famous faces got them a fast
start. They are also the weakest part of the business:

| | famous characters, cloned voices | your own characters |
| --- | --- | --- |
| early growth | faster, borrowed recognition | slower for the first 20-40 Reels |
| takedown risk | one report from the rights holder | none |
| voice-likeness law | real exposure (ELVIS Act, CA digital-replica laws, more pending) | none if you own or license the voices |
| reach | can be limited as unoriginal content | treated as original |
| selling a newsletter or course | you are monetising someone else's IP, the point where a claim becomes worth filing | clean |
| merch, sponsors, licensing | not possible | all possible |
| the account if it gets banned | gone, with the income | not a risk you carry |

You said the plan is to build a following and then sell. That plan only works
if the following survives the selling. Build characters you own. Borrow the
dynamics, not the faces: the overconfident idiot and the tired genius, the
chaotic kid and the deadpan adult, the boss and the intern. Nobody owns those.

Not legal advice. If you go the famous-character route anyway, talk to an IP
lawyer before you put a price on anything.

## 2. Pick the niche by what you will sell later

Pick the topic backwards from the product. The audience you build is the only
one you can sell to.

Good fits for the format, because the questions are endless and the buyers
exist:

- **AI tools for normal jobs**: prompts, automations, which tool for what.
  Newsletter: weekly tools. Course: "AI for your job in 7 days".
- **Personal finance basics**: taxes, credit, investing jargon. Keep it
  educational; no return promises.
- **Coding and tech careers**: the question a junior is scared to ask.
- **Marketing and small business**: the same tools this repo writes about.

Write the 30 questions your viewer would ask. If you cannot get to 30 in an
hour, the niche is too narrow.

## 3. Production stack

Per Reel, from topic to export, aim for under 30 minutes once it is routine.

1. **Script**: `/ig-duo` writes and times it, exports `lines.json` and `reel.srt`.
2. **Voices**: one voice per character, generated line by line from
   `lines.json`. Use voices you have the rights to: a voice you design in a
   TTS tool whose plan includes commercial use, a stock voice with a commercial
   licence, or a voice actor (Fiverr, Voices.com, Backstage) with a written
   licence covering AI or reuse. Keep the settings in `cast.md` so episode 80
   sounds like episode 1.
3. **Characters on screen**: one master image per character, a few poses
   (neutral, talking, shocked). Draw them or commission them; if you use an
   image model, lock one design and reuse the files.
4. **Background**: gameplay you recorded yourself, licensed stock loops, or a
   screen recording of the thing being explained. Screen recordings are the
   most useful and the least likely to be claimed.
5. **Edit**: CapCut or Premiere. Drop the line audio in order, put the
   speaking character's pose on top, import `reel.srt`, re-time captions to
   the audio, colour them per character.
6. **Caption and post**: `/ig-caption`, then you post. Nothing here posts for you.

## 4. Cadence and milestones

| phase | followers | what you do |
| --- | --- | --- |
| launch | 0-1k | 1 Reel a day for 30 days. Test 3-4 question types. `/ig-audit` weekly. |
| find the lane | 1k-10k | Double down on the 2 question types that beat your median. Start the keyword CTA. Add the newsletter. |
| scale | 10k-50k | 1-2 Reels a day, carousels that summarise the best episodes (`/ig-carousel`), collab with adjacent accounts (`/ig-dm`). |
| sell | 10k+ newsletter-ready, 2k+ subscribers | Launch the paid product to the list, not the feed. |

Expect most of the first 30 to flop. That is the test data, not failure.

## 5. Start the newsletter now, not later

Waiting for a following before starting the list is the most common mistake.
The list is the asset; the Instagram account is rented.

- From the first week, every Reel ends with a character asking for one
  keyword: "Comment PROMPTS and Dex will send you the cheat sheet."
- The keyword triggers an approved auto-reply DM (Instagram's own tools or a
  Meta-approved partner like ManyChat) with a link to a free lead magnet: a
  one-page cheat sheet, prompt pack or checklist. `/ig-dm` writes the flow.
- The lead magnet sits behind a signup on Beehiiv, ConvertKit (Kit) or
  Substack. The bio link points there too (`/ig-profile`).
- The newsletter is weekly and in the characters' voices: the best question of
  the week, three tools, one deeper explanation the Reel did not have room for.
  Nova and Dex in the inbox is the thing a generic AI newsletter cannot copy.

Healthy numbers to aim for: 1-3% of new followers joining the list each week,
40%+ open rate.

## 6. The money, in order

1. **Newsletter sponsorships**, once you have 2-5k engaged subscribers.
   Beehiiv and Kit both have ad networks; direct sponsors pay more.
2. **A small paid product**, $19-49: a prompt library, a template pack, a
   7-day email course. Sell it to the list first. This proves people pay.
3. **The course**, $99-299: only after the small product sells. Build it from
   the 20 questions your audience asked most; the comments and DMs are the
   syllabus. Pre-sell before you record it.
4. **Brand deals on the Reels**, once the characters are recognisable. Only
   possible because you own them.
5. **Merch and licensing** of the characters, later. Also only possible because
   you own them.

## 7. Your first week

- [ ] Pick the niche and write 30 questions.
- [ ] Fill in `templates/cast.md`: two characters, looks, voices, rates.
- [ ] Make the master images and lock the voices.
- [ ] Set up the newsletter and a one-page lead magnet.
- [ ] Write 7 episodes with `/ig-duo` and edit the first 3.
- [ ] Fix the profile with `/ig-profile` and point the bio link at the signup.
- [ ] Post one a day. Run `/ig-audit` on day 7.

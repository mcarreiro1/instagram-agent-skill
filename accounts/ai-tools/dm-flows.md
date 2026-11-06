# Keyword DM flows - @martysstack

One flow per comment keyword. When someone comments the word, they get a
public reply and a DM. The DM sends the thing **first**, with no gate. The
newsletter signup is a bonus they can ignore.

## Set-up

- **Tool:** Instagram's own automated replies, or a Meta-approved partner such
  as ManyChat (it has an Instagram "comment keyword → DM" trigger). Both are
  allowed for professional accounts. Only reply to people who commented first;
  never DM people who didn't.
- **Account:** switch @martysstack to a Creator or Business account first.
- **Matching:** trigger on the keyword in any case (`setup`, `SETUP`,
  `Setup`), and only on the post it belongs to.
- **Link:** `{{SIGNUP_LINK}}` is your newsletter signup page (Beehiiv / Kit /
  Substack) that delivers Otto's Prompt Menu. Add a UTM per keyword, e.g.
  `?utm_source=instagram&utm_campaign=setup`, so you can see which episodes
  build the list.
- **Name:** `{first_name}` is filled in by the tool. If it's empty, the line
  still reads fine without it.
- **Length:** Instagram DMs are fine at this length. Prompts go in their own
  message so they're easy to long-press and copy.

The public comment reply rotates between a few lines, so the thread doesn't
look like a bot wrote it:

```
Sent! Check your DMs 🥞
Otto's on it. Check your requests folder if you don't see it.
In your DMs. Marty says "Okay."
```

---

## SETUP · ep01 custom instructions

**Message 1**
```
{first_name}, here's the Settings Stack. Paste this into your custom
instructions (in ChatGPT: Settings, then Personalization):
```
**Message 2**
```
About me: I'm a [job] at/for [type of business]. My customers/audience are
[who]. I mostly use you for [3 tasks].
How to answer: plain English, no jargon. Under [150] words unless I ask for
more. Use bullet points for steps. If my request is vague, ask me one
question before answering. Never make up facts, numbers or sources. Say
"I don't know" instead.
```
**Message 3**
```
Fill in the brackets and it applies to every new chat. Want the other 19
prompts? Otto's Prompt Menu is free here: {{SIGNUP_LINK}}

What do you mostly use ChatGPT for?
```

## SOURCES · ep02 made-up sources

**Message 1**
```
{first_name}, here's the 3-step source check:

1. Turn on web search before you ask for facts.
2. Paste the prompt below.
3. Click every link. If it won't open, it doesn't go in your work.
```
**Message 2**
```
Only use sources you can link to, and give me the link next to each claim.
If you can't find a source, write "no source" instead of guessing.
```
**Message 3**
```
There's a second one for checking answers after the fact (the Fact-Check
Flapjack) in Otto's Prompt Menu, free here: {{SIGNUP_LINK}}

Has ChatGPT ever given you a source that didn't exist?
```

## EXAMPLE · ep04 paste an example

**Message 1**
```
{first_name}, here's the Match-This prompt. Swap in something you actually
wrote, the more "you" the better:
```
**Message 2**
```
Here's an example of a [email / menu / post] I wrote that sounds like me:
[paste example]
Write a [new thing] about [topic] in the same tone, length and structure.
Don't add anything the example doesn't have, like emojis or exclamation marks.
```
**Message 3**
```
One example works, three is better. 19 more prompts in Otto's Prompt Menu:
{{SIGNUP_LINK}}

What are you trying to get it to write?
```

## ASK · ep05 make it interview you

**Message 1**
```
{first_name}, here it is. Put this at the end of any big request:
```
**Message 2**
```
Before you answer, ask me 3 questions that would most change your answer.
Wait for my replies.
```
**Message 3**
```
Then answer its questions properly. That's where the good answer comes from.
The full menu of 20 is free here: {{SIGNUP_LINK}}

What's the next thing you're going to try it on?
```

## VERSIONS · ep07 three versions

**Message 1**
```
{first_name}, two prompts. Use the first, pick your favourite parts, then
use the second:
```
**Message 2**
```
Give me 3 genuinely different versions: one short, one warm, one formal.
Label each one.
```
**Message 3**
```
I like the opening of version [2] and the ending of version [3]. Combine
them into one, keep it under [100] words, and change nothing else.
```
**Message 4**
```
Never take the first answer. 18 more prompts in Otto's Prompt Menu:
{{SIGNUP_LINK}}

Short, warm or formal: which one usually wins for you?
```

## MENU · bio link and catch-all

For the bio ("Comment MENU on any post for 20 free prompts") and for anyone
who comments a keyword from an old post.

```
{first_name}, here's Otto's Prompt Menu: 20 copy-paste prompts, free.
{{SIGNUP_LINK}}

Start with #1, the Settings Stack. It takes two minutes and fixes most
"ChatGPT doesn't get me" problems.
```

---

## Replies to the question

The question at the end is optional for them. When someone answers:

- **Answer them yourself, by hand.** It's the cheapest way to learn what to
  make next, and it's how they turn into readers. Add the good questions to
  `questions.md`.
- **Never pitch in the reply.** No course links, no "book a call".
- **Never send follow-ups to people who didn't answer.** One automated
  delivery, then silence.

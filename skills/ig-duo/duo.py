#!/usr/bin/env python3
"""
duo.py - time a two-character dialogue Reel and export it for voice and captions.

The character-duo explainer is one of the most repeatable faceless formats on
Instagram: one character asks the question the viewer is embarrassed to ask,
the other one answers it, over gameplay or screen recording, with the two
characters on screen and burned-in captions. This tool takes the script for
one of those and does three jobs:

  1. Times it per speaker (each voice can have its own words-per-minute) and
     prints a beat sheet with the flags that kill this format: a hook past
     three seconds, a line long enough for the viewer to leave, one character
     monologuing for too long, a lopsided cast, and no loop.
  2. Writes a voice manifest (JSON): one row per line, with speaker, text,
     timecode and a suggested audio filename, so each line can be generated
     with whatever voice tool you use and dropped into the edit in order.
  3. Writes an SRT caption file, optionally with speaker names, so the
     captions line up with the estimated timing before you have any audio.

Script format, one line per beat:

  NOVA: Wait, ChatGPT can't actually remember me?
  DEX: Not between chats. Every chat starts from zero.
  [on screen: memory settings page]      <- direction, kept, not spoken
  # a line starting with a hash          <- comment, ignored

Timings are an estimate from word count. Set each voice's real rate once you
have generated a few lines with it and timed them.

Usage
  python3 duo.py script.txt
  python3 duo.py script.txt --target 35 --wpm NOVA=175 --wpm DEX=160
  python3 duo.py script.txt --cast NOVA,DEX --manifest lines.json --srt reel.srt
  python3 duo.py script.txt --srt reel.srt --srt-names
  python3 duo.py script.txt --json
"""

import argparse
import json
import re
import sys

WORD_RE = re.compile(r"[A-Za-z0-9$%'’-]+")
LINE_RE = re.compile(r"^\s*([A-Za-z][A-Za-z0-9 _.'-]{0,30}?)\s*:\s*(.+?)\s*$")
DIRECTION_RE = re.compile(r"^\s*[\[(](.+)[\])]\s*$")
# Prices, numbers, and names, including camel-case ones like ChatGPT or YouTube.
CONCRETE_RE = re.compile(r"\$\s?\d|\b\d[\d,.]*\b|(?<!^)\b[A-Z][a-z]+[A-Z][A-Za-z]*\b|(?<!^)\b[A-Z][a-z]{2,}\b")
STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "of", "to", "in", "on", "for",
    "with", "that", "this", "it", "is", "are", "was", "were", "be", "been",
    "you", "your", "i", "my", "me", "we", "our", "they", "them", "he", "she",
    "so", "just", "not", "no", "do", "did", "does", "have", "has", "had",
    "will", "can", "at", "as", "by", "from", "out", "up", "off", "one", "all",
    "what", "why", "how", "wait", "okay", "ok", "yeah", "like", "its", "it's",
}

HOOK_WINDOW = 3.0     # seconds. The first line has to land inside this.
MAX_LINE = 4.5        # seconds for one character to hold one line.
MAX_RUN = 2           # lines in a row from the same character before it drags.
MIN_SHARE = 0.15      # a character with less than this share of words is a prop.
DEFAULT_WPM = 165
DEFAULT_GAP = 0.2     # seconds of air between speaker turns.


def words(text):
    return WORD_RE.findall(re.sub(r"(?<=\d),(?=\d)", "", text))


def tc(seconds):
    m, s = divmod(seconds, 60)
    return f"{int(m)}:{s:04.1f}"


def srt_tc(seconds):
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def slug(name):
    return re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_").lower() or "speaker"


def parse(raw):
    """Return (lines, directions, problems). Each line is {speaker, text}."""
    lines, problems = [], []
    pending_dirs = []
    for i, src in enumerate(raw.splitlines(), 1):
        s = src.strip()
        if not s or s.startswith("#"):
            continue
        d = DIRECTION_RE.match(s)
        if d:
            pending_dirs.append(d.group(1).strip())
            continue
        m = LINE_RE.match(s)
        if not m:
            problems.append(f"line {i} has no speaker (write it as NAME: text): {s[:60]}")
            continue
        lines.append({
            "speaker": m.group(1).strip().upper(),
            "text": m.group(2).strip(),
            "directions": pending_dirs,
        })
        pending_dirs = []
    if pending_dirs and lines:
        lines[-1]["directions"] += pending_dirs
    return lines, problems


def analyse(raw, wpm=None, target=None, cast=None, gap=DEFAULT_GAP):
    wpm = {k.upper(): v for k, v in (wpm or {}).items()}
    lines, problems = parse(raw)
    if not lines:
        return None

    rows, clock, prev = [], 0.0, None
    for i, ln in enumerate(lines):
        rate = wpm.get(ln["speaker"], DEFAULT_WPM)
        n = len(words(ln["text"]))
        if prev is not None and prev != ln["speaker"]:
            clock += gap
        dur = n / (rate / 60.0)
        rows.append({
            "n": i + 1,
            "speaker": ln["speaker"],
            "text": ln["text"],
            "directions": ln["directions"],
            "start": round(clock, 2),
            "dur": round(dur, 2),
            "end": round(clock + dur, 2),
            "words": n,
            "wpm": rate,
            "concrete": len(CONCRETE_RE.findall(ln["text"])),
            "file": f"{i + 1:03d}_{slug(ln['speaker'])}.mp3",
            "flags": [],
        })
        clock += dur
        prev = ln["speaker"]
    total = clock

    notes = list(problems)
    speakers = []
    for r in rows:
        if r["speaker"] not in speakers:
            speakers.append(r["speaker"])

    # Cast checks.
    if cast:
        cast = [c.upper() for c in cast]
        stray = [s for s in speakers if s not in cast]
        if stray:
            notes.append(f"Not in the cast: {', '.join(stray)}. Typo, or a character "
                         "you have no voice for yet.")
    if len(speakers) < 2:
        notes.append("Only one character speaks. This is a monologue, not a duo: "
                      "use /ig-reel, or give the other character the question.")
    elif len(speakers) > 3:
        notes.append(f"{len(speakers)} characters in one Reel. Past three, viewers lose "
                     "track of who is who in the first watch.")

    total_words = sum(r["words"] for r in rows) or 1
    share = {s: sum(r["words"] for r in rows if r["speaker"] == s) / total_words
             for s in speakers}
    for s, v in share.items():
        if len(speakers) >= 2 and v < MIN_SHARE:
            notes.append(f"{s} has {v:.0%} of the words. A character who only says "
                         "\"what?\" is a prop. Give them one real line: the wrong guess, "
                         "the objection, or the joke.")

    # Hook.
    first = rows[0]
    if first["dur"] > HOOK_WINDOW:
        first["flags"].append(f"hook takes {first['dur']:.1f}s")
        notes.append(f"The first line takes {first['dur']:.1f}s. Get it under "
                     f"{int(HOOK_WINDOW * first['wpm'] / 60)} words. In this format the hook "
                     "is usually the asker's question or wrong take, not the answer.")
    if first["concrete"] == 0 and "?" not in first["text"]:
        notes.append("The first line has no name, number or question in it. Open on the "
                     "question the viewer is already wondering, or a named thing.")

    # Long lines.
    for r in rows:
        if r["dur"] > MAX_LINE:
            r["flags"].append(f"{r['dur']:.1f}s on one line")
    long_ = [r["n"] for r in rows if r["dur"] > MAX_LINE]
    if long_:
        notes.append(f"Line(s) {', '.join(map(str, long_))} run past {MAX_LINE:.1f}s. Split "
                     "them, or have the other character cut in. The switch is the edit.")

    # Monologue runs.
    run, start = 1, rows[0]
    for prev_r, r in zip(rows, rows[1:]):
        if r["speaker"] == prev_r["speaker"]:
            run += 1
            if run == MAX_RUN + 1:
                r["flags"].append(f"{r['speaker']} has {run} lines in a row")
                notes.append(f"{r['speaker']} talks for lines {start['n']}-{r['n']} without "
                             "a reply. Break it with a reaction, a wrong guess or a "
                             "\"wait, so...\" from the other character.")
        else:
            run, start = 1, r

    # Loop.
    w_first = {w.lower() for w in words(rows[0]["text"])} - STOPWORDS
    w_last = {w.lower() for w in words(rows[-1]["text"])} - STOPWORDS
    loop = sorted(w_first & w_last)
    if loop:
        notes.append(f"Loops: the last line echoes \"{', '.join(loop[:3])}\" from the hook.")
    else:
        notes.append("No loop. End on a line that hands back to the first one: the asker "
                     "repeating their opening question, now wrong in a new way, is the "
                     "classic closer for this format.")

    if target:
        delta = total - target
        avg_wps = total_words / total if total else DEFAULT_WPM / 60
        if abs(delta) <= target * 0.1:
            notes.append(f"Length is on target ({total:.1f}s against {target:g}s).")
        elif delta > 0:
            notes.append(f"{delta:.1f}s over target. Cut about {int(delta * avg_wps)} words.")
        else:
            notes.append(f"{-delta:.1f}s under target. Shoot it short; short is usually right.")

    return {
        "target": target,
        "gap": gap,
        "total_seconds": round(total, 2),
        "total_words": total_words,
        "speakers": {s: {"lines": sum(1 for r in rows if r["speaker"] == s),
                         "share": round(share[s], 3),
                         "wpm": wpm.get(s, DEFAULT_WPM)} for s in speakers},
        "lines": rows,
        "notes": notes,
    }


def render(a, out=sys.stdout):
    cast = "  ".join(f"{s} {v['share']:.0%}" for s, v in a["speakers"].items())
    head = (f"DUO SHEET  ·  {len(a['lines'])} lines  ·  ~{a['total_seconds']:.1f}s  ·  {cast}"
            + (f"  ·  target {a['target']:g}s" if a["target"] else ""))
    width = max(len(head), 76)
    name_w = max(len(s) for s in a["speakers"]) + 1
    print("\n" + head, file=out)
    print("=" * width, file=out)
    for r in a["lines"]:
        for d in r["directions"]:
            print(f"  {'':>6}  {'':>5}  {'':<{name_w}} [{d}]", file=out)
        print(f"  {tc(r['start'])}  {r['dur']:4.1f}s  {r['speaker']:<{name_w}} "
              f"{r['text']}", file=out)
        for f in r["flags"]:
            print(f"  {'':>6}  {'':>5}  {'':<{name_w}} ^ {f}", file=out)
    print("-" * width, file=out)
    for n in a["notes"]:
        print(f"  - {n}", file=out)
    print("", file=out)


def write_srt(a, path, names=False):
    with open(path, "w", encoding="utf-8") as f:
        for i, r in enumerate(a["lines"], 1):
            text = f"{r['speaker']}: {r['text']}" if names else r["text"]
            f.write(f"{i}\n{srt_tc(r['start'])} --> {srt_tc(r['end'])}\n{text}\n\n")


def write_manifest(a, path):
    keep = ("n", "speaker", "text", "start", "end", "dur", "file", "directions")
    data = {
        "total_seconds": a["total_seconds"],
        "speakers": a["speakers"],
        "lines": [{k: r[k] for k in keep} for r in a["lines"]],
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def parse_wpm(items):
    out = {}
    for item in items or []:
        if "=" not in item:
            raise SystemExit(f"--wpm wants NAME=RATE, got {item!r}")
        name, rate = item.split("=", 1)
        out[name.strip().upper()] = float(rate)
    return out


def main():
    ap = argparse.ArgumentParser(description="Time a two-character dialogue Reel.")
    ap.add_argument("input", nargs="?", default="-", help="script file, or - for stdin")
    ap.add_argument("--wpm", action="append", metavar="NAME=RATE",
                    help=f"speaking rate per character (default {DEFAULT_WPM})")
    ap.add_argument("--cast", help="comma-separated character names you have voices for")
    ap.add_argument("--target", type=float, help="target length in seconds")
    ap.add_argument("--gap", type=float, default=DEFAULT_GAP,
                    help=f"seconds between speaker turns (default {DEFAULT_GAP})")
    ap.add_argument("--manifest", metavar="FILE", help="write the per-line voice manifest (JSON)")
    ap.add_argument("--srt", metavar="FILE", help="write an SRT caption file")
    ap.add_argument("--srt-names", action="store_true", help="prefix captions with the speaker")
    ap.add_argument("--json", action="store_true", help="print the full analysis as JSON")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    cast = [c.strip() for c in args.cast.split(",") if c.strip()] if args.cast else None
    a = analyse(raw, wpm=parse_wpm(args.wpm), target=args.target, cast=cast, gap=args.gap)
    if not a:
        print("no dialogue lines found (write them as NAME: text)", file=sys.stderr)
        sys.exit(2)

    if args.manifest:
        write_manifest(a, args.manifest)
    if args.srt:
        write_srt(a, args.srt, names=args.srt_names)
    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        render(a)
        if args.manifest:
            print(f"  manifest -> {args.manifest}")
        if args.srt:
            print(f"  captions -> {args.srt}")
    sys.exit(0)


if __name__ == "__main__":
    main()

# How I build a Sermones episode (the rating system)

Each episode joins 3 things: **ChatGPT chats → VERBA cards → this audio.**
Patrick listens on repeat, so every line must earn its place.

## 1. Pick the words (about 25 targets)

Give each candidate word or pattern points. Take the top 25. Use no more than 3 new words.

| Source | Points |
|---|---|
| Hell list or orphan word | +5 |
| A mistake from a chat (e.g. *ad tabernam*, *cum uxōre meā*, *domī*, *Post Missam*) | +4 |
| A ChatGPT "her" line that made him lost (*ūnō impetū*, *sine intermissiōne*, *īnsolēns est*, *sīve*, *Ferē rēctē*) | +4 |
| Slow on the VERBA timer (over 1.0 s) | +3 |
| Used in a chat, but has no rating yet | +2 |
| A new word on the road to 2,000 | +2 |
| Each earlier episode where he already heard it | −2 |

His strong words get no points. They are the glue and they come back anyway.

## 2. Write the dialogue, then score it (out of 10; render only at 8+)

| Test | Points |
|---|---|
| **Story**: one real scene from his life, with a turn (a problem or a surprise) | 2 |
| **Humour**: 3+ jokes or a running gag (the magpie war, ChatGPT saying *ūnō impetū* for the 40th time) | 2 |
| **Targets**: every target 3+ times, in different lines | 2 |
| **ChatGPT survival kit**: 4–6 "her" lines, each with one of his fix replies (*Lentius, quaesō*, *Quid significat…?*, *Satis est, pergāmus*) | 2 |
| **Easy to hear**: lines of 8 Latin words or fewer, about 90% known words | 2 |

## 3. Manner: make it sound like a real podcast, not ping-pong

- **Not symmetrical.** Sometimes one person talks for 3–4 lines in a row and the other only says *Ita.* / *Mmm.* / *Vērē?*
- **Long turns**: one person tells a small story; the other reacts, interrupts, asks one short question.
- **Thinking out loud**: *Hmm… quōmodo dīcitur… ah, mēta!* / *Exspectā, cōgitō…* / *Verbum mihi deest.*
- **Never say a wrong form.** "Self-correction" = a pause while thinking for a word: *Cum… [short pause] cum fīliō meō.*
- **Clarify for yourself**: *Id est…* / *Hoc est, …* / *Sīve…* (the same say-it-again moves ChatGPT uses).
- **Real reactions**: laughs, teasing, *Ecce!*, *Euge!*, *Minimē!*, *Quid?!*
- **Emotion = "podcast level" (Rogan/Peterson), about 20% of what ElevenLabs does by default.** (Researched 19 Oct.)
  - **Stability 0.5 ("Natural")**, now the renderer default. Low stability (0.2) makes tags extreme and breathy.
  - **Tags on about 1 line in 4**, not on most lines. Let the words and punctuation carry the feeling ("…" for a thinking pause, "?" for curiosity). Use few "!" and no CAPITALS.
  - **Write mild tags in plain words** (v4 accepts free text): [lightly amused], [quietly amused], [light chuckle], [matter-of-fact], [a little more serious], [dry], [relaxed], [curious], [thoughtful], [hesitates], [short pause].
  - **Put a laugh mid-line, after the funny word** ("Cum petasō… [light chuckle]"). A tag at the start colours the whole line.
  - No more than 1 tag per line. Never stack tags, and never use [laughing], [excited], [indignant] or [panicked] (too big).
  - **BANNED: anything breathy.** No [sighs], [exhales], [inhales], [gasps], [groans], [panting], [softly], [whispers], [gently], [calmly], [warmly]. Patrick (19 Oct): Ep 2's breaths sound "pseudo-erotic" and are very distracting. Ep 2 stays as it is.
- **B1–C1 talk, with his words**: opinions (*Meā sententiā…*, *Putō…*, *Quid māvīs?*, *Cūr id putās?*), agree and disagree (*Vērē dīcis*, *Tamen…*), reasons (*quia, quoniam*), a small debate that the story settles at the end.
- Same-speaker lines get a shorter gap (the renderer does this); a line can also set its own `gap` in seconds.
- Score: count this inside "Story" and "Humour". A script that is all A-B-A-B loses 1 point.

## 3b. Tone (Patrick, 19 Oct, after Ep 3: "unhinged", "condescending", "cringe")

- Two relaxed friends, equals. Iulia is never the teacher; nobody corrects or "tests" the other.
- Humour comes from the situation (magpies, the empty pram, ChatGPT itself), never from teasing Marcus.
- No moralising and no fake debates about faith or rules ("the pub after Mass isn't holy" = banned). Opinions are light and practical.
- Default voices: no emotion tags unless one is really needed. Calm, normal speaking.

## 4. Famous quotes (2–3 per episode)

- Bible (Vulgate) and famous classical Latin that fit the scene: *Festīnā lentē* (Augustus), *Sinite parvulōs venīre ad mē* (Mark 10:14), *Dum spīrō, spērō* (motto; the idea is in Cicero).
- In the banter, someone says the quote, the other asks *Quis hoc dīxit?* / *Scīsne unde veniat?*, then: credit it (who, which book) and explain it in simple Latin (*id est…*).
- Never use the same quote twice in a season. The ChatGPT gag works only when Marcus jokes about the app (Ep 2). It fails when Iulia copies the teacher to correct him (Ep 3). Used: Festīnā lentē, Sinite parvulōs venīre ad mē, Dum spīrō spērō (Ep 2); Īte missa est, In vīnō vēritās, Tū servāstī bonum vīnum ūsque adhūc (Ep 3).

## 5. Fixed format

- Two voices: Marcus = **an Italian male voice** (from 19 Oct; Patrick's own clone felt uncanny and was half the problem, so do not use it), Iulia = Charlotte – Warm & Conversational. Before Ep 4: audition 2–3 Italian male library voices and pick one.
- Intro by one host: *Bene vēnistis ad colloquium! Hodiē loquāmur dē …*
- Each line: English, then Latin, same voice. Short pauses. [quickly].
- About 50 lines (about 5 min per pass).
- Music bed: V5 at -7 dB (raised 2 dB on 19 Oct; Patrick could barely hear it).
- Tracks: **a = English → Latin × 3**, **b = Latin only × 3** (about 15 min each).
- After each episode, update a "heard" list, so the next one picks new weak words.

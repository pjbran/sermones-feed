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
- **NO emotion tags at all** (19 Oct). Patrick: the custom directions make the speakers "sound like they're on drugs". Ep 2 and Ep 3 used them and were deleted.
- **Ep 1 is the benchmark**: no tags, ElevenLabs Dialogue mode (the whole conversation in one go), plain natural speech. Match Ep 1.
- No breath cutter (it made hard snips at line ends, 19 Oct). Soft cuts as in Ep 1.
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
- Never use the same quote twice in a season. The ChatGPT gag works only when Marcus jokes about the app (Ep 2). It fails when Iulia copies the teacher to correct him (Ep 3). (Ep 2 and 3 were deleted, so all quotes are free to use again.)

## 5. Fixed format (back to the Ep 1 recipe, confirmed 19 Oct)

- Voices: Iulia = "Rossana – Warm Italian Conversational". Marcus = an **Italian male** library voice (Patrick, 22 Oct: no more his own voice). Ep 4 used "Emanuele Matte – Clear and Serious" (qQFoiN2eQXULODjD1SwL). Backup if he dislikes it: "Valentino – English with Italian accent" (conversational).
- Job `"mode": "dialogue"`: the whole English conversation and the whole Latin conversation are each rendered in one go (ElevenLabs text-to-dialogue with timestamps, chunks under 1,800 characters), then cut softly at the given times and stitched English → Latin.
- No emotion tags, no [quickly], stability 0.2 (as Ep 1). Pauses 0.5 s after the English, 0.8 s before the next line (Ep 1); Latin only 0.35 s.
- Intro by one host: *Bene vēnistis ad colloquium! Hodiē loquāmur dē …*
- About 50 lines. Music: V5 Hammock at -7 dB (2 dB above Ep 1).
- Tracks: **a = English → Latin × 3**, **b = Latin only × 3**.

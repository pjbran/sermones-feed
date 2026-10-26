# How I build a Sermones episode (the rating system)

Each episode joins 3 things: **ChatGPT chats → VERBA cards → this audio.**
Patrick listens on repeat, so every line must earn its place.


## 0. NO SNIPPING (Patrick, 22 Oct, 5 pm: "DO NOT DO ANY MORE SNIPPING. It has completely ruined the new episode")
- Never cut into a word or its fade-out. Ep 4 was cut at the ElevenLabs text timestamps, which end before the sound ends: every line was clipped.
- A cut may only be made in real silence (measured on the audio), with a soft fade. Before publishing, check every cut point: the sound there must be below about -45 dB. If a line cannot be cut cleanly, do not publish it.
- No breath cutter, no trimming that touches speech.

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
- Titles: no "Ep N" (Patrick, 22 Oct: the podcast app shows the number). Title = "<name> · English → Latin × 3" / "<name> · Latin only × 3".

## 6. Sentence ladders (Patrick, 22 Oct: "the sentence ladder is good")
- Job `"type": "drill"`: pairs [English, Latin]; each sentence shifts a little from the one before (person, tense, can / want / let's, one added part). About 50 pairs ≈ 3 min, `repeat: 3`. `"latin_only": true` = no English.
- Free: Piper voices in the Action (English: en_GB-jenny_dioco-medium; Latin: it_IT-paola-medium). **Latin goes in as IPA** (`free_tts.latin_ipa`: eSpeak's Latin rules → raw phonemes with stress and long vowels, e.g. dormīvī → dɔrmˈiːwiː). Patrick picked IPA over the Italian respelling on 22 Oct (test job 0018). **Default since 22 Oct 9:27 pm: v said as v** (`v_as_v`; qu / gu stay kw / gw; test 0022), no pause added at the end (it made an exhale), gentle trim (-55 dB, 0.12 s). 0 credits.
- **Every ladder also gets a Latin-only track** (Patrick, 24 Oct: "it's great"). The drill job makes it automatically (`with_latin_only`, default on): "Ladder N · <topic> · Latin only (× 3)".
- **Pyramids** (Patrick, 25 Oct): a long track built on 4–5 core sentences only. Wide base, one new thing per step, the peak, then pivots (other person, verb, negative, question), plain-vs-new contrast pairs (Loqueris → ut loquāris), spaced review of earlier cores, a funny closing story using all cores, and all peaks again at the end. Each peak 6+ times. Ladder 5 = the subjunctive pyramid (ut / nē / cum + imperfect / indirect question), 288 pairs, 23 min.
- **Topic vocabulary** (Patrick, 26 Oct): nouns and verbs must belong to the pyramid's topic. For an abstract topic (learning, listening, agreeing), no everyday props ("no magpies lol"). Ladder 7 = pyramid 3: commands + ut / nē (Docē mē, ut discam · Audī mē, ut intellegās · Rogā mē, ut cōgitem · Loquāmur, ut cōnsentiāmus · Prīmum cōgitā, nē errēs), 312 pairs × 2.
- **Vocab pyramids** (Patrick, 26 Oct, road to 2,000): 50 new Road words per set (the next unseen words in road order), in 5 scenes of 10 words; each word ~6+ hearings (word → chunk → sentence in its most common role → pivot to the next most useful form → reuse with other new words); plus his top ~30 live hell words (from the Core answer log, hell.js rules) in clear frames, 4+ times each; spaced review of earlier scenes; closing story of the whole day; quick-fire list of all new and hell words. One writer agent per scene + one for the closing, then 2 reviewer agents. Ladder 8 = set 1 (731 pairs), held until 28 Oct with `not_before` (experiment 152); the workflow runs daily at 6 am Sydney to release held jobs.
- Ladders: put questions all the way through (a conversation with yourself: why? where? how much? and clarifying, 'that is…').
- **NO "SUICIDE LADDERS"** (Patrick, 24 Oct): "You don't load a boulder at the top of a boulder." Ladder 4 brought in *experrēctus est* at its peak and then dropped it.
  - The TOP of every ladder (its longest, most interesting sentence) gets its main parts reused **at least 3 more times** before the next ladder starts, in new frames: the whole sentence again, then in an *if* sentence, a *that* sentence (*putō / dīcō… + accusative and infinitive*), a comparison, a question and answer, another person or tense.
    Example: *Fessus sum, quia fīlius meus nocte experrēctus est.* → *Sī fīlius meus nocte expergīscitur, fessus sum.* → *Uxor mea dīcit fīlium nocte experrēctum esse.* → *Hodiē minus fessus sum quam herī.*
  - No new word or form at the top that is not used again. Every new element gets 3+ uses.
  - **Free tracks cost nothing, so length is fine:** make it longer rather than drop content. Every new ladder: 10–20% longer than the last, as a SOFT minimum (Patrick, 24 Oct: 30, 40, 50% longer is fine, as long as the ladder follows the other rules).
  - **Before publishing, a separate agent reviews every ladder** for this (each top reused 3+ times; each new word reused 3+ times), plus the Latin itself.
- Done 22 Oct evening: ladder 4 'talking to myself' (160 pairs, 10 min, IPA), story 'Fābella · Rūfus et cāseus' (56 pairs × 3, IPA).
- Done: ladder 1 (going, working, liking, playing, seeing, talking, learning, eating), ladder 2 (walking with my son, putō / sciō, the meeting, dīxit sē…, possum / poteram, grātiās… quod, cum domum vēnerō), ladders 1 + 2 Latin only.

## 7. Naming (Patrick, 24 Oct: "standardise… Ladder or Chat")
- Every title starts with **Chat ·** (a conversation or a story: two hosts, or Iulia telling a story) or **Ladder ·** (a sentence ladder).
- Chat: "Chat · <name> · English → Latin × 3" / "Chat · <name> · Latin only × 3" (the renderer adds "Chat ·" itself). Stories: "Chat · <name> (story, × 3)".
- Ladder: "Ladder N · <topic> (× 3)", "Ladder 1 + 2 · Latin only (× 3)". Older versions end in "(old)". No "Ep N", no "Bonus".

## 8. Storage (26 Oct)
- MP3s are NOT kept in the website any more (GitHub Pages limit about 1 GB). After each run, `pipeline/publish.py` uploads every new MP3 to the GitHub release `audio` and the feed points to `https://github.com/pjbran/sermones-feed/releases/download/audio/<file>`. Free, no real size limit.
- Free tracks (ladders, pyramids, stories) are saved at 64 kbps mono (speech-friendly, about 60% smaller).
- The "(old)" versions were removed on 26 Oct (Patrick: "do 123").

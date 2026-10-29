# Brief: "Officium" — a 5-episode comic audio series of Latin sentence pyramids (Patrick, 29 Oct 2026)

## Who and why
- Listener: Patrick, adult Latin learner (B1-ish), Sydney, works as a business analyst on a big IT project, hates meetings. He listens on walks: each line is said in English, then in Latin (Iulia's voice). He repeats the Latin out loud.
- His words: "build me a series of 3-5 like that, in an attempt to build in as much road to 2000 vocab as you can". He LOVED Ladder 10 (the meeting about meetings). Example of the style and format: /home/claude/sermones-feed/jobs/0045-drill-scala-10-conventus.json (read it first; read the pairs in full).
- Humour: "The Office x Monty Python" STYLE (never quote or copy any sketch). Deadpan; everyday words used in a funny way; logic taken one step too far; escalation; callbacks; nothing absurd (no talking animals, no magic). The pyramids build ONE funny story with a payoff.
- Care: no wife, marriage or family-home scenes (work, colleagues, the city only). Keep it kind; the butt of a joke is the situation or the office, not a person's body.

## The week (one episode per day; same cast; callbacks welcome)
- Ep 1 Mon "Tessera" (the password) — ALREADY WRITTEN: /home/claude/series/ep11_pairs.py (read it for the cast and tone).
- Ep 2 Tue · Ep 3 Wed · Ep 4 Thu · Ep 5 Fri (yours is named in your task).
- Cast: Marcus (the narrator, a man: use masculine forms for him, e.g. *lassus sum*), Gaius (the boss: says "Breviter dīcam" and then talks for an hour), Tullia (writes EVERYTHING in the minutes, literally: "Tullia scrībit: ..."), Quintus (IT; loves computers more than people; never laughs; rules), Livia (her slide is always "paene parāta"). You may add ONE new character.

## The form (follow it exactly)
- 5 core sentences (the "peaks"), each built up step by step from 1–2 words (one new chunk per line), then turned around: other person, past/future, negative, question and answer, a "that" sentence (dīcit + accusative and infinitive), an "if" sentence. Each core appears in full at least 3 times (spread out: built in its scene, again later, and all 5 together in a final review block). Cores should carry useful B1 grammar (a different mix from Ladder 10: e.g. gerundive "-ndum est", comparatives, relative clauses with quī/quae/quod, future perfect in sī-clauses, perfect passive, ut/nē, cum + subjunctive, participles, indirect questions).
- Questions all the way through (Cūr? Quis? Ubi? Quandō? Quid? -ne? nōnne?) — a conversation with yourself.
- Scenes: 4–6 short scenes that build the story; a closing scene with the payoff; then the review block of all 5 cores (and 2–4 pivots), ending on a last joke line.
- Length: 260–300 pairs. Latin lines mostly 2–9 words, never over 14. (That gives 10–14 minutes of Latin.)

## The vocabulary (the main point of the series)
- YOUR TARGET WORDS (Road to 2,000 words Patrick has NOT yet seen) are in /home/claude/study/series_words.json under your episode key. Use EVERY one of them, each at least 3 times (aim 4+), in different lines and, where natural, in different forms. First meeting = a short line where every other word is easy, so the meaning is clear from the English cue. Bend the story to fit the words (that is the craft); do not drop a word. If a word truly cannot fit, list it at the end of your reply.
- Also spread at least 6 of his "hell words" (hard small words), each 3+ times: quaesō, quoniam, quidem, adhūc, iam, nisi, tamen, ideō, propter, mox, tandem, quasi, enim, saltem, ūsque, igitur, sīc.
- Everything else: easy, common words (he knows the 700 most common Latin words well).

## Latin rules (hard)
- Classical Latin with ALL long vowels marked (macrons): ā ē ī ō ū. Correct grammar, natural Roman idiom. Modern words: use the given forms (computātrum, epistula ēlectronica, āëroplanum, etc.).
- The English cue follows the Latin WORD FOR WORD: every Latin word has a visible English word in the cue ("I'm" is fine; no idiom that hides a Latin word; "my/your" only when the Latin has meus/tuus). One English cue = one Latin answer: the same English line must never map to two different Latin lines (repeating an identical pair is fine).
- Direct speech in Latin with \" quotes is fine (see Ladder 10).

## Output
- Write a JSON file /home/claude/series/ep<N>.json: {"title": "Ladder <N> · <Latin title> (<English title>)", "summary": "<one sentence>", "cores": ["...", ...5], "pairs": [["English", "Latin"], ...]}. Ladder numbers: Tue = 12, Wed = 13, Thu = 14, Fri = 15.
- Then check your own file with a short Python script: number of pairs; for each target word, how many lines contain a form of it (count by hand-checked stems, not just exact match); each core's full count; no duplicate English cue with different Latin. Fix until every target word has 3+.
- Reply (under 200 words): the file path, the 5 cores, the story in 3 lines, the count of pairs, and any target word with fewer than 3 uses.

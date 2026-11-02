# Grammar series (podcast), started 1 Nov 2026

> For Claude. Companion to claude/AUDIO.md (read that first for voices, feed, rules).

**Why:** Patrick, 1 Nov 13:47: "this be done separated to the Letters stories ... a grammar intensive podcast ... I am fully open to an English voice explanation of the grammar and words etc similar to the content in the app ... called the 'grammar' series ... still utilises the pyramid ideas ... more than one pattern per podcast? IDC how long it goes". 13:51: "Go! Full 100% trust in you." 14:27: "Superb. Do the next one, make it 20-50% longer you decide". 15:26: "Go 3!". 18:03: "have you sketched out this grammar series based on the app's new grammar Forms section thingo? ... I'm a bit tired of the office theme, including coffee tired happy office themes etc — give some new ideas for the next theme". 18:08: "Go 4 heist".

## The app's map (Forms > Patterns, patterns.js build 294): 15 rows
1 rel (quī) · 2 when (cum/postquam/ubi) · 3 because · 4 if · 5 although · 6 says that (acc + inf) · 7 purpose ut/nē 🔒subj · 8 command ut/nē 🔒subj · 9 participle phrase 🔒ptc · 10 ablative absolute 🔒ptc · 11 cum + subjunctive 🔒subj · 12 indirect question 🔒subj · 13 result ut 🔒subj · 14 gerund / gerundive 🔒ger · 15 -ndum est 🔒ger.
- Live content (1 Nov): rows 1–2 only (80 items; no rīdeō left). Rows 3–6 "coming soon" (content in claude/campaign/patterns-raw.json). Rows 7–15 locked until Forms verb legs teach the subjunctive / participles / gerund.
- The podcast runs ahead of the app: fine (hear first, drill later).

## Format (job type `grammar`, run_grammar in pipeline/run_jobs.py)
- lines: `["t", talk with {Latin} in braces]` · `["p", English, Latin]` · `["q", Latin, English]` (ear quiz: Latin, 3 s pause, answer).
- Per pattern: hook → show-then-tell pairs (plain → pattern) → the app tip in 2–3 sentences ("Spot it") → pyramid (+ person pivots) → quick check → recap. Then a quick-fire Q&A, traps, the story using every tool, a grand swap ("one fact through every frame"), a big mixed ear quiz, a teaser.
- Warm-up of earlier tools at the start, in the episode's NEW world.
- About 20% English talk; plain words. His known words + topic words from his Plus deck (check core-words.js / plus-words.js), each 3+ times. Male endings ("I"). No rīdeō. Funny (Office x Python STYLE). Sense of place.
- One file: lesson, then every p/q Latin line alone, twice. Iulia (Rossana) on Flash.
- Script in repo `drafts/grammar-N.py` → jobs/NNNN-grammar-N-*.json. Separate reviewer agent before render (catches teaching-rule wording, English/Latin mismatches, story slips). Never leave "… nōn, …" self-correction lines in the Latin.
- Each episode about 20–50% longer than the last. NOTE: count by MINUTES (short story lines add lines but few minutes: G4 +23% Latin lines = only +6% minutes). G5 target ≥ 55 min.
- **THEME RULE (18:03): no more office / coffee / tired / happy themes.** One world per episode, matched to the grammar.

## Episodes done
1. Grammar 1 · Link words (rows 2–5). Job 0054, 135 lines (94 Latin), 21.4 min, ~4,040 credits. "Superb."
2. Grammar 2 · Sentences inside sentences (rows 1 + 6). Job 0055, 181 lines (128 Latin), 31.3 min, ~6,200 credits.
3. Grammar 3 · All the traps: the case of the coffee (rows 1–6 review). Job 0056, 216 lines (177 Latin), 42.7 min, ~6,580 credits.
4. Grammar 4 · So that, so that not (ut, nē): the heist (rows 7–8; first present subjunctive: "the swap" a→e, others +a, sit, possit; -ō → -m for I). Job 0057, 265 lines (217 Latin), 45.2 min, ~6,550 credits. Cast: Tertius (timid narrator), Pompōnia (leader), Bassus (huge, hungry); senator Opīmius's gold statue of himself; the dog adopts Bassus; the statue is already gone: "Salvēte, amīcī. Sērō vēnistis. — Alius fūr." Teaser: "Quis statuam cēpit?" → the detective episode (G6, indirect question). Verdict: pending.

## One-off: Grammar Map (2 Nov, outside the course)
- His ask 15:01: all 15 patterns "much more briefly ... the gist of every one of them in one listen ... one 'focus point' pyramid each"; 15:02 "a once off interruption to the sequential course". 15:09: his son's whinging ("I want to go home!") = the world (notes from another chat: one complaint → many patterns). 15:12: "NO LEO", same voice, no voice fiddling (I advised against emotion tags / v3; offered an optional 1-min speed/stability A/B, not done). 15:14: "filius meus is fine. Go map".
- Job 0058 `drafts/grammar-map.py`: narrator = the dad ("I"), the child = fīlius meus, "not fair" = son vs Dad (no invented sibling). Whinge kit warm-up (Nōlō! Volō! Cūr mihi nōn licet? Nōn aequum est! Iterum! Dā mihi! Paulō plūs! Mitte mē! … Domum īre volō!), then rows 1–15 in app order, one focus pyramid each, a 17-line story using all 15, last line "Nunc dormiendum est." 176 lines (138 Latin), 27.7 min, ~4,300 credits. Reviewer fixes: no bare endings in braces (TTS garbles {ns}, {ret}); abl abs = "with-form" not "e or ō"; -ndum est doer from context; valdē → vehementer for "so hard". Verdict (16:15, after the first few minutes): FAILED on tone. "I'm not complaining about my kids. This is meant to be like a piagetian curiosity about my kids requesting behaviour. The podcast is dripping in contempt ... 'unless you give me this, I'll cry' — that's shit, my kids don't do dark shit like that. Cut that shit out." 39 of 138 Latin lines are crying / shouting / dad sighing ("Tandem", "Silentium. Tandem", "Tamen mē audit", "Parvus mercātor"). REDONE 16:17 ("Yes redo map"): job 0059, file bonus-grammatica-mappa-lunae.mp3 (new name so apps refetch), "the boy and the moon": asking kit (Quaesō! Possumne lūdere? Ecce! Iterum!…), Piaget thread (Dīcit lūnam nōs sequī; Putat lūnam amīcam suam esse; Scīre vult cūr lūna nōs sequātur; Rogat ubi lūna dormiat — Nesciō… Bona quaestiō; Tam multa rogat ut ego quoque discam; Quamquam domum īre voluit, tamen laetus lūsit). 160 lines (124 Latin), 27.0 min, ~2,900 credits (102,823 left after). Reviewer: tone warm; fixed bene lūsit (= played well), Mē dormiente → Lūnā lūcente, the story line given to the dad.
- **NO "SUFFERING DAD" (16:17): "I fucking hate 'suffering dad' schtick. American reddit LLM-overtraining shit"** — in all content. Also pipeline/EPISODE-RULES.md 4f.
- **RULE for anything about his children:** warm, curious, delighted — how a small child learns to ASK (please, can I, why, again, more, let's), the dad fascinated and fond. No whinging frame, no threats or bargaining-by-crying, no eye-rolls or relief jokes at the child's expense, no crying/shouting as the running gag.

## Plan (his OK on the sketch implied by "Go 4 heist")
- G5 rows 9–10 participles + ablative absolute: Pompeii's last day (true event, sense of place) · G6 rows 11–12 cum + subjunctive + indirect question: the detective hunts the other thief from G4 (same gang + dog) · G7 row 13 result ut + "the jobs of ut": chariot race · G8 rows 14–15 gerund / gerundive / -ndum est: Apicius cooking show · G9 grand review of all 15.
- Spare themes: Paul's shipwreck on Malta (Acts 27–28), a walk round Sydney harbour, Leo the toddler boss.

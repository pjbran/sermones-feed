# Sermones Ambulātōriī

A personal Latin listening feed. Subscribe in a podcast app with: https://pjbran.github.io/sermones-feed/feed.xml

## How it works (no laptop)
- Claude writes a job file in `jobs/` and pushes it.
- The GitHub Action `render` calls ElevenLabs (secret `ELEVENLABS_API_KEY`), renders each line, stitches the episode
  (A English then Latin, B Latin only, C Latin only x8), adds the music, tags the MP3s and updates `feed.xml`.
- Results: `episodes/`, `auditions/`, `jobs/*.done.json`, `logs/last-run.json`.

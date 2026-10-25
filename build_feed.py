"""Rebuild feed.xml from episodes.json. Usage: python3 build_feed.py https://<user>.github.io/<repo>"""
import json, sys, subprocess, os, email.utils, datetime
from xml.sax.saxutils import escape as x
BASE = sys.argv[1].rstrip('/')
eps = json.load(open('episodes.json'))
def dur(p):
    s = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                             capture_output=True, text=True).stdout.strip())
    return f"{int(s // 60)}:{int(s % 60):02d}"
items = []
for e in sorted(eps, key=lambda e: e['date'], reverse=True):
    p = 'episodes/' + e['file']
    d = datetime.datetime.fromisoformat(e['date'])
    url = e.get('url') or f"{BASE}/{p}"                      # MP3s live in a GitHub release (26 Oct)
    length = e.get('bytes') or os.path.getsize(p)
    duration = e.get('duration') or dur(p)
    items.append(f"""    <item>
      <title>{x(e['title'])}</title>
      <description>{x(e['summary'])}</description>
      <itunes:summary>{x(e['summary'])}</itunes:summary>
      <enclosure url="{url}" length="{length}" type="audio/mpeg"/>
      <guid isPermaLink="false">sermones-{e['file']}</guid>
      <pubDate>{email.utils.format_datetime(d)}</pubDate>
      <itunes:duration>{duration}</itunes:duration>
      <itunes:season>{e['season']}</itunes:season>
      <itunes:episode>{e['episode']}</itunes:episode>
      <itunes:episodeType>full</itunes:episodeType>
      <itunes:explicit>false</itunes:explicit>
    </item>""")
feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Sermones Ambulātōriī</title>
    <link>{BASE}/</link>
    <atom:link href="{BASE}/feed.xml" rel="self" type="application/rss+xml"/>
    <language>la</language>
    <description>Latin walk talks: everyday conversations, English then Latin, and Latin only. A personal study feed.</description>
    <itunes:author>Sermones Ambulātōriī</itunes:author>
    <itunes:owner><itunes:name>Sermones Ambulātōriī</itunes:name></itunes:owner>
    <itunes:summary>Latin walk talks: everyday conversations, English then Latin, and Latin only. A personal study feed.</itunes:summary>
    <itunes:image href="{BASE}/cover.jpg"/>
    <image><url>{BASE}/cover.jpg</url><title>Sermones Ambulātōriī</title><link>{BASE}/</link></image>
    <itunes:category text="Education"><itunes:category text="Language Learning"/></itunes:category>
    <itunes:explicit>false</itunes:explicit>
    <itunes:type>serial</itunes:type>
    <lastBuildDate>{email.utils.format_datetime(datetime.datetime.now(datetime.timezone.utc))}</lastBuildDate>
{chr(10).join(items)}
  </channel>
</rss>
"""
open('feed.xml', 'w').write(feed)
print('feed.xml:', len(eps), 'episodes')

"""Rebuild feed.xml from episodes.json. Usage: python3 build_feed.py https://<user>.github.io/<repo> [show]
show = '' (the main Latin feed: feed.xml, episodes.json, episodes/) or 'news' (Ācta Diurna, the daily Latin news,
7 Nov 2026: news/feed.xml, news/episodes.json, news/episodes/, news/cover.jpg)."""
import json, sys, subprocess, os, email.utils, datetime
from xml.sax.saxutils import escape as x
BASE = sys.argv[1].rstrip('/')
SHOW = sys.argv[2] if len(sys.argv) > 2 else ''
D = SHOW + '/' if SHOW else ''
SHOWS = {
 '': dict(title='Sermones Ambulātōriī', lang='la', guid='sermones',
          desc='Latin walk talks: everyday conversations, English then Latin, and Latin only. A personal study feed.',
          cat='<itunes:category text="Education"><itunes:category text="Language Learning"/></itunes:category>', type='serial'),
 'news': dict(title='Ācta Diurna', lang='la', guid='acta',
          desc='The day in Latin: Canberra and Australian weather, the top Australian and world news, and one good story. A personal study feed.',
          cat='<itunes:category text="News"><itunes:category text="Daily News"/></itunes:category>', type='episodic'),
}
C = SHOWS[SHOW]
eps = json.load(open(D + 'episodes.json'))
def dur(p):
    s = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                             capture_output=True, text=True).stdout.strip())
    return f"{int(s // 60)}:{int(s % 60):02d}"
# Seasons = weeks (Patrick, 3 Nov 2026: "each week should be split into a season"). Monday to Sunday, Sydney time.
# Season 1 = the week of Mon 19 Oct 2026. Episode numbers restart each season (S3 E1, S3 E2 ...), in date order.
# Worked out here from each track's date, so episodes.json needs no manual season.
try:
    from zoneinfo import ZoneInfo; SYD = ZoneInfo('Australia/Sydney')
except Exception:
    SYD = datetime.timezone(datetime.timedelta(hours=11))
WEEK1 = datetime.date(2026, 10, 19)
def season_of(e):
    day = datetime.datetime.fromisoformat(e['date']).astimezone(SYD).date()
    return (day - WEEK1).days // 7 + 1
_count = {}
for e in sorted(eps, key=lambda e: e['date']):
    s = season_of(e); _count[s] = _count.get(s, 0) + 1
    e['season'], e['episode'] = s, _count[s]
items = []
for e in sorted(eps, key=lambda e: e['date'], reverse=True):
    p = D + 'episodes/' + e['file']
    d = datetime.datetime.fromisoformat(e['date'])
    url = e.get('url') or f"{BASE}/{p}"                      # MP3s live in a GitHub release (26 Oct)
    length = e.get('bytes') or os.path.getsize(p)
    duration = e.get('duration') or dur(p)
    items.append(f"""    <item>
      <title>{x(e['title'])}</title>
      <description>{x(e['summary'])}</description>
      <itunes:summary>{x(e['summary'])}</itunes:summary>
      <enclosure url="{url}" length="{length}" type="audio/mpeg"/>
      <guid isPermaLink="false">{C['guid']}-{e['file']}</guid>
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
    <title>{C['title']}</title>
    <link>{BASE}/{D}</link>
    <atom:link href="{BASE}/{D}feed.xml" rel="self" type="application/rss+xml"/>
    <language>{C['lang']}</language>
    <description>{C['desc']}</description>
    <itunes:author>Sermones Ambulātōriī</itunes:author>
    <itunes:owner><itunes:name>Sermones Ambulātōriī</itunes:name></itunes:owner>
    <itunes:summary>{C['desc']}</itunes:summary>
    <itunes:image href="{BASE}/{D}cover.jpg"/>
    <image><url>{BASE}/{D}cover.jpg</url><title>{C['title']}</title><link>{BASE}/{D}</link></image>
    {C['cat']}
    <itunes:explicit>false</itunes:explicit>
    <itunes:type>{C['type']}</itunes:type>
    <lastBuildDate>{email.utils.format_datetime(datetime.datetime.now(datetime.timezone.utc))}</lastBuildDate>
{chr(10).join(items)}
  </channel>
</rss>
"""
open(D + 'feed.xml', 'w').write(feed)
print(D + 'feed.xml:', len(eps), 'episodes')

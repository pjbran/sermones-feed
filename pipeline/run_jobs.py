"""Run every job in jobs/*.json that has no jobs/<name>.done.json yet.

Job types
- audition: find Australian voices, render one test line in each, publish auditions/index.html
- episode:  render every line (English + Latin, each speaker in their own voice), build
            A = English then Latin, B = Latin only, C = Latin only x N (loop), add them to the feed
"""
import glob, json, os, sys, hashlib, html, datetime, traceback, subprocess
sys.path.insert(0, os.path.dirname(__file__))
import el, audio
from smart import smart

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BASE = 'https://pjbran.github.io/sermones-feed'
MUSIC = {'v5': 'pipeline/music/v5-hammock-loop.mp3', 'v4': 'pipeline/music/v4-open-brushes-loop.mp3',
         'v1': 'pipeline/music/v1-sunday-morning-loop.mp3', 'none': None}
log = el.log


def clip(voice, text, stability=0.2):
    """Render one line once; cached in clips/ by voice + text, so re-mixing costs nothing."""
    h = hashlib.sha1(f'{voice}|{text}|{stability}'.encode()).hexdigest()[:16]
    p = f'clips/{h}.mp3'
    if not os.path.exists(p):
        os.makedirs('clips', exist_ok=True)
        el.tts(voice, text, p, stability=stability)
        log('  rendered:', text[:60])
    return audio.norm(audio.trim(audio.load(p)))


def fast(t, on=True):
    return ('[quickly] ' + t) if on and el.pick_model() in ('eleven_v3', 'eleven_v4') else t


# ---------------- audition ----------------
def run_audition(job):
    en = job.get('en', "Hey! Are you out walking already? I got up early this morning.")
    la = job.get('la', 'Salvē! Iam ambulās? Mātūrē surrēxī. Hōram, līberī, surrēxērunt.')
    cands = []
    for v in el.my_voices():
        lab = v.get('labels') or {}
        if 'austral' in (lab.get('accent') or '').lower() and 'australian man' not in v.get('name', '').lower():
            cands.append({'name': v['name'], 'voice_id': v['voice_id'], 'gender': lab.get('gender', '?'), 'src': 'mine'})
    for g, n in (('female', job.get('female', 3)), ('male', job.get('male', 2))):
        have = sum(1 for c in cands if c['gender'] == g)
        for v in el.shared_voices(g, n=n + have)[: max(0, n)]:
            if any(c['name'].startswith(v['name']) for c in cands):
                continue
            vid = el.add_shared(v)
            if vid:
                cands.append({'name': v['name'], 'voice_id': vid, 'gender': g, 'src': 'library',
                              'desc': (v.get('description') or '')[:120]})
    os.makedirs('auditions', exist_ok=True)
    rows = []
    for c in cands:
        try:
            x = audio.np.concatenate([clip(c['voice_id'], fast(en)), audio.sil(0.35), clip(c['voice_id'], fast(smart(la)))])
            slug = ''.join(ch for ch in c['name'].lower() if ch.isalnum())[:24] or c['voice_id'][:8]
            out = f'auditions/{c["gender"]}-{slug}.mp3'
            audio.save_mp3(audio.np.concatenate([audio.sil(0.3), x, audio.sil(0.5)]), out, {'title': f'Audition · {c["name"]}'})
            rows.append((c, out))
            log('audition ok:', c['name'], c['gender'], c['voice_id'])
        except Exception as e:
            log('audition failed:', c['name'], e)
    items = ''.join(f'<li><b>{html.escape(c["name"])}</b> · {c["gender"]}<br><small>{html.escape(c.get("desc", ""))}</small><br>'
                    f'<audio controls preload="none" src="{os.path.basename(p)}"></audio><br><code>{c["voice_id"]}</code></li>'
                    for c, p in rows)
    open('auditions/index.html', 'w').write(
        '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex"><title>Voice auditions</title>'
        '<style>body{font:16px/1.5 system-ui;max-width:560px;margin:24px auto;padding:0 16px;background:#1f3a38;color:#f4ecdc}'
        'li{margin:0 0 18px}audio{width:100%}code{font-size:11px;opacity:.6}</style>'
        f'<h1>Voice auditions</h1><p>"{html.escape(en)}" then <i>{html.escape(la)}</i></p><ol>{items}</ol>')
    json.dump([{**c, 'file': p} for c, p in rows], open('auditions/voices.json', 'w'), indent=1)
    return {'auditions': len(rows), 'page': f'{BASE}/auditions/'}


# ---------------- episode ----------------
def run_episode(job):
    V = json.load(open('pipeline/voices.json'))
    V.update(job.get('voices', {}))
    host = job.get('intro_by', 'F')
    pe, pl, plat = (job.get('pause_after_english', 0.35), job.get('pause_before_next', 0.55), job.get('pause_latin_only', 0.35))
    st = job.get('stability', 0.2)
    q = job.get('quick', True)
    intro = job.get('intro', [])  # [{en, la}], said by the host
    lines = job['lines']          # [{who: F|M, en, la}]

    def L(who, la):
        return clip(V[who], fast(smart(la), q), st)

    def E(who, en):
        return clip(V[who], fast(en, q), st)

    A, B = [], []
    for i, it in enumerate(intro):
        A += [(E(host, it['en']), pe), (L(host, it['la']), pl * (1.4 if i == len(intro) - 1 else 1))]
        B += [(L(host, it['la']), pl)]
    for ln in lines:
        A += [(E(ln['who'], ln['en']), pe), (L(ln['who'], ln['la']), pl)]
        B += [(L(ln['who'], ln['la']), plat)]
    loops = int(job.get('loops', 8))
    C = []
    for k in range(loops):
        C += B[:-1] + [(B[-1][0], 2.5)]

    music = MUSIC.get(job.get('music', 'v5'), MUSIC['v5'])
    lvl, dip = job.get('music_level_db', -9), job.get('music_dip_db', 7)
    num = int(job['number']); season = int(job.get('season', 1)); slug = job['slug']; title = job['title']
    eps = json.load(open('episodes.json'))
    nxt = max([e['episode'] for e in eps] + [0]) + 1
    cover = audio.make_cover('cover.jpg', f'Ep {num} · {title}', f'episodes/s{season}e{num:02d}-cover.jpg')
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=11)))
    made = []
    for code, items, label, summ in (
            ('a', A, 'English → Latin', job.get('summary', '') + ' Each line in English, then in Latin.'),
            ('b', B, 'Latin only', job.get('summary', '') + ' Latin only.'),
            ('c', C, f'Latin only × {loops}', job.get('summary', '') + f' Latin only, {loops} times in a row (a long loop).')):
        voice, ev = audio.sequence(items)
        x = audio.mix_music(voice, ev, music, lvl, dip)
        fn = f's{season}e{num:02d}{code}-{slug}.mp3'
        tags = {'title': f'Ep {num} · {title} · {label}', 'artist': 'Sermones Ambulātōriī', 'album_artist': 'Sermones Ambulātōriī',
                'album': f'Sermones Ambulātōriī · Season {season}', 'track': str(nxt), 'genre': 'Language Learning', 'date': str(now.year)}
        audio.save_mp3(x, 'episodes/' + fn, tags, cover)
        eps = [e for e in eps if e['file'] != fn]
        eps.append({'file': fn, 'title': tags['title'], 'season': season, 'episode': nxt,
                    'date': (now + datetime.timedelta(minutes=len(made))).isoformat(timespec='seconds'), 'summary': summ.strip()})
        made.append(fn); nxt += 1
        log('built', fn, f'{len(x) / audio.SR / 60:.1f} min')
    json.dump(eps, open('episodes.json', 'w'), indent=1, ensure_ascii=False)
    subprocess.run([sys.executable, 'build_feed.py', BASE], check=True)
    return {'files': made}


def main():
    done_any = False
    for jp in sorted(glob.glob('jobs/*.json')):
        if jp.endswith('.done.json') or os.path.exists(jp[:-5] + '.done.json'):
            continue
        job = json.load(open(jp)); el.LOG.clear()
        log('== job', jp, job.get('type'))
        res = {'job': jp, 'ok': False}
        try:
            res.update(run_audition(job) if job['type'] == 'audition' else run_episode(job)); res['ok'] = True
        except Exception as e:
            res['error'] = repr(e); log(traceback.format_exc())
        res['log'] = el.LOG[-200:]
        res['at'] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
        if res['ok']:
            json.dump(res, open(jp[:-5] + '.done.json', 'w'), indent=1, ensure_ascii=False)
        os.makedirs('logs', exist_ok=True)
        json.dump(res, open('logs/last-run.json', 'w'), indent=1, ensure_ascii=False)
        done_any = True
    if not done_any:
        print('no new jobs')


if __name__ == '__main__':
    main()

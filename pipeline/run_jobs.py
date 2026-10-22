"""Run every job in jobs/*.json that has no jobs/<name>.done.json yet.

Job types
- audition: find Australian voices, render one test line in each, publish auditions/index.html
- episode:  render every line (English + Latin, each speaker in their own voice), build
            a = English then Latin x 3, b = Latin only x 3 (optional c = long Latin loop), add them to the feed. Voices can be IDs or "name:<exact voice name>" (looked up in My Voices).
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
    return audio.norm(audio.trim(audio.load(p)))  # (debreath removed 19 Oct: it made hard snips)


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
    if not rows:
        raise RuntimeError('No auditions rendered (see the log above; the API key may need Voices: Read and Write).')
    return {'auditions': len(rows), 'page': f'{BASE}/auditions/'}


# ---------------- sound test ----------------
def run_test(job):
    """Render the same few lines in several ways and publish tests/<name>/index.html to compare by ear."""
    V = resolve_voices({**json.load(open('pipeline/voices.json')), **job.get('voices', {})})
    lines = job['lines']; name = job.get('name', 'test'); st = job.get('stability', 0.5)
    out_dir = f'tests/{name}'; os.makedirs(out_dir, exist_ok=True)
    seq = []  # (who, text, latin?)
    for ln in lines:
        seq += [(ln['who'], ln['en'], False), (ln['who'], smart(ln['la']), True)]
    gaps = [0.35 if i % 2 == 0 else 0.55 for i in range(len(seq))]
    rows = []

    def save(x, key, label):
        f = f'{out_dir}/{key}.mp3'
        audio.save_mp3(audio.np.concatenate([audio.sil(0.4), x, audio.sil(0.6)]), f, {'title': label})
        rows.append((label, os.path.basename(f))); log('test ok:', label)

    def per_line(model, ctx=False, quick=False, cut=True):
        clips = []
        for i, (w, t, la) in enumerate(seq):
            txt = ('[quickly] ' + t) if quick else t
            h = hashlib.sha1(f'{V[w]}|{model}|{txt}|{st}|{ctx}'.encode()).hexdigest()[:16]
            p = f'clips/t-{h}.mp3'
            if not os.path.exists(p):
                body = {'text': txt, 'model_id': model, 'voice_settings': {'stability': st, 'similarity_boost': 0.75}}
                if ctx:
                    if i: body['previous_text'] = seq[i - 1][1]
                    if i + 1 < len(seq): body['next_text'] = seq[i + 1][1]
                r = el.req('POST', f'/text-to-speech/{V[w]}?output_format=mp3_44100_128', json=body)
                if r.status_code != 200:
                    raise RuntimeError(f'{model}: {r.status_code} {r.text[:200]}')
                open(p, 'wb').write(r.content)
            y = audio.norm(audio.load(p))
            clips.append(audio.debreath(y) if cut else y)
        return audio.sequence(list(zip(clips, gaps)), lead=0.2, tail=0.2)[0]

    variants = job.get('variants', ['v4_lines', 'v4_dialogue', 'v2_lines'])
    if 'now' in variants:
        try:
            el._MODEL = el._MODEL or 'eleven_v4'
            save(per_line_cached(V, seq, gaps, job.get('now_stability', 0.5)), 'a-now', 'A · As Ep 3 (v4, [quickly]), breaths cut')
        except Exception as e:
            log('now failed:', e)
    for v in variants:
        try:
            if v == 'v4_lines':
                save(per_line('eleven_v4'), 'b-v4-lines', 'B · Eleven v4, line by line, natural speed, breaths cut')
            elif v == 'v4_dialogue':
                x = None
                for model in ('eleven_v4', 'eleven_v3'):
                    body = {'inputs': [{'text': t, 'voice_id': V[w]} for w, t, la in seq], 'model_id': model,
                            'settings': {'stability': job.get('dialogue_stability', st)}}
                    r = el.req('POST', '/text-to-dialogue?output_format=mp3_44100_128', json=body)
                    if r.status_code == 200:
                        p = f'{out_dir}/raw-dialogue-{model}.mp3'; open(p, 'wb').write(r.content)
                        x = audio.norm(audio.load(p)); x = x if job.get('dialogue_stability') else audio.debreath(x, max_gap=0.55); used = model; break
                    log('dialogue refused', model, r.status_code, r.text[:200])
                if x is not None:
                    save(x, 'c-dialogue', f'NOW · {used} Dialogue mode (as the episodes) · full price' if job.get('dialogue_stability') else f'C · Whole conversation in one go ({used} dialogue), breaths cut')
            elif v == 'flash_lines':  # 20 Oct: the half-price models (0.5 credits a character), no breath cutter
                save(per_line('eleven_flash_v2_5', ctx=True, cut=False), 'e-flash', 'Flash v2.5 · HALF PRICE · line by line')
            elif v == 'turbo_lines':
                save(per_line('eleven_turbo_v2_5', ctx=True, cut=False), 'f-turbo', 'Turbo v2.5 · HALF PRICE · line by line')
            elif v == 'v2_plain':
                save(per_line('eleven_multilingual_v2', ctx=True, cut=False), 'g-v2', 'Multilingual v2 · full price · line by line')
            elif v == 'v2_lines':
                save(per_line('eleven_multilingual_v2', ctx=True), 'd-v2-lines', 'D · Calm narration model (Multilingual v2), line by line, breaths cut')
        except Exception as e:
            log('variant failed:', v, e)
    items = ''.join(f'<li><b>{html.escape(l)}</b><br><audio controls preload="none" src="{f}"></audio></li>' for l, f in rows)
    script = ''.join(f'<li>{html.escape(ln["en"])}<br><i>{html.escape(ln["la"])}</i></li>' for ln in lines)
    open(f'{out_dir}/index.html', 'w').write(
        '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex"><title>Sound test</title>'
        '<style>body{font:16px/1.5 system-ui;max-width:560px;margin:24px auto;padding:0 16px;background:#1f3a38;color:#f4ecdc}'
        'li{margin:0 0 18px}audio{width:100%}small{opacity:.7}</style>'
        f'<h1>Sound test</h1><p>Same lines, different ways. Pick the one that sounds most like two calm people talking.</p><ol>{items}</ol>'
        f'<h2>Script</h2><ol><small>{script}</small></ol>')
    if not rows:
        raise RuntimeError('No test variant rendered.')
    return {'tests': len(rows), 'page': f'{BASE}/{out_dir}/'}


def per_line_cached(V, seq, gaps, st):
    clips = [clip(V[w], '[quickly] ' + t, st) for w, t, la in seq]
    return audio.sequence(list(zip(clips, gaps)), lead=0.2, tail=0.2)[0]


# ---------------- dialogue mode (the Episode 1 recipe) ----------------
def render_dialogue(seq, st):
    """One ElevenLabs dialogue render (whole conversation in one go) with exact times per input.
    seq: [(voice_id, text)]. Cached in clips/d-<hash>.mp3 + .json."""
    import base64
    h = hashlib.sha1(json.dumps([seq, st], ensure_ascii=False).encode()).hexdigest()[:16]
    mp3, js = f'clips/d-{h}.mp3', f'clips/d-{h}.json'
    if not (os.path.exists(mp3) and os.path.exists(js)):
        os.makedirs('clips', exist_ok=True)
        last = ''
        for model, stab in (('eleven_v4', st), ('eleven_v4', 0.5), ('eleven_v3', 0.5)):
            body = {'inputs': [{'text': t, 'voice_id': v} for v, t in seq], 'model_id': model, 'settings': {'stability': stab}}
            r = el.req('POST', '/text-to-dialogue/with-timestamps?output_format=mp3_44100_128', json=body)
            if r.status_code == 200:
                d = r.json()
                open(mp3, 'wb').write(base64.b64decode(d['audio_base64']))
                json.dump({'model': model, 'stability': stab, 'segments': d.get('voice_segments', [])}, open(js, 'w'))
                log('  dialogue rendered:', model, stab, len(seq), 'inputs')
                break
            last = f'{r.status_code} {r.text[:300]}'; log('dialogue refused', model, stab, last)
        else:
            raise RuntimeError('Dialogue render failed: ' + last)
    x = audio.load(mp3); segs = json.load(open(js))['segments']
    spans = []
    for i in range(len(seq)):
        ss = [g for g in segs if g.get('dialogue_input_index') == i]
        if not ss:
            raise RuntimeError(f'No timing for dialogue input {i}: {seq[i][1][:40]}')
        spans.append((min(g['start_time_seconds'] for g in ss), max(g['end_time_seconds'] for g in ss)))
    out = []
    for i, (a, b) in enumerate(spans):   # soft edges, as in Episode 1 (no hard snips)
        gp = a - spans[i - 1][1] if i else 1.0
        gn = spans[i + 1][0] - b if i + 1 < len(spans) else 1.0
        pre = min(0.06, max(0.0, gp - 0.05)); post = min(0.18, max(0.02, gn - 0.06))
        seg = x[max(0, int((a - pre) * audio.SR)):min(len(x), int((b + post) * audio.SR))]
        out.append(audio.fade(audio.norm(seg), 12))
    return out


def dialogue_clips(seq, st, max_chars=1800):
    """Split a long conversation into renders under the API's ~2,000 character limit (at line breaks)."""
    out, chunk, n = [], [], 0
    for item in seq:
        if chunk and n + len(item[1]) > max_chars:
            out += render_dialogue(chunk, st); chunk, n = [], 0
        chunk.append(item); n += len(item[1])
    if chunk:
        out += render_dialogue(chunk, st)
    return out


# ---------------- episode ----------------
def resolve_voices(V):
    """Turn "name:Australian man" into a voice ID (exact, case-sensitive name in My Voices)."""
    if not any(str(v).startswith(('name:', 'shared:')) for v in V.values()):
        return V
    mine = el.my_voices()
    out = {}
    for k, v in list(V.items()):
        if str(v).startswith('shared:'):          # e.g. "shared:italian:male" = best library voice, added once
            _, accent, gender = v.split(':')[:3]
            have = [m for m in mine if accent in ((m.get('labels') or {}).get('accent') or '').lower()
                    and ((m.get('labels') or {}).get('gender') or '') == gender and m.get('category') != 'cloned']
            if have:
                V[k] = 'id:' + have[0]['voice_id']; log('voice', k, '=', have[0]['name'], '(already in my voices)')
            else:
                pick = el.pick_shared(accent, gender)
                vid = el.add_shared(pick) if pick else None
                if not vid:
                    raise RuntimeError(f'Could not add a {accent} {gender} library voice (voice slots full?).')
                V[k] = 'id:' + vid; log('voice', k, '=', pick['name'], vid, '(added from the library)')
    for k, v in V.items():
        if str(v).startswith('id:'):
            out[k] = v[3:]; continue
        if str(v).startswith('name:'):
            hit = [m['voice_id'] for m in mine if m.get('name') == v[5:]] or \
                  [m['voice_id'] for m in mine if m.get('name', '').startswith(v[5:])][:1]
            if not hit:
                raise RuntimeError(f'Voice "{v[5:]}" not found. My voices: ' + ', '.join(m.get('name', '?') for m in mine))
            out[k] = hit[0]; log('voice', k, '=', v[5:], hit[0])
        else:
            out[k] = v
    return out


def run_episode(job):
    V = json.load(open('pipeline/voices.json'))
    V.update(job.get('voices', {}))
    V = resolve_voices(V)
    for k in {job.get('intro_by', 'F')} | {ln['who'] for ln in job['lines']}:
        if not V.get(k):
            raise RuntimeError(f'No voice set for speaker {k} (pipeline/voices.json or job "voices").')
    host = job.get('intro_by', 'F')
    pe, pl, plat = (job.get('pause_after_english', 0.35), job.get('pause_before_next', 0.55), job.get('pause_latin_only', 0.35))
    st = job.get('stability', 0.5)  # 0.5 = Natural: mild tags, no breathiness (19 Oct)
    q = job.get('quick', False)  # [quickly] made voices rush and gasp (19 Oct)
    intro = job.get('intro', [])  # [{en, la}], said by the host
    lines = job['lines']          # [{who: F|M, en, la}]

    def L(who, la):
        return clip(V[who], fast(smart(la), q), st)

    def E(who, en):
        return clip(V[who], fast(en, q), st)

    A, B = [], []
    if job.get('mode') == 'dialogue':   # the Episode 1 recipe: whole conversation in one go, cut softly
        pe, pl = job.get('pause_after_english', 0.5), job.get('pause_before_next', 0.8)
        st = job.get('stability', 0.2)
        IN = dialogue_clips([x for it in intro for x in ((V[host], it['en']), (V[host], smart(it['la'])))], st) if intro else []
        EN = dialogue_clips([(V[ln['who']], ln['en']) for ln in lines], st)
        LA = dialogue_clips([(V[ln['who']], smart(ln['la'])) for ln in lines], st)
        for i in range(len(intro)):
            A += [(IN[2 * i], pe), (IN[2 * i + 1], pl * (1.5 if i == len(intro) - 1 else 1))]
            B += [(IN[2 * i + 1], pl)]
        for i in range(len(lines)):
            A += [(EN[i], pe), (LA[i], pl)]
            B += [(LA[i], plat)]
        intro, lines_iter = [], []
    else:
        lines_iter = lines
    for i, it in enumerate(intro):
        A += [(E(host, it['en']), pe), (L(host, it['la']), pl * (1.4 if i == len(intro) - 1 else 1))]
        B += [(L(host, it['la']), pl)]
    for i, ln in enumerate(lines_iter):
        # same speaker goes on (a long turn, thinking for a word): a shorter gap; a line can set its own "gap"
        same = i + 1 < len(lines_iter) and lines_iter[i + 1]['who'] == ln['who']
        g = ln.get('gap', pl * 0.6 if same else pl)
        A += [(E(ln['who'], ln['en']), pe), (L(ln['who'], ln['la']), g)]
        B += [(L(ln['who'], ln['la']), ln.get('gap', plat * 0.7 if same else plat))]
    def rep(items, n):
        out = []
        for k in range(n):
            out += items[:-1] + [(items[-1][0], 2.5)]
        return out

    n3 = int(job.get('repeat', 3))      # every track = the whole dialogue, 3 times
    tracks = [('a', rep(A, n3), f'English → Latin × {n3}', f' Each line in English, then in Latin. The whole dialogue {n3} times.'),
              ('b', rep(B, n3), f'Latin only × {n3}', f' Latin only. The whole dialogue {n3} times.')]
    if job.get('latin_loop'):           # optional extra long Latin loop
        k = int(job['latin_loop'])
        tracks.append(('c', rep(B, k), f'Latin only × {k}', f' Latin only, {k} times in a row (a long loop).'))

    music = MUSIC.get(job.get('music', 'v5'), MUSIC['v5'])
    lvl, dip = job.get('music_level_db', -7), job.get('music_dip_db', 7)
    num = int(job['number']); season = int(job.get('season', 1)); slug = job['slug']; title = job['title']
    eps = json.load(open('episodes.json'))
    pre = f's{season}e{num:02d}'
    for e in [e for e in eps if e['file'].startswith(pre)]:   # a remake replaces the old version
        if os.path.exists('episodes/' + e['file']):
            os.remove('episodes/' + e['file'])
    eps = [e for e in eps if not e['file'].startswith(pre)]
    nxt = max([e['episode'] for e in eps] + [0]) + 1
    cover = audio.make_cover('cover.jpg', f'Ep {num} · {title}', f'episodes/s{season}e{num:02d}-cover.jpg')
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=11)))
    made = []
    for code, items, label, extra in tracks:
        summ = job.get('summary', '') + extra
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
            res.update({'audition': run_audition, 'test': run_test}.get(job['type'], run_episode)(job)); res['ok'] = True
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

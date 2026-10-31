"""Small ElevenLabs API client (text to speech, voice library). Needs env ELEVENLABS_API_KEY."""
import os, time, json
import requests

API = 'https://api.elevenlabs.io/v1'
LOG = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    LOG.append(s)


def _headers():
    k = os.environ.get('ELEVENLABS_API_KEY', '').strip()
    if not k:
        raise RuntimeError('ELEVENLABS_API_KEY is not set (GitHub: Settings > Secrets and variables > Actions).')
    return {'xi-api-key': k}


def req(method, path, **kw):
    r = None
    for i in range(5):
        r = requests.request(method, API + path, headers=_headers(), timeout=180, **kw)
        if r.status_code == 429 or r.status_code >= 500:
            time.sleep(4 * (i + 1)); continue
        return r
    return r


_MODEL = None


def pick_model():
    """Prefer Eleven v4, then v3, then multilingual v2."""
    global _MODEL
    if _MODEL:
        return _MODEL
    want = ['eleven_v4', 'eleven_v3', 'eleven_multilingual_v2']
    try:
        r = req('GET', '/models')
        if r.status_code == 200:
            ids = [m.get('model_id') for m in r.json()]
            log('models available:', ', '.join(i for i in ids if i))
            for w in want:
                if w in ids:
                    _MODEL = w; break
            if not _MODEL:
                v4 = [i for i in ids if i and 'v4' in i]
                _MODEL = v4[0] if v4 else want[1]
        else:
            log('models list:', r.status_code, r.text[:200]); _MODEL = want[0]
    except Exception as e:
        log('models list failed:', e); _MODEL = want[0]
    log('model:', _MODEL)
    return _MODEL


def tts(voice_id, text, out, stability=0.2, similarity=0.75, model=None):
    """Render one clip to an MP3 file. Falls back on stability and model when the API refuses.
    model given (e.g. the half-price eleven_flash_v2_5): that model only, never a silent switch to a full-price one."""
    global _MODEL
    if model:
        tries = [(model, stability), (model, 0.5)]
    else:
        model = pick_model()
        tries = [(model, stability), (model, 0.5), ('eleven_v3', 0.5), ('eleven_multilingual_v2', 0.5)]
    last = ''
    for m, st in tries:
        body = {'text': text, 'model_id': m, 'voice_settings': {'stability': st, 'similarity_boost': similarity}}
        r = req('POST', f'/text-to-speech/{voice_id}?output_format=mp3_44100_128', json=body)
        if r.status_code == 200 and r.content:
            open(out, 'wb').write(r.content)
            if not tries[0][0] == m and _MODEL and m != _MODEL:
                log('switched model to', m); _MODEL = m
            return m
        last = f'{r.status_code} {r.text[:300]}'
        log(f'TTS refused ({m}, stability {st}):', last)
        if r.status_code in (401, 403):
            break
    raise RuntimeError('TTS failed: ' + last)


def my_voices():
    r = req('GET', '/voices')
    if r.status_code != 200:
        log('voices list:', r.status_code, r.text[:200]); return []
    return r.json().get('voices', [])


def shared_voices(gender, accent='australian', n=3):
    params = {'page_size': 40, 'gender': gender, 'accent': accent, 'language': 'en'}
    r = req('GET', '/shared-voices', params=params)
    if r.status_code != 200:
        log('shared voices:', r.status_code, r.text[:200]); return []
    vs = [v for v in r.json().get('voices', []) if 'austral' in (v.get('accent') or '').lower()]
    vs.sort(key=lambda v: -(v.get('cloned_by_count') or 0))
    return vs[:n]


def pick_shared(accent, gender, prefer=('conversational', 'natural', 'warm')):
    """Best library voice for an accent + gender: conversational first, then most cloned."""
    r = req('GET', '/shared-voices', params={'page_size': 60, 'gender': gender, 'accent': accent})
    if r.status_code != 200:
        log('shared voices:', r.status_code, r.text[:200]); return None
    vs = [v for v in r.json().get('voices', []) if accent in (v.get('accent') or '').lower()]
    def score(v):
        txt = ' '.join(str(v.get(k) or '') for k in ('name', 'description', 'use_case', 'descriptive')).lower()
        return (sum(w in txt for w in prefer), v.get('cloned_by_count') or 0)
    vs.sort(key=score, reverse=True)
    for v in vs[:5]:
        log('  candidate:', v.get('name'), '|', v.get('use_case'), '|', v.get('cloned_by_count'))
    return vs[0] if vs else None


def add_shared(v):
    """Add a library voice to my voices; returns the new voice id (or None)."""
    r = req('POST', f"/voices/add/{v['public_owner_id']}/{v['voice_id']}", json={'new_name': v['name'][:40]})
    if r.status_code == 200:
        return r.json().get('voice_id')
    log('add voice failed:', v.get('name'), r.status_code, r.text[:200])
    return None


def subscription():
    """Credits: {used, limit, left, resets (unix s), tier}."""
    r = req('GET', '/user/subscription')
    if r.status_code != 200:
        raise RuntimeError(f'subscription: {r.status_code} {r.text[:200]}')
    j = r.json()
    used, lim = j.get('character_count', 0), j.get('character_limit', 0)
    return {'used': used, 'limit': lim, 'left': lim - used, 'resets': j.get('next_character_count_reset_unix'),
            'tier': j.get('tier'), 'status': j.get('status')}


def sound_effect(text, out, seconds=None):
    """ElevenLabs sound effects (text -> sound). Returns True on success."""
    body = {'text': text, 'prompt_influence': 0.5}
    if seconds: body['duration_seconds'] = seconds
    r = req('POST', '/sound-generation', json=body)
    if r.status_code == 200 and r.content:
        open(out, 'wb').write(r.content); return True
    log('sound effect refused:', r.status_code, r.text[:200]); return False


def music(prompt, out, ms=30000):
    """Eleven Music (text -> song). Returns True on success."""
    r = req('POST', '/music', json={'prompt': prompt, 'music_length_ms': ms})
    if r.status_code == 200 and r.content:
        open(out, 'wb').write(r.content); return True
    log('music refused:', r.status_code, r.text[:300]); return False


def pick_character_voices(n=2, exclude=()):
    """Playful female character voices from the library (animation use case), most used first."""
    out = []
    for params in ({'gender': 'female', 'use_cases': 'characters_animation', 'page_size': 40},
                   {'gender': 'female', 'search': 'cartoon', 'page_size': 40},
                   {'gender': 'female', 'search': 'playful', 'page_size': 40}):
        r = req('GET', '/shared-voices', params=params)
        if r.status_code != 200:
            log('shared voices:', r.status_code, r.text[:200]); continue
        vs = [v for v in r.json().get('voices', []) if 'americ' not in (v.get('accent') or '').lower()]
        vs.sort(key=lambda v: -(v.get('cloned_by_count') or 0))
        for v in vs:
            if v['name'] not in exclude and v['name'] not in [o['name'] for o in out]:
                out.append(v)
            if len(out) >= n: return out
    return out

"""Move finished MP3s out of the website into a GitHub release (free, no 1 GB Pages limit).
Runs in the Action (needs GH_TOKEN and GITHUB_REPOSITORY). The feed points to the release files."""
import glob, json, os, subprocess

TAG = 'audio'


def _gh(*a, check=True):
    return subprocess.run(['gh', *a], capture_output=True, text=True, check=check)


def dur(p):
    s = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                             capture_output=True, text=True).stdout.strip())
    return f"{int(s // 60)}:{int(s % 60):02d}"


def shrink(p):
    """Speech-friendly size for free tracks: 64 kbps mono (about 60% smaller)."""
    tmp = p + '.small.mp3'
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', p, '-map', '0', '-ac', '1', '-b:a', '64k', '-c:v', 'copy',
                    '-id3v2_version', '3', tmp], check=True)
    os.replace(tmp, p)


MODE = 'pages'   # 27 Oct: Apple Podcasts said "can't be played on this device" for release files (served as a download,
                 # application/octet-stream). The MP3s live in the website again (audio/mpeg). 'release' = the old way.


def keep_in_site(log=print):
    """Pages mode: the MP3 stays in episodes/ (the workflow commits it); the feed points to the website."""
    eps = json.load(open('episodes.json')); by = {e['file']: e for e in eps}; n = 0
    for p in sorted(glob.glob('episodes/*.mp3')):
        fn = os.path.basename(p)
        if fn in by:
            e = by[fn]
            if e.get('url') or e.get('host') != 'pages' or not e.get('bytes'):
                e.pop('url', None); e['host'] = 'pages'; e['bytes'] = os.path.getsize(p); e['duration'] = dur(p); n += 1
    json.dump(eps, open('episodes.json', 'w'), indent=1, ensure_ascii=False)
    repo = os.environ.get('GITHUB_REPOSITORY', 'pjbran/sermones-feed')
    subprocess.run(['python3', 'build_feed.py', 'https://' + repo.split('/')[0] + '.github.io/' + repo.split('/')[1]], check=True)
    log('kept in the website:', n, 'files updated')
    return n


def bring_back(log=print):
    """Download every release MP3 that the feed uses into episodes/ (job type "to_pages")."""
    eps = json.load(open('episodes.json')); os.makedirs('episodes', exist_ok=True); n = 0
    for e in eps:
        fn = e['file']
        if not os.path.exists('episodes/' + fn):
            r = _gh('release', 'download', TAG, '-p', fn, '-D', 'episodes', '--clobber', check=False)
            if r.returncode != 0:
                log('could not bring back', fn, r.stderr[:200]); continue
            n += 1
    log('brought back', n, 'MP3s from the release')
    return n


def publish_all(log=print, shrink_free=False):
    if MODE == 'pages':
        return keep_in_site(log)
    repo = os.environ.get('GITHUB_REPOSITORY')
    if not (repo and os.environ.get('GH_TOKEN')):
        log('publish: no GH_TOKEN / GITHUB_REPOSITORY, files stay in the site'); return 0
    files = sorted(glob.glob('episodes/*.mp3'))
    if not files:
        return 0
    if _gh('release', 'view', TAG, check=False).returncode != 0:
        _gh('release', 'create', TAG, '--title', 'Audio files', '--notes', 'MP3s for the Sermones feed.')
    eps = json.load(open('episodes.json'))
    by = {e['file']: e for e in eps}
    n = 0
    for p in files:
        fn = os.path.basename(p)
        if fn not in by or by[fn].get('host') == 'pages':   # kept in the website (27 Oct: playback test)
            continue
        if shrink_free and fn.startswith('bonus-'):
            shrink(p)
        by[fn]['bytes'] = os.path.getsize(p); by[fn]['duration'] = dur(p)
        _gh('release', 'upload', TAG, p, '--clobber')
        by[fn]['url'] = f'https://github.com/{repo}/releases/download/{TAG}/{fn}'
        os.remove(p); n += 1
        log('published to release:', fn, by[fn]['bytes'] // 1024, 'KB')
    json.dump(eps, open('episodes.json', 'w'), indent=1, ensure_ascii=False)
    subprocess.run(['python3', 'build_feed.py', 'https://' + repo.split('/')[0] + '.github.io/' + repo.split('/')[1]], check=True)
    return n

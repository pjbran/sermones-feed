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


def publish_all(log=print, shrink_free=False):
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

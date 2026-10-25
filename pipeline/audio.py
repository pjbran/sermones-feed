"""Audio helpers: decode, trim, stitch, music bed with ducking, loudness, tags, cover."""
import subprocess, wave, os
import numpy as np

SR = 44100


def load(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, '<i2').astype(np.float32) / 32768


def trim(x, thr_db=-45, pad=0.04):
    """Cut the silence the TTS adds at both ends."""
    n = int(0.01 * SR)
    if len(x) < n * 3:
        return x
    e = np.array([np.sqrt(np.mean(x[i:i + n] ** 2) + 1e-12) for i in range(0, len(x) - n, n)])
    on = np.where(20 * np.log10(e) > thr_db)[0]
    if not len(on):
        return x
    a = max(0, on[0] * n - int(pad * SR)); b = min(len(x), (on[-1] + 1) * n + int(pad * 2 * SR))
    return fade(x[a:b])


def fade(x, ms=10):
    n = min(int(SR * ms / 1000), len(x) // 2)
    if n > 0:
        r = np.linspace(0, 1, n); x = x.copy(); x[:n] *= r; x[-n:] *= r[::-1]
    return x


def norm(x, target_db=-19.0):
    act = x[np.abs(x) > 0.02]
    rms = np.sqrt(np.mean(act ** 2)) if len(act) else 1e-3
    return x * (10 ** (target_db / 20) / rms)


def sil(s):
    return np.zeros(int(s * SR), np.float32)


def sequence(items, lead=1.2, tail=3.0):
    """items: list of (clip, gap_after). Returns (voice track, list of (start, end) in seconds)."""
    parts, ev, t = [sil(lead)], [], lead
    for x, gap in items:
        ev.append((t, t + len(x) / SR)); parts += [x, sil(gap)]; t += len(x) / SR + gap
    parts.append(sil(tail))
    return np.concatenate(parts), ev


def mix_music(voice, ev, loop_path, level_db=-9.0, dip_db=7.0):
    if not loop_path:
        return voice
    m = load(loop_path)
    m = m * (10 ** (-24 / 20) / np.sqrt(np.mean(m ** 2)))
    total = len(voice)
    m = np.tile(m, int(np.ceil(total / len(m))) + 1)[:total]
    base, low = 10 ** (level_db / 20), 10 ** ((level_db - dip_db) / 20)
    target = np.full(total, base)
    for i, (a, b) in enumerate(ev):
        nxt = ev[i + 1] if i + 1 < len(ev) else None
        s = int(max(0, a - 0.08) * SR)
        e = int((b + 0.05) * SR) if (not nxt or nxt[0] - b > 0.35) else int(max(0, nxt[0] - 0.08) * SR)
        target[s:e] = low
    end = int(((ev[-1][1] if ev else 0) + 0.5) * SR); target[end:] = 0
    # one-pole smoothing (fast down, slow up), done in blocks of 10 ms for speed
    hop = int(0.01 * SR); tb = target[::hop]; g = np.zeros_like(tb)
    for i in range(1, len(tb)):
        k = 0.5 if tb[i] < g[i - 1] else 0.04
        if tb[i] == 0: k = 0.012
        g[i] = g[i - 1] + k * (tb[i] - g[i - 1])
    g = np.repeat(g, hop)[:total]; g = np.pad(g, (0, total - len(g)), 'edge')
    ramp = np.clip(np.arange(total) / SR / 2.0, 0, 1)
    out = voice + m * g * ramp
    return out * min(1.0, 0.95 / np.max(np.abs(out)))


def save_mp3(x, path, tags, cover=None, bitrate='160k', channels=2):
    tmp = path + '.wav'
    with wave.open(tmp, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(x, -1, 1) * 32767).astype('<i2').tobytes())
    tmp2 = path + '.tmp.mp3'
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', tmp, '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11',
                    '-ac', str(channels), '-ar', '44100', '-b:a', bitrate, tmp2], check=True)
    cmd = ['ffmpeg', '-y', '-v', 'error', '-i', tmp2]
    if cover and os.path.exists(cover):
        cmd += ['-i', cover, '-map', '0:a', '-map', '1', '-metadata:s:v', 'title=Cover', '-metadata:s:v', 'comment=Cover (front)']
    cmd += ['-c', 'copy', '-id3v2_version', '3']
    for k, v in tags.items():
        cmd += ['-metadata', f'{k}={v}']
    subprocess.run(cmd + [path], check=True)
    os.remove(tmp); os.remove(tmp2)


def make_cover(base, text, out):
    try:
        from PIL import Image, ImageDraw, ImageFont
        img = Image.open(base).convert('RGB'); d = ImageDraw.Draw(img); W = img.width
        d.rectangle([0, int(W * 0.84), W, W], fill=(31, 58, 56))
        f = None
        for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf']:
            if os.path.exists(p):
                f = ImageFont.truetype(p, int(W * 0.055))
        if f:
            w = d.textlength(text, font=f); d.text(((W - w) / 2, int(W * 0.87)), text, font=f, fill=(244, 236, 220))
        img.save(out, quality=90)
        return out
    except Exception as e:
        print('cover failed:', e)
        return base


def debreath(x, speech_db=-25.0, keep_short_gap=0.20, pre=0.06, post=0.10, max_gap=0.35):
    """Remove breaths and 'hah' exhales: keep only speech (plus a small margin), silence the rest,
    cut lead/tail, and shorten long internal gaps. x must be normalised first (norm)."""
    n = int(0.01 * SR)
    if len(x) < n * 5:
        return x
    e = np.array([20 * np.log10(np.sqrt(np.mean(x[i:i + n] ** 2)) + 1e-9) for i in range(0, len(x) - n + 1, n)])
    core = e > speech_db
    if not core.any():
        return x
    idx = np.where(core)[0]
    # join speech regions that are close (gaps inside words and short pauses stay untouched)
    regs = [[idx[0], idx[0]]]
    for i in idx[1:]:
        if (i - regs[-1][1]) * 0.01 <= keep_short_gap:
            regs[-1][1] = i
        else:
            regs.append([i, i])
    parts = []
    for k, (a, b) in enumerate(regs):
        s = max(0, int((a * 0.01 - pre) * SR)); t = min(len(x), int(((b + 1) * 0.01 + post) * SR))
        if parts:
            prev_end = parts[-1][1]
            s = max(s, prev_end)
        parts.append((s, t))
    out = []
    for k, (s, t) in enumerate(parts):
        if k:
            gap = (s - parts[k - 1][1]) / SR
            out.append(sil(min(max(gap, 0.0), max_gap)))
        out.append(fade(x[s:t], 8))
    return np.concatenate(out)

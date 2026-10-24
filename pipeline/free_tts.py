"""Free voices (no ElevenLabs credits): Piper, an open-source neural TTS that runs in the GitHub Action.
Latin is respelled for an ITALIAN voice so it comes out in classical pronunciation (hard c and g, v = w, ae = ai)."""
import os, re, subprocess, sys, unicodedata

DATA = 'piper-voices'


def ensure(voice):
    os.makedirs(DATA, exist_ok=True)
    if not os.path.exists(f'{DATA}/{voice}.onnx'):
        subprocess.run([sys.executable, '-m', 'piper.download_voices', '--download-dir', DATA, voice], check=True)
    return f'{DATA}/{voice}.onnx'


_VOICES = {}


def say(voice, text, out_wav, length_scale=1.0):
    """Synthesize with the voice kept in memory (much faster than one process per line)."""
    import wave
    from piper import PiperVoice, SynthesisConfig
    if voice not in _VOICES:
        _VOICES[voice] = PiperVoice.load(ensure(voice))
    v = _VOICES[voice]
    with wave.open(out_wav, 'wb') as wf:
        if length_scale != 1.0:
            v.synthesize_wav(text, wf, syn_config=SynthesisConfig(length_scale=length_scale))
        else:
            v.synthesize_wav(text, wf)
    return out_wav


def latin_for_italian(t):
    """Classical Latin -> Italian spelling that an Italian voice reads with classical sounds."""
    t = unicodedata.normalize('NFD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))   # no macrons (the voice cannot use them)
    t = t.replace('ae', 'ai').replace('Ae', 'Ai').replace('oe', 'oi')
    t = t.replace('ph', 'f').replace('th', 't').replace('Th', 'T').replace('y', 'i')
    t = re.sub(r'ch', 'c', t)
    t = re.sub(r'sc(?=[eiEI])', 'sch', t)                          # scis -> schis (not "shis")
    t = re.sub(r'([cC])(?=[eiEI])', lambda m: m.group(1) + 'h', t)  # Cicero -> Chichero = /kikero/
    t = re.sub(r'([gG])(?=[eiEI])', lambda m: m.group(1) + 'h', t)  # gens -> ghens = /gens/
    t = re.sub(r'(?<![qQ])v', 'u', t).replace('V', 'U')            # consonant v = w
    t = t.replace('x', 'cs')
    return t


if __name__ == '__main__':
    for s in ['Cicerō scrīpsit: dum anima est, spēs esse dīcitur.', 'Rem tenē, verba sequentur.', 'Scīsne quid Horātius dīcat?']:
        print(s, '->', latin_for_italian(s))


def latin_ipa(t, pad=False, v_as_v=False):
    """Classical Latin -> IPA with stress and long vowels (eSpeak's Latin rules, built into Piper),
    sent to the voice as raw phonemes, so it does not guess (dormīvī -> dɔrmˈiːwiː)."""
    import piper
    from piper.phonemize_espeak import EspeakPhonemizer
    global _PH
    try:
        _PH
    except NameError:
        _PH = EspeakPhonemizer(os.path.join(os.path.dirname(piper.__file__), 'espeak-ng-data'))
    ipa = ' '.join(''.join(s) for s in _PH.phonemize('la', unicodedata.normalize('NFC', t)))
    ipa = ipa.replace('ʲ', '')
    if v_as_v:   # letter v said as [v] (Church style), but qu / gu stay kw / gw
        ipa = re.sub(r'(?<![kɡgs])w', 'v', ipa)
    if pad:   # a short pause after the last word, so the voice finishes the last syllable
        ipa = ipa.rstrip() + ' ...'
    return '[[ ' + ipa + ' ]]'

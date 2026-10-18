"""Smart spelling: classical Latin (with macrons) -> letters the ElevenLabs voices say correctly.
Tested 17 Oct 2026: this gives a rolled R and long vowels; IPA gave a German R."""
import re, unicodedata

# words that start with a consonantal i but are not caught by the rule below
EXTRA_J = {}


def smart(t: str) -> str:
    t = unicodedata.normalize('NFC', t)
    t = re.sub(r'\b([Ii])(?=[aeouāēōūAEOU])', lambda m: 'J' if m.group(1) == 'I' else 'j', t)  # iam -> jam
    t = re.sub(r'(?<=[sS])u(?=[ēeāa]t)', 'w', t)  # cōnsuētūdō -> kōnswētūdō
    t = t.replace('qu', 'kw').replace('Qu', 'Kw')
    t = re.sub(r'(?<=n)gu(?=[aeiouāēīōū])', 'gw', t)  # lingua -> lingwa
    t = t.replace('ae', 'ai').replace('Ae', 'Ai').replace('oe', 'oi')
    t = t.replace('ch', 'k').replace('ph', 'p').replace('th', 't').replace('Ch', 'K').replace('Ph', 'P').replace('Th', 'T')
    t = t.replace('x', 'ks')
    t = t.replace('v', 'w').replace('V', 'W')
    t = t.replace('c', 'k').replace('C', 'K')
    return t


if __name__ == '__main__':
    for s in ['Salvē, Marce! Iamne vigilās?', 'Mea cōnsuētūdō est mātūrē surgere.', 'Quid in linguā Latīnā?']:
        print(s, '->', smart(s))

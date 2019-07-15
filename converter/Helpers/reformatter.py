import re
def reformat(sentence : str) -> str:
    sentence = re.sub('^-+|-+$|', "", sentence)
    sentence = re.sub('\s+\-\s+', "-", sentence)
    sentence = re.sub('\s{2,}|-\s+', " ", sentence)
    sentence = re.sub('\W+-', ", ", sentence)
    return  sentence

def normalize_kobo(parts: list, round_kobo=False):
    int_parts = list(map(int, parts))

    if int_parts[1] > 99 and round_kobo:
        int_parts[0] += (int_parts[1] // 100)
        int_parts[1] -= 100 * (int_parts[1] // 100)

    return int_parts
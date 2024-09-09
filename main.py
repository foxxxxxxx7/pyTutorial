VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
def translate(text):
    words = text.split()
    result = []
    for w in words:
        if w[:2] == 'yt':
            result.append(w + 'ay')
        elif w[0] == 'y':
            result.append(w[1:] + 'yay')
        elif w[:2] == 'xr' or w[0] in VOWELS:
            result.append(w + 'ay')
        elif 'qu' in w:
            index_u = w.find('qu') + 2
            result.append(w[index_u:] + w[:index_u] + 'ay')
        elif w[0] not in VOWELS:
            for i, l in enumerate(w):
                if l in VOWELS:
                    result.append(w[i:] + w[:i] + 'ay')
                    break
    return ' '.join(result)
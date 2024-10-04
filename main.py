VOWELS = {'a', 'e', 'i', 'o', 'u', 'y'}
EXCEPTIONS = {'xr', 'yt'}
SUFFIX = 'ay'


def translate_word(word):
    if word[:2] in EXCEPTIONS or word[0] in VOWELS - {'y'}:
        return f"{word}{SUFFIX}"

    if word[0] == 'y':
        return f"{word[1:]}y{SUFFIX}"

    if (qu_index := word.find('qu')) != -1:
        return f"{word[qu_index + 2:]}{word[:qu_index + 2]}{SUFFIX}"

    for i, letter in enumerate(word):
        if letter in VOWELS:
            return f"{word[i:]}{word[:i]}{SUFFIX}"
    return word


def translate(text):
    words = text.split()
    result = (translate_word(word) for word in words)
    return ' '.join(result)

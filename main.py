from collections import defaultdict


def count_words(sentence):
    sentence = sentence.lower().translate(str.maketrans(",:._!&@$%^", " " * 10)).strip("'")
    words = sentence.split()

    result = defaultdict(int)
    for word in words:
        word = word.strip("'")
        result[word] += 1

    return dict(result)
def count_words(sentence):
    result = {}
    sentence = sentence.lower().translate(str.maketrans(",:._!&@$%^", "          ")).strip("'")
    words = sentence.lower().split()
    for word in words:
        word = word.strip("'")
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

def find_anagrams(word, candidates):
    sorted_word = sorted(word.lower())
    return [c for c in candidates if sorted(c.lower()) == sorted_word and c.lower() != word.lower()]
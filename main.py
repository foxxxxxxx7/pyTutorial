def find_anagrams(word, candidates):
    matches = []
    sorted_word = list(sorted(word.lower()))
    for c in candidates:
        check = list(sorted(c.lower()))
        if check == sorted_word:
            matches.append(c)
        if c.lower() == word.lower():
            matches.remove(c)
    return matches
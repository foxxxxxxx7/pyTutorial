from string import ascii_lowercase as letters

def is_pangram(sentence):
    return all((letter in sentence.lower()) for letter in letters)
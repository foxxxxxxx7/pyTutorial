def abbreviate(phrase):
    return ''.join(word[0].upper() for word in phrase.replace('-', ' ').replace('_', '').split())
PLAIN = 'abcdefghijklmnopqrstuvwxyz'
DIGITS = '1234567890'


def encode(plain_text):
    cipher = ''
    for c in plain_text.lower():
        if c in PLAIN:
            index = PLAIN.index(c) + 1
            cipher += PLAIN[-index]
        elif c in DIGITS:
            cipher += c
        continue

    return ' '.join(cipher[i:i + 5] for i in range(0, len(cipher), 5))


def decode(ciphered_text):
    plain = ciphered_text.replace(' ', '')
    result = ''
    for c in plain:
        if c in PLAIN:
            index = PLAIN.index(c) + 1
            result += PLAIN[-index]
        if c in DIGITS:
            result += c
    return result
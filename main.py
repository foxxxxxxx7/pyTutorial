from random import randint


class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join([chr(ord('a') + randint(0, 25)) for i in range(100)])
        else:
            self.key = key

    def encode(self, text):
        return self.shift_text(text, direction=1)

    def decode(self, text):
        return self.shift_text(text, direction=-1)

    def shift_text(self, text, direction):
        result = []
        key_length = len(self.key)

        for i, char in enumerate(text):
            shift = ord(self.key[i % key_length]) - ord('a')
            shifted_char = chr((ord(char) - ord('a') + direction * shift) % 26 + ord('a'))
            result.append(shifted_char)

        return ''.join(result)

def rotate(text, key):
    cipher = []
    letters_list = list('abcdefghijklmnopqrstuvwxyz')

    def get_final_index(letter, key):
        letter_index = letters_list.index(letter)
        final_index = letter_index + key
        if final_index > 25:
            final_index -= 26
        return final_index

    for c in text:
        if c.isupper():
            final_index = get_final_index(c.lower(), key)
            cipher.append(letters_list[final_index].upper())
        elif c not in letters_list:
            cipher.append(c)
        else:
            final_index = get_final_index(c, key)
            cipher.append(letters_list[final_index])

    return ''.join(cipher)
LETTERS =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rows(letter):
    result = []
    l_index = LETTERS.index(letter)
    for i in range(l_index + 1):
        if i == 0:  
            result.append(' ' * l_index + LETTERS[i] + ' ' * l_index)
        else:  
            inner_spaces = 2 * i - 1
            result.append(' ' * (l_index - i) + LETTERS[i] + ' ' * inner_spaces + LETTERS[i] + ' ' * (l_index - i))
    return result + result[-2::-1]
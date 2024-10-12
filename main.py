def is_isogram(string):
    string = ''.join(filter(str.isalpha, string)).lower()

    return len(string) == len(set(string))

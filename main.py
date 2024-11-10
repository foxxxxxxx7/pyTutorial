# Possible sublist categories
EQUAL = 1
UNEQUAL = 2
SUBLIST = 3
SUPERLIST = 4


def sublist(list_one, list_two):
    len_one, len_two = len(list_one), len(list_two)

    if list_one == list_two:
        return EQUAL
    elif len_one < len_two:
        for i in range(len_two - len_one + 1):
            if list_two[i:i + len_one] == list_one:
                return SUBLIST
    elif len_one > len_two:
        for i in range(len_one - len_two + 1):
            if list_one[i:i + len_two] == list_two:
                return SUPERLIST

    return UNEQUAL

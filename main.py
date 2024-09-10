SUBLIST = 3
SUPERLIST = 4
EQUAL = 1
UNEQUAL = 2


def sublist(list_one, list_two):
    len_one = len(list_one)
    len_two = len(list_two)

    if list_one == list_two:
        return EQUAL
    if len_one < len_two:
        for i in range(len_two - len_one + 1):
            if list_two[i: i + len_one] == list_one:
                return SUBLIST
    if len_one > len_two:
        for i in range(len_one - len_two + 1):
            if list_one[i: i + len_two] == list_two:
                return SUPERLIST
    return UNEQUAL
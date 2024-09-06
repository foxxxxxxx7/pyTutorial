def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for list in lists:
        for item in list:
            result.append(item)
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result.append(item)
        else:
            pass
    return result


def length(list):
    count = 0
    for item in list:
        count += 1
    return count


def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    for item in reversed(list):
        initial = function(initial, item)
    return initial


def reverse(list):
    result = []
    while len(list) > 0:
        result.append(list.pop())
    return result

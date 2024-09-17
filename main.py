def decode(string):
    result = ''
    multiply = 0
    for s in string:
        if s.isdigit():
            multiply = (multiply * 10) + int(s)
        else:
            result += max(1, multiply) * s
            multiply = 0
    return result
def encode(string):
    prev_s = ''
    count = 1
    result = ''
    for s in string:
        if s == prev_s or s == '':
            count += 1
            prev_s = s
        elif s != prev_s:
            if count != 1:
                result += str(count) + prev_s
                count = 1
                prev_s = s
            else:
                result += prev_s
                count = 1
                prev_s = s
    if count != 1:
        result += str(count) + prev_s
    else:
        result += prev_s
    return result
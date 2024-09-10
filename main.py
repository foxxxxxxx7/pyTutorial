def is_paired(input_string):
    bracket_pairs = {"(": ")", "{": "}", "[": "]"}
    stack = []

    for c in input_string:
        if c in bracket_pairs.keys():
            stack.append(c)
        elif c in bracket_pairs.values():
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if bracket_pairs[last_open] != c:
                return False

    return len(stack) == 0
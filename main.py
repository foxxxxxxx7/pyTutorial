def sum_of_multiples(limit, multiples):
    result = set()
    for m in multiples:
        if m != 0:
            for n in range(m, limit, m):  # Start from m, step by m
                result.add(n)
    return sum(result)

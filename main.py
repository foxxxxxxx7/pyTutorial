def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')

    result = []
    i = 2
    while len(result) < number:
        if is_prime(i):
            result.append(i)
        i += 1
    return result.pop()


def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True
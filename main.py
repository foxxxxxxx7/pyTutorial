def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes(limit):
    result = []
    for n in range(limit + 1):
        if is_prime(n):
            result.append(n)
        pass
    return result

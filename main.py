def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    factors = []
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    for n in range(1, number):
        if number % n == 0:
            factors.append(n)
    if sum(factors) == number:
        return 'perfect'
    if sum(factors) > number:
        return 'abundant'
    if sum(factors) < number:
        return 'deficient' .
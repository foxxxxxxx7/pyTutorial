def is_armstrong_number(number):
    """
    Determine if a given number is an Armstrong number.

    An Armstrong number (or narcissistic number) is a number that is equal to the sum of its digits
    each raised to the power of the number of digits in the number.

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.

    """
    power = len(str(number))
    result = 0

    for digit in str(number):
        result += int(digit) ** power

    return result == number
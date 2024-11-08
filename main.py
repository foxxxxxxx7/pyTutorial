def square(number):
    """
    Calculate the number of grains of rice on a specific square of a chessboard
    where the number of grains doubles on each subsequent square.

    The chessboard has 64 squares, and the number of grains on each square
    corresponds to 2 raised to the power of (square number - 1).

    Args:
        number (int): The square number (must be between 1 and 64 inclusive).

    Returns:
        int: The number of grains of rice on the given square.

    Raises:
        ValueError: If the square number is not between 1 and 64.
    """
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")


def total():
    """
    Calculate the total number of grains of rice on a chessboard if the number
    of grains doubles on each subsequent square.

    Returns:
        int: The total number of grains of rice on all 64 squares of the chessboard.
    """
    return (2 ** 64) - 1

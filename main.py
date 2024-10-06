def is_valid_triangle(a, b, c):
    return a + b >= c and b + c >= a and a + c >= b


def equilateral(sides):
    """
    Determine if a triangle is equilateral.

    An equilateral triangle has all three sides equal and none of the sides should be zero.

    Args:
        sides (list or tuple of three numbers): The lengths of the three sides of the triangle.

    Returns:
        bool: True if the triangle is equilateral, False otherwise.
    """
    a, b, c = sides
    return a == b and a == c and a != 0


def isosceles(sides):
    """
    Determine if a triangle is isosceles.

    An isosceles triangle has at least two sides of equal length. Additionally, the sum of the lengths
    of any two sides must be greater than or equal to the length of the remaining side.

    Args:
        sides (list or tuple of three numbers): The lengths of the three sides of the triangle.

    Returns:
        bool: True if the triangle is isosceles, False otherwise.
    """
    a, b, c = sides
    return is_valid_triangle(a, b, c) and (a == b or a == c or b == c)


def scalene(sides):
    """
    Determine if a triangle is scalene.

    A scalene triangle has all three sides of different lengths. Additionally, the sum of the lengths
    of any two sides must be greater than or equal to the length of the remaining side.

    Args:
        sides (list or tuple of three numbers): The lengths of the three sides of the triangle.

    Returns:
        bool: True if the triangle is scalene, False otherwise.
    """
    a, b, c = sides
    return is_valid_triangle(a, b, c) and (a != b != c != a)

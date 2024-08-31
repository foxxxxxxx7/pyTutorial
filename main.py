def is_valid(isbn):
    """
    Validates a 10-digit ISBN number.

    This function checks if the given ISBN string is a valid 10-digit ISBN. It considers
    ISBN numbers with or without hyphens. The validation follows the ISBN-10 checksum formula:
    - The first 9 characters should be digits.
    - The last character can be a digit or the letter 'X', which represents the value 10.
    - The checksum is calculated by multiplying each of the first 9 digits by a decreasing
      weight from 10 to 2, and adding the last character (or its value if it's 'X') to the result.
    - The total sum, including the last character, must be divisible by 11 for the ISBN to be valid.

    Args:
        isbn (str): The ISBN number to be validated, which may include hyphens.

    Returns:
        bool: True if the ISBN is valid, False otherwise.

    """
    iteration = 10
    result = 0
    isbn = list(isbn.replace("-", ""))
    if len(isbn) != 10:
        return False

    final_char = isbn.pop()
    for character in isbn:
        if character.isalpha():
            return False

    if final_char == 'X':
        final_char = 10
    elif not final_char.isdigit():
        return False

    for character in isbn:
        result += int(character) * iteration
        iteration -= 1
    return (result + int(final_char)) % 11 == 0

NUMBER_DICT = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
    1000000: 'million',
    1000000000: 'billion'
}


def say(number):
    if 0 > number or number >= 1_000_000_000_000:
        raise ValueError("input out of range")

    result = ''
    counter = 1
    number_str = str(number)[::-1]
    if len(number_str) > 3:
        for i in range(0, len(number_str), 3):
            chunk = number_str[i:i + 3][::-1]
            chunk_value = int(chunk)
            if counter == 1:
                result = f'{three_digits(chunk_value)} {result}'
            elif chunk_value != 0:
                result = f'{three_digits(chunk_value)} {NUMBER_DICT[counter]} {result}'
            counter *= 1000
        result = result.replace('zero', '')
        return result.strip()
    return three_digits(number)


def three_digits(number):
    result = ''
    if number >= 100:
        first_digit = (number % 100) % 10
        second_digit = (number % 100) - first_digit
        third_digit = (number - (second_digit + first_digit)) / 100
        if number % 100 == 0:
            result += f'{NUMBER_DICT[third_digit]} {NUMBER_DICT[100]}'
        elif number % ((third_digit * 10) + (second_digit / 10)) == 0:
            result += f'{NUMBER_DICT[third_digit]} {NUMBER_DICT[100]} {NUMBER_DICT[second_digit]}'
        else:
            result += f'{NUMBER_DICT[third_digit]} {NUMBER_DICT[100]} {NUMBER_DICT[second_digit]}-{NUMBER_DICT[first_digit]}'

    elif number >= 20 and number % 10 != 0:
        first_digit = number % 10
        second_digit = number - first_digit
        result += NUMBER_DICT[second_digit] + '-' + NUMBER_DICT[first_digit]
    else:
        result += NUMBER_DICT[number]
    return result
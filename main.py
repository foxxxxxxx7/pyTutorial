RESISTOR_VALUES = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7,
    'grey': 8, 'white': 9}


def label(colors):
    value = int(''.join(str(RESISTOR_VALUES[color]) for color in colors[:2]))
    exponent = RESISTOR_VALUES[colors[2]]
    final_value = value * (10 ** exponent)

    if 2 <= exponent <= 5:
        final_value //= 1000
        unit = "kiloohms"
    elif 6 <= exponent <= 8:
        final_value //= 1000000
        unit = "megaohms"
    elif 9 <= exponent <= 11:
        final_value //= 1000000000
        unit = "gigaohms"
    else:
        unit = "ohms"

    return f"{final_value} {unit}"

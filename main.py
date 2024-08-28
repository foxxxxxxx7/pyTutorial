RESISTOR_VALUES = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
TOLERANCE_VALUES = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5, 'brown': 1, 'red': 2, 'gold': 5, 'silver': 10}

def resistor_label(colors):
    if len(colors) == 4:
        digits, exponent_color, tolerance_color = colors[:2], colors[2], colors[3]
    else:
        digits, exponent_color, tolerance_color = colors[:3], colors[3], colors[4]

    value = int(''.join(str(RESISTOR_VALUES[color]) for color in digits))
    exponent = RESISTOR_VALUES[exponent_color]
    tolerance = TOLERANCE_VALUES[tolerance_color]

    final_value = value * (10 ** exponent)
    unit = " ohms"
    if exponent >= 9:
        final_value /= 10 ** 9
        unit = " gigaohms"
    elif exponent >= 6:
        final_value /= 10 ** 6
        unit = " megaohms"
    elif exponent >= 3:
        final_value /= 10 ** 3
        unit = " kiloohms"

    final_value = int(final_value) if final_value.is_integer() else final_value
    return f"{final_value}{unit} ±{tolerance}%"
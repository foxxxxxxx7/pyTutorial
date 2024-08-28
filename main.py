RESISTOR_VALUES = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7,
    'grey': 8, 'white': 9}
TOLERANCE_VALUES = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5, 'brown': 1, 'red': 2, 'gold': 5,
    'silver': 10, }


def resistor_label(colors):
    value = ""
    exponent = 0
    tolerance = 0
    unit = " ohms"
    if len(colors) == 4:
        for i, color in enumerate(colors):
            if i < 2:
                value += str(RESISTOR_VALUES[color])
            elif i == 2:
                exponent = RESISTOR_VALUES[color]
            elif i == 3:
                tolerance = TOLERANCE_VALUES[color]
    else:
        for i, color in enumerate(colors):
            if i < 3:
                value += str(RESISTOR_VALUES[color])
            elif i == 3:
                exponent = RESISTOR_VALUES[color]
            elif i == 4:
                tolerance = TOLERANCE_VALUES[color]

    final_value = (float(value) * (10 ** exponent))
    if len(colors) == 4:
        if 2 <= exponent <= 5:
            final_value = final_value / 1000
            unit = " kiloohms"
        elif 6 <= exponent <= 8:
            final_value = final_value / 1000 ** 2
            unit = " megaohms"
        elif 9 <= exponent <= 11:
            final_value = final_value / 1000 ** 3
            unit = " gigaohms"
    else:
        if 1 <= exponent <= 3:
            final_value = final_value / 1000
            unit = " kiloohms"
        elif 4 <= exponent <= 6:
            final_value = final_value / 1000 ** 2
            unit = " megaohms"
        elif 7 <= exponent <= 11:
            final_value = final_value / 1000 ** 3
            unit = " gigaohms"
    if final_value == 0:
        return f'{int(final_value)}{unit}'
    elif str(final_value)[-2:] == '.0':
        return f"{int(final_value)}{unit} ±{tolerance}%"
    return f"{final_value}{unit} ±{tolerance}%"

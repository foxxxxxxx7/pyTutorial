RESISTOR_VALUES = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3,
    'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7,
    'grey': 8, 'white': 9
}

TOLERANCE_VALUES = {
    'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5,
    'brown': 1, 'red': 2, 'gold': 5, 'silver': 10
}

def resistor_label(colors):
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

    sig_figs_count = 2 if len(colors) == 4 else 3
    value = int(''.join(str(RESISTOR_VALUES[color]) for color in colors[:sig_figs_count]))
    exponent = RESISTOR_VALUES[colors[sig_figs_count]]
    tolerance = TOLERANCE_VALUES.get(colors[-1], 0)

    final_value = value * (10 ** exponent)

    if final_value >= 1_000_000_000:
        final_value /= 1_000_000_000
        unit = "gigaohms"
    elif final_value >= 1_000_000:
        final_value /= 1_000_000
        unit = "megaohms"
    elif final_value >= 1_000:
        final_value /= 1000
        unit = "kiloohms"
    else:
        unit = "ohms"

    final_value_str = f"{final_value:.2f}".rstrip('0').rstrip('.') if isinstance(final_value, float) else str(int(final_value))
    return f"{final_value_str} {unit} ±{tolerance}%"
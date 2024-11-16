def convert_length(value, from_unit, to_unit):
    conversions = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "inches": 39.3701,
        "feet": 3.28084,
        "miles": 0.000621371
    }
    return value * conversions[to_unit] / conversions[from_unit]


def convert_weight(value, from_unit, to_unit):
    conversions = {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274
    }
    return value * conversions[to_unit] / conversions[from_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9 / 5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5 / 9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    else:
        return value  # No conversion needed for same units


def main():
    print("Welcome to the Unit Converter!")
    print("Conversion categories: length, weight, temperature")

    category = input("\nEnter a category to convert (length/weight/temperature): ").strip().lower()

    if category == "length":
        print("Available units: meters, kilometers, centimeters, inches, feet, miles")
        from_unit = input("Enter the unit to convert from: ").strip().lower()
        to_unit = input("Enter the unit to convert to: ").strip().lower()
        value = float(input("Enter the value to convert: "))
        result = convert_length(value, from_unit, to_unit)

    elif category == "weight":
        print("Available units: grams, kilograms, pounds, ounces")
        from_unit = input("Enter the unit to convert from: ").strip().lower()
        to_unit = input("Enter the unit to convert to: ").strip().lower()
        value = float(input("Enter the value to convert: "))
        result = convert_weight(value, from_unit, to_unit)

    elif category == "temperature":
        print("Available units: celsius, fahrenheit, kelvin")
        from_unit = input("Enter the unit to convert from: ").strip().lower()
        to_unit = input("Enter the unit to convert to: ").strip().lower()
        value = float(input("Enter the value to convert: "))
        result = convert_temperature(value, from_unit, to_unit)

    else:
        print("Invalid category.")
        return

    print(f"\nConverted value: {result:.2f} {to_unit}")


if __name__ == "__main__":
    main()

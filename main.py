weight = float(input("Enter weight: "))
unit = input("KG or lbs? (K or L): ").strip().lower()

if unit == "k":
    converted_weight = weight * 2.205
    unit = "lbs"
elif unit == "l":
    converted_weight = weight / 2.205
    unit = "kgs"
else:
    print(f"{unit.upper()} was not valid")
    exit()

print(f"Your weight is: {round(converted_weight, 1)} {unit.capitalize()}.")

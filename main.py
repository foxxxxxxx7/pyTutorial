basket = []
total = 0

while True:
    food = input("Enter the food you want to buy (q to Quit): ").strip()
    if food.lower() == "q":
        break
    try:
        price = float(input(f"Enter the price of {food}: €").strip())
        basket.append((food, price))
        total += price
    except ValueError:
        print("Please enter a valid price.")

print("\n------ YOUR BASKET ------")
print(", ".join(food for food, _ in basket))
print(f"Your total is: €{total:.2f}")

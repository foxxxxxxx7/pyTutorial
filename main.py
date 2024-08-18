menu = {"pizza": 5.00,
        "popcorn": 3.00,
        "chocolate": 2.00,
        "sweets": 1.50,
        "soda": 2.00,
        "water": 1.00,
        "nachos": 3.50,
        "chips": 4.00}

cart = []
total = 0

print("------------- MENU ---------------")
for key, value in menu.items():
    print(f"{key:10}: €{value:.2f}")
print("----------------------------------")

while True:
    food = input("Select an item(q to Quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------------- ORDER ---------------")
for food in cart:
       total += menu.get(food)
       print(food, end=" ")

print()
print(f"Total is: €{total:.2f}")

print("----------------------------------")
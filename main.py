menu = {
    "pizza": 5.00,
    "popcorn": 3.00,
    "chocolate": 2.00,
    "sweets": 1.50,
    "soda": 2.00,
    "water": 1.00,
    "nachos": 3.50,
    "chips": 4.00
}

def print_menu(menu):
    print("------------- MENU ---------------")
    for item, price in menu.items():
        print(f"{item:10}: €{price:.2f}")
    print("----------------------------------")

def take_order(menu):
    cart = []
    while (food := input("Select an item(q to Quit): ").lower()) != "q":
        if food in menu:
            cart.append(food)
        else:
            print("Item not on the menu. Please try again.")
    return cart

def print_order(cart, menu):
    total = sum(menu[item] for item in cart)
    print("------------- ORDER ---------------")
    print(" ".join(cart))
    print(f"Total is: €{total:.2f}")
    print("----------------------------------")

def main():
    print_menu(menu)
    cart = take_order(menu)
    print_order(cart, menu)

if __name__ == "__main__":
    main()

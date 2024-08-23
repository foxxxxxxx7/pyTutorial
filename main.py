def print_border():
    print("-----------------")


def show_balance(balance):
    print_border()
    print(f"Your balance is €{balance:.2f}")
    print_border()


def get_amount(action):
    print_border()
    amount = float(input(f"How much do you want to {action}?: "))
    print_border()
    if amount < 0:
        print("No negative numbers")
        return 0
    return amount


def deposit(balance):
    return balance + get_amount("deposit")


def withdraw(balance):
    amount = get_amount("withdraw")
    if amount > balance:
        print_border()
        print("Insufficient funds")
        print_border()
        return balance
    return balance - amount


def main():
    balance = 0
    actions = {
        "1": lambda: show_balance(balance),
        "2": lambda: deposit(balance),
        "3": lambda: withdraw(balance),
        "4": lambda: exit("Thanks for banking with us")
    }

    while True:
        print_border()
        print("Banking programme")
        print_border()
        print("1. Show Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        print_border()
        action = input("Enter your choice (1-4): ")
        print_border()
        balance = actions.get(action, lambda: print("Not an option"))()


if __name__ == "__main__":
    main()

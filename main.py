import random

def roll_dice(sides, count):
    """Rolls dice and returns the results."""
    return [random.randint(1, sides) for _ in range(count)]

def main():
    """Main function for the virtual dice roller."""
    print("Welcome to the Virtual Dice Roller!")
    while True:
        try:
            sides = int(input("\nEnter the number of sides on the dice (e.g., 6 for a standard dice): "))
            count = int(input("Enter the number of dice to roll: "))
            if sides <= 0 or count <= 0:
                print("Please enter positive integers for both sides and count.")
                continue
        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue

        results = roll_dice(sides, count)
        print(f"\nYou rolled: {results}")
        print(f"Total: {sum(results)}")

        retry = input("\nWould you like to roll again? (yes/no): ").strip().lower()
        if retry != "yes":
            print("Thanks for using the Virtual Dice Roller! Goodbye!")
            break

if __name__ == "__main__":
    main()

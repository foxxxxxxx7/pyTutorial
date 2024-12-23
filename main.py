import math


def is_prime(num):
    """Check if a number is a prime."""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def next_prime(start):
    """Find the next prime number greater than a given start."""
    num = start + 1
    while not is_prime(num):
        num += 1
    return num


def primes_up_to(limit):
    """Generate all primes up to a given limit."""
    return [num for num in range(2, limit + 1) if is_prime(num)]


def interactive_menu():
    """Interactive prime number explorer."""
    print("=== Prime Number Explorer ===")
    print("Choose an option:")
    print("1. Check if a number is prime")
    print("2. Find the next prime after a number")
    print("3. List all primes up to a number")
    print("4. Exit")

    while True:
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            try:
                num = int(input("Enter a number to check: "))
                if is_prime(num):
                    print(f"{num} is a prime number!")
                else:
                    print(f"{num} is not a prime number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            try:
                num = int(input("Enter a number to find the next prime after it: "))
                print(f"The next prime after {num} is {next_prime(num)}.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            try:
                limit = int(input("Enter an upper limit: "))
                primes = primes_up_to(limit)
                print(f"Primes up to {limit}: {primes}")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please select a valid option.")


# Run the explorer
interactive_menu()

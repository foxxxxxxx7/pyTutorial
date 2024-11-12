import random
import string


# Function to generate a password
def generate_password(length, include_uppercase, include_numbers, include_special_chars):
    # Base set of characters (lowercase letters)
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    # Ensure we have at least one character from each selected set
    password = []
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_numbers:
        password.append(random.choice(string.digits))
    if include_special_chars:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random characters
    password += random.choices(characters, k=length - len(password))

    # Shuffle the result to avoid predictable sequences
    random.shuffle(password)

    # Return the password as a string
    return ''.join(password)


# Function to get user input and generate a password
def main():
    print("Welcome to the Password Generator!")

    # Get password length
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length should be at least 4.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Get preferences for character types
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes" or "y"
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes" or "y"
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes" or "y"

    # Generate the password
    password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
    print(f"\nYour generated password: {password}")


if __name__ == "__main__":
    main()

import random

lowest_number, highest_number = 1, 100
answer = random.randint(lowest_number, highest_number)
guesses = 0

print("Python Number Guessing Game")
print(f"Select a number between {lowest_number} and {highest_number}")

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Invalid guess: Not a number")
        continue

    guess = int(guess)
    guesses += 1

    if not (lowest_number <= guess <= highest_number):
        print(f"Invalid guess: out of range. Select a number between {lowest_number} and {highest_number}")
    elif guess < answer:
        print("Too low, try again")
    elif guess > answer:
        print("Too high, try again")
    else:
        print(f"CORRECT! {answer} is correct. It took {guesses} guesses")
        break

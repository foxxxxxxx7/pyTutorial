import random
from wordlist import words

hangman_art = [
    "   \n   \n   ",
    " o \n   \n   ",
    " o \n | \n   ",
    " o \n/| \n   ",
    " o \n/|\\\n   ",
    " o \n/|\\\n/  ",
    " o \n/|\\\n/ \\"
]

def display_man(incorrect_guesses):
    print_border()
    print(hangman_art[incorrect_guesses])
    print_border()

def print_border():
    print('*************')

def main():
    answer = random.choice(words)
    hint = ['_'] * len(answer)
    guessed_letters = set()
    incorrect_guesses = 0

    while True:
        display_man(incorrect_guesses)
        print(' '.join(hint))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Invalid input! Enter a single letter.')
            continue

        if guess in guessed_letters:
            print(f'You already guessed "{guess}"!')
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
        else:
            incorrect_guesses += 1

        if '_' not in hint:
            display_man(incorrect_guesses)
            print(' '.join(answer))
            print('WINNER WINNER!!')
            break
        elif incorrect_guesses == len(hangman_art) - 1:
            display_man(incorrect_guesses)
            print(' '.join(answer))
            print('LOOOOOOOOOSER!!')
            break

if __name__ == '__main__':
    main()

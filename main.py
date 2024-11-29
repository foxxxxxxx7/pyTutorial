import random
import json

FLASHCARDS_FILE = "flashcards.json"


def load_flashcards():
    """Load flashcards from a file."""
    try:
        with open(FLASHCARDS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_flashcards(flashcards):
    """Save flashcards to a file."""
    with open(FLASHCARDS_FILE, "w") as file:
        json.dump(flashcards, file)


def create_flashcard(flashcards):
    """Create a new flashcard."""
    question = input("Enter the question: ").strip()
    answer = input("Enter the answer: ").strip()
    flashcards[question] = answer
    print("Flashcard added!")


def review_flashcards(flashcards):
    """Review flashcards with the user."""
    if not flashcards:
        print("No flashcards to review!")
        return

    questions = list(flashcards.keys())
    random.shuffle(questions)
    score = 0

    for question in questions:
        print(f"\nQuestion: {question}")
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == flashcards[question].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {flashcards[question]}")

    print(f"\nYour score: {score}/{len(questions)}")


def main():
    """Main function for the Flashcard Quiz App."""
    print("Welcome to the Flashcard Quiz App!")
    flashcards = load_flashcards()

    while True:
        print("\nMenu:")
        print("1. Create a flashcard")
        print("2. Review flashcards")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_flashcard(flashcards)
            save_flashcards(flashcards)
        elif choice == "2":
            review_flashcards(flashcards)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

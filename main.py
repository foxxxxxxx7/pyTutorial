import time
import random

# Sample sentences for the typing test
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Typing speed is a useful skill to develop.",
    "Always aim for accuracy before speed.",
    "Practice makes perfect when it comes to typing."
]

def get_random_sentence():
    """Return a random sentence from the list."""
    return random.choice(SENTENCES)

def typing_test():
    """Run the typing speed test."""
    sentence = get_random_sentence()
    print("\nTyping Speed Test!")
    print(f"Type the following sentence:\n\n{sentence}\n")
    input("Press Enter when you are ready to start...")

    start_time = time.time()
    typed_sentence = input("\nStart typing: ")
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time
    elapsed_minutes = elapsed_time / 60

    # Calculate words per minute
    words = len(sentence.split())
    wpm = words / elapsed_minutes

    # Calculate accuracy
    correct_chars = sum(1 for a, b in zip(typed_sentence, sentence) if a == b)
    accuracy = (correct_chars / len(sentence)) * 100

    # Display results
    print("\nResults:")
    print(f"Time Taken: {elapsed_time:.2f} seconds")
    print(f"Words Per Minute (WPM): {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")
    if typed_sentence != sentence:
        print("\nYour input had errors. Here's the original sentence:")
        print(sentence)

def main():
    """Main program loop."""
    while True:
        typing_test()
        retry = input("\nWould you like to try again? (yes/no): ").strip().lower()
        if retry != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()

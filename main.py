import json
import random

FILENAME = "library.json"

# Sample book recommendations database
RECOMMENDATIONS = {
    "Fiction": ["The Great Gatsby", "To Kill a Mockingbird", "1984"],
    "Non-Fiction": ["Sapiens", "Educated", "The Immortal Life of Henrietta Lacks"],
    "Fantasy": ["Harry Potter", "The Hobbit", "Mistborn"],
    "Science Fiction": ["Dune", "Neuromancer", "The Martian"],
    "Mystery": ["Gone Girl", "Sherlock Holmes", "The Girl with the Dragon Tattoo"]
}

def load_library():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library(library):
    with open(FILENAME, "w") as file:
        json.dump(library, file)

def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author's name: ").strip()
    genre = input("Enter the genre: ").strip().capitalize()

    library.append({"title": title, "author": author, "genre": genre})
    print(f"Book '{title}' by {author} added to your library.")

def view_library(library):
    if not library:
        print("Your library is empty. Start adding books!")
        return

    print("\nYour Library:")
    for book in library:
        print(f"- {book['title']} by {book['author']} (Genre: {book['genre']})")

def recommend_books(library):
    if not library:
        print("Your library is empty. Add some books to get recommendations!")
        return

    genres = [book["genre"] for book in library]
    favorite_genre = max(set(genres), key=genres.count)

    print(f"\nBased on your favorite genre '{favorite_genre}', we recommend:")
    for book in random.sample(RECOMMENDATIONS.get(favorite_genre, []), k=3):
        print(f"- {book}")

def main():
    print("Welcome to the Book Recommendation System!")
    library = load_library()

    while True:
        print("\nOptions:")
        print("1. Add a Book")
        print("2. View Library")
        print("3. Get Recommendations")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            view_library(library)
        elif choice == "3":
            recommend_books(library)
        elif choice == "4":
            save_library(library)
            print("Goodbye! Happy reading!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

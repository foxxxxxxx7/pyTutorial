from textblob import TextBlob
import matplotlib.pyplot as plt
from datetime import datetime
import json

# Function to analyze sentiment
def analyze_sentiment(entry):
    analysis = TextBlob(entry)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Function to save a journal entry
def save_entry(entry, mood):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("journal.json", "r+") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
        data.append({"timestamp": timestamp, "entry": entry, "mood": mood})
        file.seek(0)
        json.dump(data, file, indent=4)

# Function to view mood trends
def view_mood_trends():
    try:
        with open("journal.json", "r") as file:
            data = json.load(file)
        dates = [entry["timestamp"] for entry in data]
        moods = [entry["mood"] for entry in data]
        mood_map = {"Positive": 1, "Neutral": 0, "Negative": -1}
        mood_scores = [mood_map[mood] for mood in moods]

        plt.plot(dates, mood_scores, marker="o")
        plt.xticks(rotation=45)
        plt.title("Mood Trends Over Time")
        plt.ylabel("Mood (Positive: 1, Neutral: 0, Negative: -1)")
        plt.xlabel("Date")
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print("No journal entries found. Start journaling today!")

# Main function
def main():
    print("Welcome to the Daily Journal with Sentiment Analysis!")
    while True:
        print("\nMenu:")
        print("1. Write a new journal entry")
        print("2. View mood trends")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            entry = input("Write your journal entry:\n")
            mood = analyze_sentiment(entry)
            save_entry(entry, mood)
            print(f"Your mood has been analyzed as: {mood}. Entry saved!")

        elif choice == "2":
            view_mood_trends()

        elif choice == "3":
            print("Goodbye! Keep journaling!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

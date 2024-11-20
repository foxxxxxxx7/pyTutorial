import json
from datetime import datetime

FILENAME = "habits.json"

def load_habits():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_habits(habits):
    with open(FILENAME, "w") as file:
        json.dump(habits, file)

def add_habit(habits):
    habit = input("Enter the name of the habit you want to track: ").strip()
    if habit in habits:
        print("This habit is already being tracked.")
    else:
        habits[habit] = {"streak": 0, "last_completed": None}
        print(f"Habit '{habit}' added successfully!")

def log_habit(habits):
    habit = input("Enter the habit you completed today: ").strip()
    if habit not in habits:
        print("This habit is not being tracked. Add it first!")
        return

    today = datetime.now().date().isoformat()
    if habits[habit]["last_completed"] == today:
        print("You already logged this habit for today.")
        return

    if habits[habit]["last_completed"]:
        last_date = datetime.fromisoformat(habits[habit]["last_completed"]).date()
        if (datetime.now().date() - last_date).days == 1:
            habits[habit]["streak"] += 1
        else:
            habits[habit]["streak"] = 1
    else:
        habits[habit]["streak"] = 1

    habits[habit]["last_completed"] = today
    print(f"Habit '{habit}' logged for today. Current streak: {habits[habit]['streak']} days.")

def view_habits(habits):
    if not habits:
        print("No habits being tracked yet.")
        return

    print("\nTracked Habits:")
    for habit, details in habits.items():
        streak = details["streak"]
        last_completed = details["last_completed"] or "Never"
        print(f"- {habit}: Streak - {streak} days | Last Completed - {last_completed}")

def main():
    print("Welcome to the Habit Tracker!")
    habits = load_habits()

    while True:
        print("\nOptions:")
        print("1. Add a Habit")
        print("2. Log a Habit")
        print("3. View Habits")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            log_habit(habits)
        elif choice == "3":
            view_habits(habits)
        elif choice == "4":
            save_habits(habits)
            print("Goodbye! Keep building your habits!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

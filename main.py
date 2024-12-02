import json

# Predefined exercise library
EXERCISES = {
    "strength": ["Push-ups", "Squats", "Deadlifts", "Pull-ups"],
    "cardio": ["Jumping Jacks", "Burpees", "Running", "Cycling"],
    "flexibility": ["Yoga Poses", "Stretching", "Pilates", "Tai Chi"],
}


def generate_workout(goal, time, equipment):
    """Generate a workout plan based on user input."""
    plan = []
    exercises = EXERCISES.get(goal, [])
    for exercise in exercises:
        if equipment or exercise not in ["Pull-ups", "Deadlifts"]:  # Example filter
            plan.append(f"{exercise}: {time // len(exercises)} minutes")
    return plan


def save_workout(plan):
    """Save the workout plan to a file."""
    with open("workout_plan.json", "w") as file:
        json.dump(plan, file)
    print("Workout plan saved!")


def load_workout():
    """Load a saved workout plan."""
    try:
        with open("workout_plan.json", "r") as file:
            plan = json.load(file)
        print("Loaded workout plan:")
        for exercise in plan:
            print(f"- {exercise}")
    except FileNotFoundError:
        print("No saved workout plan found.")


def main():
    print("Welcome to the Personalized Workout Planner!")

    while True:
        print("\nMenu:")
        print("1. Create a new workout plan")
        print("2. View saved workout plan")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            goal = input("Enter your fitness goal (strength, cardio, flexibility): ").strip().lower()
            time = int(input("How many minutes do you have for a workout? ").strip())
            equipment = input("Do you have any equipment? (yes/no): ").strip().lower() == "yes"

            plan = generate_workout(goal, time, equipment)
            print("\nYour workout plan:")
            for exercise in plan:
                print(f"- {exercise}")

            save_choice = input("Do you want to save this plan? (yes/no): ").strip().lower()
            if save_choice == "yes":
                save_workout(plan)

        elif choice == "2":
            load_workout()

        elif choice == "3":
            print("Goodbye! Stay fit!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

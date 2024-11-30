import random
import json

RECIPES_FILE = "recipes.json"

def load_recipes():
    """Load recipes from a file."""
    try:
        with open(RECIPES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_recipes(recipes):
    """Save recipes to a file."""
    with open(RECIPES_FILE, "w") as file:
        json.dump(recipes, file)

def add_recipe(recipes):
    """Add a new recipe."""
    recipe_name = input("Enter the recipe name: ").strip()
    ingredients = input("Enter the ingredients (comma-separated): ").strip().split(",")
    recipes[recipe_name] = [ingredient.strip() for ingredient in ingredients]
    print(f"Recipe '{recipe_name}' added!")

def generate_meal_plan(recipes):
    """Generate a weekly meal plan."""
    if not recipes:
        print("No recipes available! Please add some recipes first.")
        return

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meal_plan = {day: random.choice(list(recipes.keys())) for day in days}

    print("\nWeekly Meal Plan:")
    for day, recipe in meal_plan.items():
        print(f"- {day}: {recipe}")

    return meal_plan

def create_shopping_list(meal_plan, recipes):
    """Create a shopping list based on the meal plan."""
    if not meal_plan:
        print("No meal plan available! Generate one first.")
        return

    shopping_list = {}
    for recipe in meal_plan.values():
        for ingredient in recipes[recipe]:
            shopping_list[ingredient] = shopping_list.get(ingredient, 0) + 1

    print("\nShopping List:")
    for ingredient, count in shopping_list.items():
        print(f"- {ingredient}: {count}")

def main():
    """Main function for the Random Meal Planner."""
    print("Welcome to the Random Meal Planner!")
    recipes = load_recipes()
    meal_plan = None

    while True:
        print("\nMenu:")
        print("1. Add a recipe")
        print("2. Generate weekly meal plan")
        print("3. Create shopping list")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_recipe(recipes)
            save_recipes(recipes)
        elif choice == "2":
            meal_plan = generate_meal_plan(recipes)
        elif choice == "3":
            create_shopping_list(meal_plan, recipes)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

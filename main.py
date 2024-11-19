import csv

def add_expense(expenses):
    category = input("Enter expense category (e.g., Food, Transport): ").strip().capitalize()
    try:
        amount = float(input("Enter amount spent: "))
        expenses.append({"category": category, "amount": amount})
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_summary(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    summary = {}
    for expense in expenses:
        summary[expense["category"]] = summary.get(expense["category"], 0) + expense["amount"]

    print("\nExpense Summary:")
    for category, total in summary.items():
        print(f"{category}: €{total:.2f}")
    print(f"Total Spending: €{sum(item['amount'] for item in expenses):.2f}")

def export_to_csv(expenses):
    if not expenses:
        print("No expenses to export.")
        return

    filename = "expenses.csv"
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["category", "amount"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)

    print(f"Expenses exported to {filename}")

def main():
    print("Welcome to the Expense Tracker!")
    expenses = []

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Export to CSV")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            export_to_csv(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

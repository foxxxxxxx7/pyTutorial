import time
import threading
import os

def countdown_timer(name, duration, alert_message):
    """Runs a countdown timer."""
    print(f"Timer '{name}' started for {duration} seconds.")
    while duration > 0:
        mins, secs = divmod(duration, 60)
        timer_display = f"{mins:02}:{secs:02}"
        print(f"{name}: {timer_display}", end="\r")
        time.sleep(1)
        duration -= 1
    print(f"\nTime's up for '{name}'! {alert_message}")

def set_timer():
    """Prompt the user to set up a timer."""
    name = input("Enter a name for your timer: ").strip()
    duration = int(input("Enter the duration in seconds: ").strip())
    alert_message = input("Enter a custom message for when the timer ends: ").strip()
    return name, duration, alert_message

def main():
    """Main function to manage multiple timers."""
    print("Welcome to the Custom Countdown Timer!")
    timers = []

    while True:
        print("\nMenu:")
        print("1. Set a new timer")
        print("2. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name, duration, alert_message = set_timer()
            timer_thread = threading.Thread(target=countdown_timer, args=(name, duration, alert_message))
            timer_thread.start()
            timers.append(timer_thread)
        elif choice == "2":
            print("Exiting... Waiting for all timers to finish.")
            for timer in timers:
                timer.join()
            print("All timers have completed. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

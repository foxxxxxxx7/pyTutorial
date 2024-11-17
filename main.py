import time


def pomodoro_timer(work_minutes, break_minutes, cycles):
    for cycle in range(1, cycles + 1):
        print(f"\nCycle {cycle}/{cycles}: Work for {work_minutes} minutes.")
        countdown(work_minutes * 60, "Time to take a break!")

        if cycle < cycles:
            print(f"Take a break for {break_minutes} minutes.")
            countdown(break_minutes * 60, "Back to work!")

    print("\nPomodoro session complete. Great job!")


def countdown(seconds, message):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print(message)


def main():
    print("Welcome to the Pomodoro Timer!")
    try:
        work_minutes = int(input("Enter work duration (in minutes): "))
        break_minutes = int(input("Enter break duration (in minutes): "))
        cycles = int(input("Enter number of cycles: "))

        pomodoro_timer(work_minutes, break_minutes, cycles)
    except ValueError:
        print("Please enter valid numbers for the durations and cycles.")


if __name__ == "__main__":
    main()

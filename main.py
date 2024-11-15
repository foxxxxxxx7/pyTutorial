import time


def stopwatch():
    print("Welcome to the Stopwatch!")
    print("Commands:")
    print("  start - Start the stopwatch")
    print("  stop  - Pause the stopwatch")
    print("  reset - Reset the stopwatch to 0")
    print("  quit  - Exit the stopwatch")

    start_time = 0
    elapsed_time = 0
    running = False

    while True:
        command = input("\nEnter a command: ").lower()

        if command == "start":
            if running:
                print("Stopwatch is already running.")
            else:
                start_time = time.time() - elapsed_time
                running = True
                print("Stopwatch started.")

        elif command == "stop":
            if not running:
                print("Stopwatch is not running.")
            else:
                elapsed_time = time.time() - start_time
                running = False
                print(f"Stopwatch paused at {elapsed_time:.2f} seconds.")

        elif command == "reset":
            start_time = 0
            elapsed_time = 0
            running = False
            print("Stopwatch reset to 0 seconds.")

        elif command == "quit":
            print("Exiting stopwatch. Goodbye!")
            break

        else:
            print("Invalid command. Please use start, stop, reset, or quit.")

        # Display elapsed time in real-time if running
        if running:
            elapsed_time = time.time() - start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds", end="\r")


if __name__ == "__main__":
    stopwatch()

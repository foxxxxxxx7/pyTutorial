import requests
import json

API_KEY = "your_openweathermap_api_key"

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    else:
        return {"error": "City not found or API issue."}

def save_log(city, weather, observation):
    with open("weather_journal.txt", "a") as file:
        file.write(f"City: {city}\n")
        file.write(f"Temperature: {weather['temperature']}°C\n")
        file.write(f"Weather: {weather['description']}\n")
        file.write(f"Observation: {observation}\n")
        file.write("-" * 40 + "\n")

def display_logs():
    try:
        with open("weather_journal.txt", "r") as file:
            print("\nYour Weather Journal:\n")
            print(file.read())
    except FileNotFoundError:
        print("\nNo logs found. Start journaling your weather observations!")

def main():
    print("Welcome to the Weather Journal!")
    while True:
        print("\nOptions:")
        print("1. Fetch Weather")
        print("2. Log Weather Observation")
        print("3. View Weather Journal")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            city = input("Enter a city: ").strip()
            weather = fetch_weather(city)
            if "error" in weather:
                print(weather["error"])
            else:
                print(f"City: {weather['city']}")
                print(f"Temperature: {weather['temperature']}°C")
                print(f"Weather: {weather['description']}")
        elif choice == "2":
            city = input("Enter a city: ").strip()
            weather = fetch_weather(city)
            if "error" in weather:
                print(weather["error"])
            else:
                observation = input("Write your weather observation: ").strip()
                save_log(city, weather, observation)
                print("Observation saved!")
        elif choice == "3":
            display_logs()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

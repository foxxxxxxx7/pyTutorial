import requests

# Function to get weather data for a city
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Extract weather information
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Display the information
        print(f"\nWeather in {city.capitalize()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather_description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    except requests.exceptions.HTTPError:
        print("City not found. Please check the city name and try again.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    api_key = "your_openweathermap_api_key"  # Replace with your actual API key
    print("Welcome to the Weather App!")
    city = input("Enter the name of a city to get the current weather: ").strip()
    get_weather(city, api_key)

if __name__ == "__main__":
    main()

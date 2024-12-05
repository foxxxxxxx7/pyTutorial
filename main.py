import os
import platform
import time
import random
import requests
from datetime import datetime

# Function to set wallpaper (platform-specific)
def set_wallpaper(image_path):
    system = platform.system()
    if system == "Windows":
        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
    elif system == "Darwin":  # macOS
        os.system(f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"{image_path}\"'")
    elif system == "Linux":
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}")

# Function to fetch weather information
def get_weather():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    location = "Dublin,IE"  # Replace with your city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data["weather"][0]["main"].lower()  # e.g., sunny, rainy, snowy
    else:
        print("Error fetching weather data.")
        return "default"

# Function to get wallpapers by time or weather
def get_wallpaper_by_theme(theme):
    wallpaper_directory = "wallpapers"  # Replace with the path to your wallpaper folder
    theme_folder = os.path.join(wallpaper_directory, theme)
    if os.path.exists(theme_folder):
        return random.choice([os.path.join(theme_folder, f) for f in os.listdir(theme_folder) if f.endswith(('.jpg', '.png'))])
    else:
        print(f"No wallpapers found for theme: {theme}")
        return None

# Main function
def main():
    print("Dynamic Wallpaper Rotator started!")
    while True:
        # Determine theme based on time and weather
        now = datetime.now()
        if now.hour < 12:
            time_theme = "morning"
        elif 12 <= now.hour < 18:
            time_theme = "afternoon"
        else:
            time_theme = "night"

        weather_theme = get_weather()
        print(f"Time Theme: {time_theme}, Weather Theme: {weather_theme}")

        # Get wallpaper
        wallpaper = get_wallpaper_by_theme(weather_theme) or get_wallpaper_by_theme(time_theme)
        if wallpaper:
            set_wallpaper(wallpaper)
            print(f"Wallpaper set to: {wallpaper}")
        else:
            print("No suitable wallpaper found.")

        time.sleep(3600)  # Change wallpaper every hour

if __name__ == "__main__":
    main()

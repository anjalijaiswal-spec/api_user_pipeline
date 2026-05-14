import requests
import json
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()
# Get API key safely
API_KEY = os.getenv("API_KEY")
print(API_KEY)
CITY = "Delhi"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print("✓ Weather API request successful")
            return response.json()
        else:
            print(f"✗ API Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as error:
        print(f"✗ Request Failed: {error}")
        return None


def display_weather(data):

    if not data:
        return

    city = data["name"]
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print("\n====== WEATHER REPORT ======")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {weather}")
    print(f"Humidity: {humidity}%")
    print("============================")


def save_weather(data):

    try:

        with open("weather_data.json", "w") as file:
            json.dump(data, file, indent=2)

        print("✓ Saved weather_data.json")

    except Exception as error:
        print(f"✗ Failed saving file: {error}")


def main():

    print("Starting Weather Pipeline...\n")

    weather_data = fetch_weather()

    if weather_data:

        display_weather(weather_data)

        save_weather(weather_data)

        print("\nPipeline Complete!")


main()
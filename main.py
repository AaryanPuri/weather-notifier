import requests
from plyer import notification
import schedule
import time

def get_weather(city_name, api_key):
    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}"

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        temp = data['current']['temp_c']
        condition = data['current']['condition']['text']

        print(f"Temperature in {city_name}: {temp}°C")
        print(f"Condition: {condition}")

        
        if "rain" in condition.lower():
            mood = "🌧️ Don't forget your umbrella!"
        elif "sunny" in condition.lower():
            mood = "☀️ Bright and sunny!"
        else:
            mood = "🌤️ Looks like a normal day."

        message = f"{condition}\nTemperature: {temp}°C\n{mood}"

        notification.notify(
            title=f"Weather Update for {city_name}",
            message=message,
            timeout=10
        )
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")

def job():
    city = input("Enter the city name: ")
    api_key = "405b618c06c643e788784042252606"
    get_weather(city, api_key)

if __name__ == "__main__":
    print("Weather Notifier running... (Press Ctrl+C to stop)")
    schedule.every().day.at("08:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)



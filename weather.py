import requests

def get_weather(city):
    api_key = "cd95bfc489f09469cb862762755b86bd"  # Your API key inserted here
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses
        data = response.json()

        if data["cod"] == 200:
            city_name = data["name"]
            temperature = data["main"]["temp"]
            weather_description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            
            # Display the weather information
            print(f"Weather in {city_name}:")
            print(f"Temperature: {temperature}°C")
            print(f"Weather: {weather_description}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("City not found!")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
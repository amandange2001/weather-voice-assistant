import requests
import win32com.client 

def fetch_weather(api_key, city):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch weather data. {e}")
        return None

def speak_weather_data(city, weather, temperature):
    user_input = f"The current weather report in {city} is {weather} weather and temperature is {temperature} degrees Celsius."
    try:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(user_input)
        print("Spoken:", user_input)
    except Exception as e:
        print(f"Error during speech synthesis: {e}")

def main():
    api_key = "9007cf4ca14b408e9b1142448230712"  

    city = input("Enter the name of the city: ").strip()
    if not city:
        print("Error: Please enter a valid city name.")
        return

    while True:
        weather_data = fetch_weather(api_key, city)
        if weather_data is None:
            return

        temperature_celsius = weather_data["current"]["temp_c"]
        climate = weather_data["current"]["condition"]["text"]
        print(f"{climate} weather at {city} with {temperature_celsius}°C")
        
        speak_weather_data(city, climate, temperature_celsius)

        user_input1 = input("Type 'exit' to quit: ")
        if user_input1.lower() == 'exit':
            break

if __name__ == "__main__":
    main()

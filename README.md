# weather-voice-assistant
The repository contains a Python script that fetches current weather data from the WeatherAPI and uses text-to-speech synthesis to verbally report the weather conditions for a specified city. The script utilizes the requests library for API communication and the win32com library for speech synthesis.


Weather Report Application
Developed a Python application that fetches real-time weather data using the WeatherAPI, providing a spoken weather report using the Windows SAPI text-to-speech engine.

Technologies Used:
Python
Requests library for API interaction
Win32com library for text-to-speech synthesis

Key Features:
Fetches weather data from the WeatherAPI based on user-input city names.
Utilizes exception handling for robust error management during API requests.
Integrates the Windows SAPI library to provide a spoken weather report, including current weather conditions and temperature.

Implementation:
User inputs a city name to get the latest weather report.
Displays current weather conditions and temperature in Celsius.
Provides an option for the user to exit the application.
Utilizes a try-except block for handling errors during API requests and speech synthesis.

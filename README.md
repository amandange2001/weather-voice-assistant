
# Weather Voice Assistant

## Overview

This Python script serves as a Weather Voice Assistant, fetching real-time weather data from the WeatherAPI and providing a spoken weather report using the Windows SAPI text-to-speech engine. The application is designed to be user-friendly, allowing users to input a city name and receive a verbal report on the current weather conditions and temperature.


## Technologies Used

- Python: The core programming language for developing the application.
- Requests library: Utilized for making API requests to the - - - WeatherAPI and fetching real-time weather data.
- Win32com library: Integrated for text-to-speech synthesis using the Windows SAPI engine.

## Key Features

1. Weather Data Fetching: The application fetches weather data from the WeatherAPI based on user-input city names.

2. Exception Handling: Robust error management is implemented using try-except blocks to handle errors that may occur during API requests and speech synthesis.

3. Text-to-Speech Synthesis: Utilizes the Windows SAPI library to provide a spoken weather report, including current weather conditions and temperature.


## Implementation


1. User Input: Users input a city name to get the latest weather report.

2. Weather Report Display: The application displays current weather conditions and temperature in Celsius.

3. User Interaction: Provides an option for the user to exit the application gracefully.
## Deployment

Clone the repository to your local machine.


1. Clone the repository:
```bash
  git clone https://github.com/your-username/weather-voice-assistant.git
```

2. Install the required dependencies.
```bash
pip install win32com.client
```

3. Run the script
```bash
python weather_voice_assistant.py
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

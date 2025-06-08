# Weather App

A simple command-line weather application that provides current weather information for any location.

## Features

- Search weather by city name
- Displays temperature, humidity, wind speed, and weather conditions
- Fast and easy-to-use CLI interface

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/weather_app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd weather_app
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application from the command line:
    ```bash
    python main.py --city "City Name"
    ```
    Replace `"City Name"` with the desired location.

## Configuration

- Set your weather API key in the `.env` file:
  ```
  WEATHER_API_KEY=your_api_key_here
  ```

## Technologies Used

- Python
- Requests (or httpx)
- Weather API (e.g., OpenWeatherMap)

## License

This project is licensed under the MIT License.

## Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/)
- [Python](https://python.org/)

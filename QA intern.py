import requests

# London weather data from the API
def get_weather_data(date):
    api_url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(api_url)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Failed to fetch weather data.")
        return None
#temperature
def print_temperature(weather_data, date):
    for forecast in weather_data['list']:
        if forecast['dt_txt'].startswith(date):
            temp = forecast['main']['temp']
            print(f"Temperature on {date}: {temp:.2f}°C")
            return
    print(f"Could not find temperature data for {date}.")
#wind speed
def print_wind_speed(weather_data, date):
    for forecast in weather_data['list']:
        if forecast['dt_txt'].startswith(date):
            wind_speed = forecast['wind']['speed']
            print(f"Wind Speed on {date}: {wind_speed} m/s")
            return
    print(f"Could not find wind speed data for {date}.")
#pressure
def print_pressure(weather_data, date):
    for forecast in weather_data['list']:
        if forecast['dt_txt'].startswith(date):
            pressure = forecast['main']['pressure']
            print(f"Pressure on {date}: {pressure} hPa")
            return
    print(f"Could not find pressure data for {date}.")
# Main program loop
def main():
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice (0-3): ")

        if choice == '1':
            date_input = input("Enter the date (YYYY-MM-DD): ")
            weather_data = get_weather_data(date_input)
            if weather_data:
                print_temperature(weather_data, date_input)
        elif choice == '2':
            date_input = input("Enter the date (YYYY-MM-DD): ")
            weather_data = get_weather_data(date_input)
            if weather_data:
                print_wind_speed(weather_data, date_input)
        elif choice == '3':
            date_input = input("Enter the date (YYYY-MM-DD): ")
            weather_data = get_weather_data(date_input)
            if weather_data:
                print_pressure(weather_data, date_input)
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

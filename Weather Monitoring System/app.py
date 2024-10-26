import time
from weather import process_weather_data
from rollups import calculate_daily_aggregate
from alerts import check_threshold_violation
from visualizations import plot_weather_trend

CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
COLLECT_INTERVAL = 300  # Time interval to fetch weather data (in seconds)
THRESHOLD_TEMP = 35.0

all_weather_data = {city: [] for city in CITIES}

def print_weather_data(weather_data):
    # Print the header for weather data
    print("+--------------------------------------------------+")
    print("|                 Fetched Weather Data             |")
    print("+-----------+------------+------------+------------+")
    print("|   City    |   Temp (°C) | Feels Like | Condition |")
    print("+-----------+------------+------------+------------+")

    # Print each city's weather data
    for city, data in weather_data.items():
        if data:
            latest_weather = data[-1]  # Get the latest weather data
            print(f"| {city:<9} | {latest_weather['temp']:<10.2f} | {latest_weather['feels_like']:<10.2f} | {latest_weather['condition']:<10} |")
            print("+------------+------------+------------+------------+")

def print_daily_summary():
    # Print the header for daily summaries
    print("+---------------------------------------------------------------------------------+")
    print("|                              Daily Weather Summary                              |")
    print("+-----------+----------------+----------------+----------------+--------------------+")
    print("|   City    | Avg Temp (°C) | Max Temp (°C) | Min Temp (°C)   | Dominant Condition  |")
    print("+-----------+----------------+----------------+----------------+--------------------+")

    # Print each city's daily summary
    for city, data in all_weather_data.items():
        if data:
            daily_summary = calculate_daily_aggregate(data)
            print(f"| {city:<9} | {daily_summary['average_temp']:<14.2f} | {daily_summary['max_temp']:<14.2f} | {daily_summary['min_temp']:<14.2f} | {daily_summary['dominant_condition']:<18} |")
            print("+-----------+----------------+----------------+----------------+--------------------+")

def main():
    while True:
        for city in CITIES:
            weather_info = process_weather_data(city)
            if weather_info:
                all_weather_data[city].append(weather_info)

        # Print formatted weather data
        print_weather_data(all_weather_data)
        print()
        print()

        # Print daily summaries in a box
        print_daily_summary()
        print()

        # Check for alerts
        for city, data in all_weather_data.items():
            if data:
                alerts = check_threshold_violation(data, THRESHOLD_TEMP)
                for alert in alerts:
                    print(alert)

        # Plot weather trends
        for city, data in all_weather_data.items():
            if data:
                plot_weather_trend(data, city)

        # Sleep for the specified interval before fetching new data
        time.sleep(COLLECT_INTERVAL)

if __name__ == '__main__':
    main()

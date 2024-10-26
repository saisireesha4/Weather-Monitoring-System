import matplotlib.pyplot as plt
from datetime import datetime


def plot_weather_trend(weather_data, city):
    """Plot temperature trends for a specific city."""
    timestamps = [datetime.utcfromtimestamp(data['timestamp']) for data in weather_data]
    temps = [data['temp'] for data in weather_data]

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temps, marker='o', linestyle='-', color='b')
    plt.title(f"Temperature Trend for {city}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.show()

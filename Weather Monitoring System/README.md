# Weather Monitoring System

## Overview
The Weather Monitoring System is a Python-based application that fetches real-time weather data for multiple cities, performs daily summaries, checks for temperature alerts, and visualizes weather trends. The system utilizes the OpenWeatherMap API for data retrieval.

## Features
- Fetches current weather data for specified cities at regular intervals.
- Calculates daily weather summaries, including average, maximum, and minimum temperatures.
- Checks for temperature threshold violations and alerts the user.
- Visualizes weather trends using plots.

# Design Choices

- **Modular Structure**: The application is divided into multiple modules:
  - weather.py : Responsible for fetching and processing weather data from the OpenWeatherMap API.
  - rollups.py : Contains functions to calculate daily weather aggregates.
  - alerts.py : Handles the monitoring of alert thresholds and notifying users of any violations.
  - visualizations.py : Provides functions for visualizing weather trends over time.
  
- **Real-time Processing**: The application continuously retrieves and processes data to provide up-to-date weather insights.

- **User Configurable Settings**: Users can set their preferred temperature thresholds for alerts.

## Installation

### Prerequisites
- Python 3.x
- requests
- matplotlib (for visualizations)
- OpenWeatherMap API Key (sign up at [OpenWeatherMap](https://openweathermap.org/) to get your API key)

## Usage
- The application will fetch weather data every 5 minutes (300 seconds).
- The fetched data and daily summaries will be printed in a formatted table in the console.
- Alerts for temperature threshold violations will be displayed if applicable.
- Visualizations of weather trends will be generated.

## Conclusion
The Weather Monitoring System serves as an effective tool for tracking real-time weather data across multiple cities. By providing summarized insights, alerts, and visualizations, this application enables users to stay informed about weather conditions and potential temperature-related issues. It can be further enhanced with additional features, such as user-specific alerts or historical weather analysis, making it a versatile solution for personal or organizational use.

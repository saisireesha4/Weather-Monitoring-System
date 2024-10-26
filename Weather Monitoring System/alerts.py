def check_threshold_violation(weather_data, threshold_temp=35.0):
    """Check if the temperature exceeds a given threshold."""
    violations = []
    for data in weather_data:
        if data['temp'] > threshold_temp:
            violations.append(f"Alert: {data['city']} exceeded {threshold_temp}°C at {data['timestamp']}")
    return violations

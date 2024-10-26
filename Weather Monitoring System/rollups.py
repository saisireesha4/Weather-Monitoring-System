import datetime


def calculate_daily_aggregate(weather_data):
    """Calculate daily aggregates: average, min, max temperature and dominant weather."""
    temp_list = [data['temp'] for data in weather_data]
    avg_temp = sum(temp_list) / len(temp_list)
    max_temp = max(temp_list)
    min_temp = min(temp_list)

    # Find dominant weather condition (most frequent)
    conditions = [data['condition'] for data in weather_data]
    dominant_condition = max(set(conditions), key=conditions.count)

    return {
        'date': datetime.date.today(),
        'average_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_condition': dominant_condition
    }

import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    return date.strftime('%A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    temp_in_c = round((float(temp_in_farenheit) - 32) / 1.8, 1)
    return temp_in_c
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """


def calculate_mean(weather_data):
    sum = 0
    for x in weather_data:
        sum += float(x)
    mean = sum / len(weather_data)
    return mean
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    weather_data = []
    with open(csv_file, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        for line in reader:
            if not line:
                continue
            line[1] = int(line[1])
            line[2] = int(line[2])
            weather_data.append(line)
    return weather_data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if not weather_data:
        return ()
    else:
        min_value = float(9999999)
        min_index = None
        index = 0

        for this_element in weather_data:
            this_element = float(this_element)
            if this_element <= min_value:
                min_value = this_element
                min_index = index

            index += 1

        return (float(min_value), min_index)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if not weather_data:
        return ()
    else:
        max_value = 0
        max_index = 0
        index = 0

        for this_element in weather_data:
            this_element = float(this_element)
            if this_element >= max_value:
                max_value = this_element
                max_index = index

            index += 1
        return (max_value, max_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    quantity_of_days = len(weather_data)
    list_of_dates = []
    list_of_min_temp = []
    list_of_max_temp = []
    for item in weather_data:
        list_of_dates.append(convert_date(item[0]))
        list_of_min_temp.append(item[1])
        list_of_max_temp.append(item[2])

    lowest_temperature = find_min(list_of_min_temp)
    highest_temperature = find_max(list_of_max_temp)
    average_low = calculate_mean(list_of_min_temp)
    average_high = calculate_mean(list_of_max_temp)

    return (f"{quantity_of_days} Day Overview\n  The lowest temperature will be {format_temperature(convert_f_to_c(lowest_temperature[0]))}, and will occur on {list_of_dates[lowest_temperature[1]]}.\n  The highest temperature will be {format_temperature(convert_f_to_c(highest_temperature[0]))}, and will occur on {list_of_dates[highest_temperature[1]]}.\n  The average low this week is {format_temperature(convert_f_to_c(average_low))}.\n  The average high this week is {format_temperature(convert_f_to_c(average_high))}.\n")


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    result = ""
    for item in weather_data:
        result += f"---- {convert_date(item[0])} ----\n  Minimum Temperature: {format_temperature(convert_f_to_c(item[1]))}\n  Maximum Temperature: {format_temperature(convert_f_to_c(item[2]))}\n\n"
    return result

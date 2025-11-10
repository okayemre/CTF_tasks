import math_utils
import stats_utils

REPORT_TITLE = "Daily Climate Data Analysis"
DEFAULT_TEMPERATURE_UNIT = "C"


def generate_report():
    print(f"*********{REPORT_TITLE}*********")

    temp_list = [22.5, 23.1, 21.9, 24.0, 22.8]

    list_average = stats_utils.calculate_average(temp_list)
    list_stdeviation = stats_utils.calculate_standard_deviation(temp_list)

    value_F = math_utils.convert_temperature(list_average, "C", "F")

    round_temp_value = round(value_F, math_utils.DEFAULT_PRECISION)

    print(f" - Temperature List Average: {list_average}")
    print(f" - Temperature List Standard Deviation: {list_stdeviation}")
    print(f" - Fahrenheit Temp: {round_temp_value}")


generate_report()

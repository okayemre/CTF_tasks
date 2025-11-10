# Task 1: Creating a Library for Numerical Analysis Functions

# 1.1 Mathematical Helper Functions

# 1. calculate_average(numbers_list): Takes a list of numbers and returns their arithmetic mean.


def calculate_average(numbers_list: list[float]) -> float:
    """
    Calculate the arithmetic mean (average) of a list of numbers.

    Args:
        numbers_list (list[float]): A list of numerical values.

    Returns:
        float: The calculated average value.

    Raises:
        ValueError: If the list is empty.
    """

    if len(numbers_list) == 0:
        return 0
        # return None
        # raise ValueError("List is empty")

    sum = 0
    # for i in range(0, len(numbers_list)):
    for i in numbers_list:
        # sum = sum + numbers_list[i]
        sum += i
    return sum / len(numbers_list)


def calculate_average_2(numbers_list):
    return sum(numbers_list) / len(numbers_list)


number_array = [1, 2, 3, 4, 5, 6]

number_array_2 = [2, 4, 4, 4, 5, 5, 7, 9]

number_array_3 = [10, 12, 23, 23, 16, 23, 21, 16]


print(calculate_average(number_array))

print(calculate_average_2(number_array))


# 2. calculate_standard_deviation(numbers_list): Takes a list of numbers and returns their standard deviation (you can focus on the sample standard deviation). If necessary, use your calculate_average function internally.

# σ = sqrt( (1/n) * Σ(xᵢ - μ)² )

import math


def calculate_standard_deviation(numbers_list: list[float]) -> float:
    """
    Calculate the sample standard deviation of a list of numbers.

    Formula:
        σ = sqrt( Σ(xᵢ - μ)² / (n - 1) )

    Args:
        numbers_list (list[float]): A list of numerical values.

    Returns:
        float: The sample standard deviation.

    Raises:
        ValueError: If the list has fewer than 2 elements.
    """

    # Σ(xᵢ - μ)²
    sum_sqrt = 0
    for i in numbers_list:
        # sum_sqrt += (i - calculate_average(numbers_list)) * (i - calculate_average(numbers_list))
        sum_sqrt += (i - calculate_average(numbers_list)) ** 2

    return math.sqrt(sum_sqrt / len(numbers_list))


print(f"\n {calculate_standard_deviation(number_array)}")
print(f"\n {calculate_standard_deviation(number_array_2)}")
print(f"\n {calculate_standard_deviation(number_array_3)}")


# 3. convert_temperature(value, unit_from, unit_to): This function should be able to convert temperature values between Celsius ('C'), Fahrenheit ('F'), and Kelvin ('K'). It takes the value, the source unit, and the target unit as strings. For invalid units or conversions, it should raise a ValueError or return None.


def convert_temperature(value: float, unit_from: str, unit_to: str) -> float:
    """
    Convert a temperature value between Celsius (C), Fahrenheit (F), and Kelvin (K).

    Args:
        value (float): The input temperature value.
        unit_from (str): The source unit ('C', 'F', or 'K').
        unit_to (str): The target unit ('C', 'F', or 'K').

    Returns:
        float: The converted temperature value.

    Raises:
        ValueError: If an invalid temperature unit is provided.
    """

    if unit_from == "C" and unit_to == "F":
        value_F = value * (9 / 5) + 32
        return value_F
    elif unit_from == "F" and unit_to == "C":
        value_C = (value - 32) * (5 / 9)
        return value_C
    elif unit_from == "C" and unit_to == "K":
        value_K = value + 273.15
        return value_K
    elif unit_from == "K" and unit_to == "C":
        value_C = value - 273.15
        return value_C
    elif unit_from == "F" and unit_to == "K":
        value_C = (value - 32) * (5 / 9)
        value_K = value_C + 273.15
        return value_K
    elif unit_from == "K" and unit_to == "F":
        value_C = value - 273.15
        value_F = value_C * (9 / 5) + 32
        return value_F
    else:
        # print("Value Error")
        raise ValueError("Value Error")


print(convert_temperature(15, "C", "F"))  # 59.0
print(convert_temperature(15, "C", "K"))  # 288.15
print(convert_temperature(59, "F", "C"))  # 15.0
print(convert_temperature(59, "F", "K"))  # 288.15
print(convert_temperature(288.15, "K", "C"))  # 15.0
print(convert_temperature(288.15, "K", "F"))  # 59.0


# 1.2 Additional Requirements
# Error Handling: Ensure your functions are robust. For example, calculate_average should detect an empty list and react appropriately (e.g., return 0 or None, or raise a ValueError).

""" !!! The above function has been updated appropriately."""

# Docstrings and Type Hints: Add a meaningful docstring to each function, describing what the function does, what parameters it expects, and what it returns. Also, use type hints for parameters and return values.

""" !!! The above function has been updated appropriately."""


# ****************************************************************************************
# Task 2: Modularization and Scope Management for a Report Generator
# 2.1 Modular Division of Functions

# math_utils.py: Create a new Python file named math_utils.py. Move the convert_temperature function into this file.

""" DONE """

# stats_utils.py: Create another Python file named stats_utils.py. Move the calculate_average and calculate_standard_deviation functions into this file.

""" DONE """

# Module-wide Constants:
# Add a module-global constant DEFAULT_PRECISION = 2 (number of decimal places) to math_utils.py.
""" DONE """

# Add a module-global constant MIN_DATAPOINTS = 2 to stats_utils.py, indicating how many data points are minimally necessary for statistical calculations (e.g., for standard deviation). Adjust the functions accordingly so that they use this constant, e.g., to raise an error if not enough data points are present.
""" DONE """

# Create a third Python file named report_generator.py. This will be your main program, which uses the functions from the two modules to generate a small report.
""" DONE """

# Import Modules: Import the math_utils and stats_utils modules into report_generator.py.
""" DONE """

# Global Configuration: In report_generator.py, define a global variable REPORT_TITLE = "Daily Climate Data Analysis" and another global variable DEFAULT_TEMPERATURE_UNIT = "C".
""" DONE """

# Main Function generate_report():
# Define a function generate_report() in report_generator.py.
# Inside this function:
# Use REPORT_TITLE for the report's heading.
""" DONE """

# Define a local list of temperature data (e.g., [22.5, 23.1, 21.9, 24.0, 22.8]).
""" DONE """

# Calculate the average and standard deviation of the temperatures using the functions from stats_utils. Pay attention to how you address the modules (e.g., stats_utils.calculate_average(...)).
""" DONE """

# Convert the calculated average to Fahrenheit, using the convert_temperature function from math_utils. Ensure the result is rounded to math_utils.DEFAULT_PRECISION (use an internal function or formatting for this).
# Output all results neatly to the console, including the title and the converted temperature.
""" DONE """

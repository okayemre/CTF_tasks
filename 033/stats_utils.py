MIN_DATAPOINTS = 2


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

    if len(numbers_list) < MIN_DATAPOINTS:
        raise ValueError("Not enough data points")

    sum = 0
    # for i in range(0, len(numbers_list)):
    for i in numbers_list:
        # sum = sum + numbers_list[i]
        sum += i
    return sum / len(numbers_list)


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

    if len(numbers_list) < MIN_DATAPOINTS:
        raise ValueError("Not enough data points")

    # Σ(xᵢ - μ)²
    sum_sqrt = 0
    for i in numbers_list:
        # sum_sqrt += (i - calculate_average(numbers_list)) * (i - calculate_average(numbers_list))
        sum_sqrt += (i - calculate_average(numbers_list)) ** 2

    return math.sqrt(sum_sqrt / len(numbers_list))

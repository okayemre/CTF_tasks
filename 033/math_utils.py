DEFAULT_PRECISION = 2


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

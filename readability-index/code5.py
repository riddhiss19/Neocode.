def calculate_sum(numbers):
    """
    Calculates the sum of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The sum of the numbers.
    """
    total = 0
    for number in numbers:
        total += number
    return total


def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers.
    """
    total = calculate_sum(numbers)
    average = total / len(numbers)
    return average

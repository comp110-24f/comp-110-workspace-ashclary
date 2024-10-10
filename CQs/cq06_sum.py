"""Summing the elements of a list using different loops"""

__author__ = "730754494"


def w_sum(
    vals: list[float],
) -> float:  # this function takes in a list and outputs a float
    """Function for summing floats in a list using a while loop."""
    number: float = 0.0
    idx: int = 0
    while idx < len(vals):  # this while loops allows for iteration through the string
        number = number + vals[idx]  # I am adding each float in vals to number
        idx += 1
    return number  # the returned float is the sum


def f_sum(vals: list[float]) -> float:  # this function is leading to the same output
    """Function for summing floats in a list using a for...in...loop."""
    number: float = 0.0  # I am setting the initial sum value to 0.0
    for element in vals:  # the for loops allows for each element to be considered
        number = number + element
    return number  # I am still returning the float that is the sum


def f_range_sum(vals: list[float]) -> float:
    """Function for summing floats in a list using a for...in range(...) loop."""
    number: float = 0.0
    idx: int = 0  # I am again using idx to go through each element
    for idx in range(
        0, len(vals)
    ):  # this range allows for the correct length to add each element
        number = number + vals[idx]
        idx += 1  # this will make progress toward being out of the range
    return number

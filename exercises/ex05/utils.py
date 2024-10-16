"""Working with various list utility functions."""

__author__ = "730754494"


def only_evens(integer_list: list[int]) -> list[int]:
    """Function to return a list with the even integers only."""
    even_integers: list[int] = []  # I am establishing the local variable of a new list
    for idx in range(
        0, len(integer_list)
    ):  # using a for...in range loop to go through each integer in the input list
        if integer_list[idx] % 2 == 0:  # showing an even number
            even_integers.append(
                integer_list[idx]
            )  # only mutating the second list not the input
    return even_integers


def sub(integer_list: list[int], index_start: int, index_end: int) -> list[int]:
    """Function to return a subset of a list input."""
    subset_list: list[int] = []  # establishing the local variable of the subset list
    if index_start < 0:  # I am starting from the beginning if given a negative index
        index_start = 0
    if index_end > len(
        integer_list
    ):  # this expression makes sure the index does not go past the list's length
        index_end = len(integer_list)
    if (
        len(integer_list) == 0
    ):  # the subset list will also be empty if the input list is empty
        return subset_list
    if index_start >= len(
        integer_list
    ):  # an empty list will return is there is too large of a start index
        return subset_list
    if (
        index_end < 0
    ):  # too small of an end index will also lead to an empty list returning
        return subset_list
    for idx in range(
        index_start, (index_end)
    ):  # if all requirements are passed, subset_list will append to make the subset
        subset_list.append(
            integer_list[idx]
        )  # appending each integer in the established range to make the subset
    return subset_list


def add_at_index(integer_list: list[int], element: int, index: int) -> None:
    """Function to put the element at the index in the list."""
    if index < 0 or index > (
        len(integer_list) + 1
    ):  # an out-of-range index will lead to an error message
        raise IndexError("Index is out of bounds for the input list")
    else:
        integer_list.append(0)  # appending an element to create more room
        for idx in range(
            index + 1, len(integer_list)
        ):  # going through the integers to the right of the index
            integer_list[idx] = integer_list[
                idx - 1
            ]  # shifting the integers to the right to allow more room
        integer_list[index] = element  # putting the element at the index

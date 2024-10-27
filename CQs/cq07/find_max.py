"""Folder for the function to remove the largest integer in a list."""

__author__ = "730754494"


def find_and_remove_max(number_list: list[int]) -> int:
    """Function to return the largest number and remove it from the list."""
    if number_list == []:  # specific case of an empty list
        return -1  # will return -1 as instructed
    largest_number: int = number_list[
        0
    ]  # setting the initial largest number as the first integer
    idx: int = 0
    while idx < len(number_list):  # using a while loop to iterate through the list
        if (
            number_list[idx] > largest_number
        ):  # meaning that the observed number becomes the max number for now
            largest_number = number_list[
                idx
            ]  # reassigning the value to the new largest number
        idx += 1
    idx_2: int = 0  # a new index for the next loop about mutating the list
    while idx_2 < len(number_list):
        if number_list[idx_2] == largest_number:  # only removing the max number
            number_list.pop(idx_2)  # the pop method takes the integer out of the list
        else:
            idx_2 += (
                1  # add else because only need to add 1 to idx if no int is removed
            )
    return largest_number  # will return the max number when the list is not empty

"""Testing function utilities to learn about their behaviors."""

__author__ = "730754494"


def all(integer_list: list[int], number: int) -> bool:
    """A function to check whether or not all the sting's integers equal number"""
    index: int = 0
    if integer_list == []:  # I am adding this line for an empty string specifically
        return False
    while index < len(
        integer_list
    ):  # I am using a while loop to go through each integer
        if integer_list[index] != number:
            return False  # returning here will exit the definition
        index += 1
    return True  # getting to this line will show that all integers equal the number


def max(integer_list: list[int]) -> int:
    """A function to find the largest of integers in a list."""
    if len(integer_list) == 0:  # an error will be raised for an empty list
        raise ValueError("max() arg is an empty list")
    largest_number: int = (
        0  # establishing this local variable will allow for it to be returned
    )
    for number in integer_list:  # using a for...in... loop to go through each integer
        if number > largest_number:
            largest_number = (
                number  # I will reassign largest number each time the integer is larger
            )
    return largest_number  # returning the largest number will show the biggest integer


def is_equal(integer_list1: list[int], integer_list2: list[int]) -> bool:
    """A function to see whether or not each element is equal in both lists."""
    if len(integer_list1) != len(
        integer_list2
    ):  # establishes that each element cannot be equal if the lengths are different
        return False
    for idx in range(
        0, len(integer_list1)
    ):  # using a for...in range loop allows for testing each index to compare
        if integer_list1[idx] != integer_list2[idx]:
            return (
                False  # if one index has different characters, immediately return False
            )
    return True


def extend(integer_list1: list[int], integer_list2: list[int]) -> None:
    """A function to append integers for a second list to the first list."""
    for (
        number
    ) in integer_list2:  # using a for...in... loop to append each integer from list 2
        integer_list1.append(number)  # the append method correlates to list

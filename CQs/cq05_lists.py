"""Mutating functions."""

__author__ = "730754494"


def manual_append(list: list[int], integer: int) -> None:
    """Function to append the integer to the list."""
    list.append(integer)  # mutating the list by appending the integer argument


def double(list: list[int]) -> None:
    """Function to double each element in the list."""
    index: int = 0  # setting up for the while loop
    while index < len(list):
        list[index] = list[index] * 2  # mutating each element by multiplying by 2
        index += 1  # making the loop not infinite


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1  # this connects the list_2 to the id of list_1 in the heap
double(list=list_2)  # I am assigning list_2 as the argument for double
print(list_1)
print(list_2)  # these will now print the same output because of connected id

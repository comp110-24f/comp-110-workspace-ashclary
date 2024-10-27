"""Folder for unit tests about find_and_remove_max's behavior."""

__author__ = "730754494"

from CQs.cq07.find_max import find_and_remove_max


def test_return_find_and_remove_max() -> None:
    """Unit test function to confirm the largest number return."""
    assert (
        find_and_remove_max([2, 7, 13]) == 13
    )  # 13 will return as the largest of the list


def test_mutation_find_and_remove_max() -> None:
    """Unit test function to confirm that the input function will be mutated."""
    number_list: list[int] = [2, 1, 2]  # local variable to test the input
    find_and_remove_max(
        number_list
    )  # I am putting the list as an input into the function to test
    assert number_list == [
        1
    ]  # confirming the removal of the largest integer as a mutation


def test_edge_find_and_remove_max() -> None:
    """Unit test function to confirm the -1 return value for an empty list."""
    assert (
        find_and_remove_max([]) == -1
    )  # in this edge case, the empty list input should lead to this return of -1

"""Using unit tests to test utility functions."""

__author__ = "730754494"

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_empty_only_evens() -> None:
    """Unit test function to confirm the correct empty list response."""
    assert (
        only_evens(integer_list=[]) == []
    )  # asserting that an empty list will return an empty list


def test_return_only_evens() -> None:
    """Unit test function to test only_evens' return response."""
    assert only_evens(integer_list=[1, 3, 4]) == [
        4
    ]  # the function should return a list with only the even integers


def test_mutation_only_evens() -> None:
    """Unit test function to check that only_evens does not alter the input."""
    number_list: list[int] = [
        3,
        5,
        6,
    ]  # establishing an input list to make sure it will not be changed
    only_evens(number_list)
    assert number_list == [
        3,
        5,
        6,
    ]  # number_list should be the same after being used as an input in only_evens


def test_start_index_sub() -> None:
    """Unit test function confirming an empty list return if start index is too big."""
    assert sub(integer_list=[1, 2, 3], index_start=5, index_end=7) == []
    # checking for the empty list return


def test_return_sub() -> None:
    """Unit test function to confirm that sub returns values correctly."""
    assert sub(integer_list=[1, 4, 5, 8, 11, 15], index_start=2, index_end=5) == [
        5,
        8,
        11,
    ]  # testing the proper function use of the sub function


def test_mutation_sub() -> None:
    """Unit test function to confirm that sub does not modify input list."""
    number_list: list[int] = [8, 8, 6]  # local variable for the test
    sub(number_list, 2, 5)  # inputting the local variable into sub
    assert number_list == [8, 8, 6]  # the number list should not have changed


def test_negatives_add_at_index() -> None:
    """Unit test function to confirm the mutation with negative integers."""
    number_list: list[int] = [-5, -6, -5]
    add_at_index(
        integer_list=number_list, element=-3, index=2
    )  # putting the negative numbers into the function
    assert number_list == [
        -5,
        -6,
        -3,
        -5,
    ]  # the list should still show negative numbers


def test_return_add_at_index() -> None:
    """Unit test function to confirm that the function will always return None."""
    assert (
        add_at_index(integer_list=[5, 6, 5], element=3, index=1) == None
    )  # testing that any input will return None


def test_mutation_add_at_index() -> None:
    """Unit test function to confirm that the input list will be mutated."""
    number_list: list[int] = [5, 6, 5]
    add_at_index(
        integer_list=number_list, element=3, index=2
    )  # these are valid requirements to proceed through the definition
    assert number_list == [5, 6, 3, 5]  # the input list will now be mutated

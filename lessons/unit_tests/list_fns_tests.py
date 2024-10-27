"""Testing functions in lists_fns"""

from lists_fns import get_first, remove_first, check


def test_get_first() -> None:
    assert get_first(input=["Viktorya", "Samy", "Izzi"]) == "Viktorya"


def test_remove_first() -> None:
    my_TAs: list[str] = ["Viktorya", "Samy", "Benjamin"]
    remove_first(my_TAs)
    assert my_TAs == ["Samy", "Benjamin"]


def test_return_check() -> None:
    nums: list[int] = [1]
    assert check(nums) is True

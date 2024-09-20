"""Practice with while loops!"""

__author__ = "730754494"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = (
        0  # this is keeping track of the times that search_char appears in phrase
    )
    index: int = (
        0  # this number is used to make the while loop stop at the end of the phrase
    )
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    return count  # I am returning the count of the times search_char is in phrase

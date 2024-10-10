"""Folder for concatenating two strings to make one longer string."""

__author__ = "730754494"


def concat(
    str_1: str, str_2: str
) -> str:  # this function is made to input strings and lead to a string
    return str_1 + str_2


word1: str = "happy"  # these variables are being assigned globally
word2: str = "tuesday"
if (
    __name__ == "__main__"
):  # this line suppresses the call to the function when imported
    print(concat(str_1=word1, str_2=word2))

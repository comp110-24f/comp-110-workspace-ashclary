"""Folder for concatenating two strings to make one longer string."""

__author__ = "730754494"


def concat(str_1: str, str_2: str) -> str:
    return str_1 + str_2


word1: str = "happy"
word2: str = "tuesday"
if __name__ == "__main__":
    print(concat(str_1=word1, str_2=word2))

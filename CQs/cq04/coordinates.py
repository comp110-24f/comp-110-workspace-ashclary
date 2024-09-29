"""Function to find the pairs from each string."""

__author__ = "730754494"


def get_coords(xs: str, ys: str) -> None:
    index: int = 0
    while index < len(xs):
        index2: int = 0
        while index2 < len(ys):
            print(f"({xs[index]},{ys[index2]})")
            index2 += 1
        index += 1

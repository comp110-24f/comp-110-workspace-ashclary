"""Function to find the pairs from each string."""

__author__ = "730754494"


def get_coords(xs: str, ys: str) -> None:
    index: int = 0  # I am checking each index for the first string
    while index < len(xs):
        index2: int = 0  # I am also checking each index on the second string
        while index2 < len(ys):
            print(f"({xs[index]},{ys[index2]})")  # here is the printed output line
            index2 += (
                1  # increasing the index will cause the while loop to not be infinite
            )
        index += 1

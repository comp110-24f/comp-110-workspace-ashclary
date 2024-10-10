"""Folder for importing functions from concatenation and coordinates."""

__author__ = "730754494"

from CQs.cq04.concatenation import (
    concat,
)  # I am importing to have access to the concat function
from CQs.cq04.coordinates import get_coords

x: str = "123"  # these are again global variables being assigned
y: str = "abc"
print(concat(x, y))  # I can not access the print of the imported function


get_coords(x, y)

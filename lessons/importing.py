"""Practice importing"""

from lessons.scope_practice import remove_chars
from CQs.cq05_lists import manual_append
from CQs.cq05_lists import double

print(remove_chars("hi", "h"))

a: list[int] = [1, 2, 3]

manual_append(a, 2)
print(a)

double(a)
print(a)

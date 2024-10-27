"""Examples of dictionary syntax with Ice Cream SHop order tallies."""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 4}

my_dict: dict[int, str] = {8: "dog", 1: "cat", 10: "mouse", 15: "bird", 0: "whale"}
for x in my_dict:
    print(my_dict[x])

for x in my_dict:
    print(x)

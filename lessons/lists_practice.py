"""Practice with lists"""

my_numbers: list[float] = []  # with a literal
my_numbers: list[float] = list()  # with constructor
my_numbers.append(1.5)  # to add a value to the end of a list

# initializing an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)
print(game_points[2])
print(game_points[len(game_points) - 1])
game_points[1] = 72  # modifying by index
game_points.append(22)  # add an item to a list
game_points.append(22)
print(game_points)
game_points.pop(1)  # remove an item from a list
print(game_points)

"""Program to help users plan a tea party!"""

__author__: str = "730754494"


def main_planner(guests: int) -> None:
    """A function to plan a tea party"""
    print("A Cozy Tea Party For " + str(guests) + " People")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # this function works to combine all the return values by calling and printing


def tea_bags(people: int) -> int:
    """Function to find how many tea bags are needed"""
    return people * 2


def treats(people: int) -> int:
    """Function to find how many treats are needed"""
    return int(tea_bags(people=people) * 1.5)
    # note that I need to specify the int and the argument from the previous definition


def cost(tea_count: int, treat_count: int) -> float:
    """Function to find the total cost of the party"""
    return 0.50 * tea_count + 0.75 * treat_count
    # this approach is used to allow for different costs for tea and treats


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    # this line involves letting the program run based on the user's input

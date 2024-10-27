"""Exercise for working with utility functions for dictionaries."""

__author__ = "730754494"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Function to invert the dictionary's value and keys."""
    inverted_dict: dict[str, str] = {}  # creating an empty dict to return at end
    for element in inp_dict:  # this for loop iterates through the keys in inp_dict
        if (
            inp_dict[element] in inverted_dict
        ):  # if the value is already established as a new key, there is an error
            raise KeyError("Cannot have multiple of the same key!")
        else:  # means that the value can become a unique key
            inverted_dict[inp_dict[element]] = (
                element  # making inp_dict's values be inverted_dict's keys
            )
    return inverted_dict  # returning the new inverted dict


def favorite_color(colors_dict: dict[str, str]) -> str:
    """Function to return the most popular color that people chose."""
    count: dict[str, int] = {}  # creating an empty dict to keep track of count
    greatest_color: str = ""  # establishing an empty string for eventual return
    for element in colors_dict:
        if (
            colors_dict[element] in count
        ):  # if the color value is already present, cannot add it again as a key
            count[
                colors_dict[element]
            ] += 1  # will increase the integer to show another instance of the color
        else:
            count[colors_dict[element]] = (
                1  # putting the color and integer key-value pair in the dict
            )
    highest_count: int = 0  # starting at 0 to test the count of each color
    for color in count:
        if (
            count[color] > highest_count
        ):  # replacing the highest count only if greater, not equal
            highest_count = count[color]
            greatest_color = color  # assigning the current color to the greatest
    return (
        greatest_color  # will return the key from count, which is the value from input
    )


def count(inp_strings: list[str]) -> dict[str, int]:
    """Function to return a dict with strings and the # of instances of them in list."""
    result: dict[str, int] = {}  # using a literal to make the empty dictionary
    for idx in range(0, len(inp_strings)):  # iterating through the input list
        if inp_strings[idx] in result:  # cannot have duplicate keys present
            result[
                inp_strings[idx]
            ] += 1  # showing that there is another instance of this string
        else:  # will need to add this string as a key
            result[inp_strings[idx]] = (
                1  # assigning a value of 1 to account for the 1 instance
            )
    return result


def alphabetizer(words_list: list[str]) -> dict[str, list[str]]:
    """Function to return a dict tracking the 1st letters and corresponding strings."""
    first_letters: dict[str, list[str]] = (
        {}
    )  # establishing an empty dict to return later
    alphabet_str: str = ""  # to track the present first letters
    for element in words_list:
        if (
            element[0].lower() not in alphabet_str
        ):  # will only add one of each first letter to the string
            alphabet_str += element[0].lower()  # element at index 0 is the first letter
    for element in alphabet_str:  # going through each letter
        for word in words_list:
            if (
                word[0].lower() == element
            ):  # seeing if the first letter corresponds with the letter
                if word[0].lower() in first_letters:
                    first_letters[word[0].lower()].append(
                        word
                    )  # appending the string as another instance
                else:
                    first_letters[word[0].lower()] = [
                        word
                    ]  # establishing a key-value pair if not already there
    return first_letters


def update_attendance(
    days_attendance: dict[str, list[str]], day: str, student: str
) -> None:
    """Function to mutate the attendance dict based on string inputs."""
    if (
        day not in days_attendance
    ):  # adding the key-value pair to show the attendance on that day
        days_attendance[day] = [student]  # the input string of day becomes the key
    else:  # if day is already a key, I cannot add it again
        days_attendance[day].append(
            student
        )  # appending to show an increase for that attendance list

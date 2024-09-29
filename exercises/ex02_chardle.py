"""Chardle exercise for finding instances of a letter in a word!"""

__author__ = "730754494"


def input_word() -> str:
    five_character_word: str = str(
        input("Enter a 5-character word: ")
    )  # the input should be converted to a str to confirm he correct type
    if (
        len(five_character_word) != 5
    ):  # this line is checking if the value of the input fits the character length
        print("Error: Word must contain 5 characters.")
        exit()
    return five_character_word


def input_letter() -> str:
    single_character: str = str(input("Enter a single character: "))
    if len(single_character) != 1:
        print(
            "Error: Character must be a single character."
        )  # the error message is printed to tell the user about the problem
        exit()
    return single_character  # either way, we still return the str character value


def contains_char(word: str, letter: str) -> None:
    print(str("Searching for " + letter + " in " + word))
    character_counter: int = (
        0  # the counter tracks the number of times that the letter appears in the word
    )
    if word[0] == letter:
        print(letter + " found at index 0")
        character_counter += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        character_counter += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        character_counter += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        character_counter += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        character_counter += 1
    if character_counter == 0:
        print("No instances of " + letter + " found in " + word)
    elif character_counter == 1:
        print(str(character_counter) + " instance of " + letter + " found in " + word)
    else:  # this else block applies to all entries that do not fit the if and the elif
        print(str(character_counter) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(
        word=input_word(), letter=input_letter()
    )  # this line works to connect all of the previous functions to make use easier


if __name__ == "__main__":
    main()

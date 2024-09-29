"""A wordle game for the user to guess a word and see information about the letters."""

___author__ = "730754494"


def input_guess(secret_word_len: int) -> str:
    """A function to make sure that the length of the guess is correct."""
    guess = str(
        input(f"Enter a {secret_word_len} character word: ")
    )  # this line assigns the user's input to the secret word
    while len(guess) != secret_word_len:
        guess = str(
            input(f"That wasn't {secret_word_len} chars! Try again: ")
        )  # this new phrase can still be used to update the secret word
    return guess  # the return happens once the length is correct


def contains_char(secret_word: str, char_guess: str) -> bool:
    """A function to determine whether the guess and character have a match."""
    assert len(char_guess) == 1
    index: int = (
        0  # I start with this index of 0 to then check each letter in the secret word
    )
    while index < len(secret_word):
        if (
            secret_word[index] == char_guess
        ):  # having a match will mean that the guessed character is in the word
            return True
        index += 1
    return False  # False becomes returned if no character matches


def emojified(guess: str, secret_word: str) -> str:
    """A function that displays emojis to indicate character matches."""
    assert len(guess) == len(secret_word)
    string_boxes: str = ""  # this string starts as empty to then add the boxes
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    while index < len(guess):  # I made a loop to check each character in guess
        if guess[index] == secret_word[index]:
            string_boxes += GREEN_BOX
        elif contains_char(
            secret_word, guess[index]
        ):  # calling contains_char checks if the character is present
            string_boxes += YELLOW_BOX
        else:
            string_boxes += WHITE_BOX  # the final else then adds the white box
        index += 1
    return string_boxes  # the string is returned so I can then print it


def main(secret_word: str) -> None:
    """This function connects the other functions."""
    user_turn: int = 1
    guess_status: bool = False  # this bool establishes when the guess becomes correct
    while (
        user_turn <= 6 and not guess_status
    ):  # not guess_status means the while loop does not eneter if guess is True
        print(f"=== Turn {user_turn}/6 ===")
        guess = input_guess(
            secret_word_len=len(secret_word)
        )  # connecting guess to the user's input in input_guess
        print(
            emojified(guess=guess, secret_word=secret_word)
        )  # keyword arguments to output the box string for the user's guess
        user_turn += 1
        if guess == secret_word:
            guess_status = True
    if guess_status:
        print(
            f"You won in {user_turn-1}/6 turns!"
        )  # this means that the guess_status is True with the guess being correct
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="codes")

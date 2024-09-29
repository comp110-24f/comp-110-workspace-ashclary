def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with the instances of char removed."""
    copy: str = ""  # set up empty string for copying values
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
        index += 1
    return copy


print(remove_chars("hi", "i"))

if __name__ == "__main__":
    word: str = "yoyo"
    print(remove_chars(word, "y"))
    print(word)

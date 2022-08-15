from random_word import RandomWords


def setup_word_length() -> str:
    return 3
    difficulty = input("Select difficulty (Easy, Normal, Hard): ")
    return DIFFICULTIES[difficulty.lower()]


def generate_word(word_len: str) -> str:
    """
    Generates a random word. The length is based on the difficulty selected.
    """
    return RandomWords().get_random_word(
        hasDictionaryDef="true",
        minLength=word_len,
        maxLength=word_len,
    )

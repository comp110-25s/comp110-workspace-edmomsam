"A Program to run the Game of Wordle"

__author__: str = "730549027"

"""Code for Emojified Boxes"""


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(secret_character: str, character: str) -> bool:
    """Checks if the given character exists in the search string"""
    assert len(character) == 1, f"len('{character}')is not 1"
    idx = 0
    while idx < len(secret_character):
        if character == secret_character[idx]:
            return True
        else:
            idx = idx + 1
    return False


def emojified(guess: str, secret_character: str) -> str:
    """Emojified The Inputs"""
    assert len(guess) == len(secret_character), "Guess must be same length as secret"
    idx = 0
    box_string: str = ""
    while idx < len(secret_character):
        if guess[idx] == secret_character[idx]:
            box_string = box_string + GREEN_BOX
        elif contains_char(secret_character, guess[idx]):
            box_string = box_string + YELLOW_BOX
        else:
            box_string = box_string + WHITE_BOX
        idx = idx + 1
    return f"{box_string}"


def input_guess(expected_length: int) -> str:
    """Function Permiting Users to Input Guesses"""
    word = input(f"Enter a {expected_length} character word:")
    while expected_length != len(word):
        word = input(f"That wasn't {expected_length} chars! Try again:")
    return word


def main(secret_character: str) -> None:
    """The entry point of the program and maingame loop."""
    secret_character = "codes"
    turn = 1
    max_attempts = 6
    won = False
    while turn <= max_attempts and not won:
        print(f"=== Turn {turn}/6 ===")
        word = input_guess(len(secret_character))
        if word == secret_character:
            print(f"{emojified(word, secret_character)}")
            print(f"You won in {turn}/6 turns!")
            won = True
        else:
            print(f"{emojified(word, secret_character)}")
        turn = turn + 1
    if won is False:
        print("X/6 - sorry try again tomorrow!")


if __name__ == "__main__":
    main(secret_character="codes")

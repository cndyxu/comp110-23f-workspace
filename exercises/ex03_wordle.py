"""EX03 - Wordle!"""
__author__ = "730479883"


def contains_char(word: str, character: str) -> bool:
    """Generates a bool value depending on if a character from the guess word is in the secret word."""
    assert len(character) == 1
    index: int = 0
    while index < len(word):
        if word[index] == character:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Generates certain colored boxes depending on if the guess character or word are in the secret word."""
    assert len(guess) == len(secret)
    YELLOW_BOX: str = "\U0001F7E8"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    emoji: str = ""
    second_index: int = 0
    while second_index < len(secret):
        if contains_char(secret, guess[second_index]) is False:
            emoji += WHITE_BOX
        else:
            if secret[second_index] != guess[second_index]:
                emoji += YELLOW_BOX
            else:
                emoji += GREEN_BOX
        second_index += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Prompts user for guess of expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn_number: int = 0
    playing: bool = True
    while playing:
        turn_number += 1
        print(f"=== Turn {turn_number}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn_number}/6 turns!")
            playing = False
        elif turn_number > 5:
            print("X/6 - Sorry, try again tomorrow!")
            playing = False


if __name__ == "__main__":
    main()
"""One Shot Wordle."""
__author__ = "730479883"

secret_word: str = "python"
guessed_word: str = input(f"What is your {len(secret_word)}- letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
emoji_box: str = ""
anywhere_else: bool = False
second_index: int = 0

while len(guessed_word) != len(secret_word) and guessed_word != secret_word:
    guessed_word = input(f"That was not {len(secret_word)} letters! Try again: ")

if len(guessed_word) == len(secret_word):
    if guessed_word == secret_word:
        while index < len(secret_word):
            if guessed_word[index] == secret_word[index]:
                emoji_box = emoji_box + GREEN_BOX
                index = index + 1
    else:
        while index < len(secret_word):
            if guessed_word[index] == secret_word[index]:
                emoji_box = emoji_box + GREEN_BOX
            else:
                while second_index < len(secret_word) and anywhere_else is not True:
                    if guessed_word[index] == secret_word[second_index]:
                        emoji_box = emoji_box + YELLOW_BOX
                        anywhere_else = True
                    else:
                        anywhere_else = False
                    second_index = second_index + 1
                if anywhere_else is not True:
                    emoji_box = emoji_box + WHITE_BOX
                anywhere_else = False
            second_index = 0
            index = index + 1

print(emoji_box)

if guessed_word == secret_word:
    print("Woo! You got it!")
if guessed_word != secret_word:
    print("Not quite. Play again soon!")
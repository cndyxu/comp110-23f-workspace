"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730479883"

letter_count: int = 0

chosen_word: str = input("Enter a 5-character word: ")
if len(chosen_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

chosen_letter: str = input("Enter a single character: ")
if len(chosen_letter) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + chosen_letter + " in " + chosen_word)
if chosen_word[0] == chosen_letter:
    print(chosen_letter + " found at index 0")
    letter_count = letter_count + 1
if chosen_word[1] == chosen_letter:
    print(chosen_letter + " found at index 1")
    letter_count = letter_count + 1
if chosen_word[2] == chosen_letter:
    print(chosen_letter + " found at index 2")
    letter_count = letter_count + 1
if chosen_word[3] == chosen_letter:
    print(chosen_letter + " found at index 3")
    letter_count = letter_count + 1
if chosen_word[4] == chosen_letter:
    print(chosen_letter + " found at index 4")
    letter_count = letter_count + 1

if letter_count == 0:
    print("No instances of " + chosen_letter + " found in " + chosen_word)
if letter_count == 1:
    print("1 instance of " + chosen_letter + " found in " + chosen_word)
if letter_count >= 2:
    print(str(letter_count) + " instances of " + chosen_letter + " found in " + chosen_word)
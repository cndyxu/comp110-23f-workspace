"""Using built-in commands to practice dictionaries."""

__author__ = "730479883"


def invert(d1: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values of a dictionary using loops and returning an error message when there is more than one of the same key."""
    invert_dict: dict[str, str] = {}
    for key, value in d1.items():
        if value in invert_dict:
            raise KeyError("Cannot have duplicated key")
        invert_dict[value] = key  
    return invert_dict


def favorite_color(d2: dict[str, str]) -> str:
    """Finding the most popular color that appears in a dictionary of names and favorite colors."""
    colors: list[str] = []
    i: int = 0
    most_color: str = ""
    for key in d2:
        colors.append(d2[key])
    count_colors: dict[str, int] = count(colors)
    for key in count_colors:
        if count_colors[key] > i:
            most_color = key
            i = count_colors[key]
    return most_color


def count(l1: list[str]) -> dict[str, int]:
    """Counting the amount of times that a value is in a dictionary and returning that value."""
    count_dict: dict[str, int] = {}
    for item in l1:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def alphabetizer(l2: list[str]) -> dict[str, list[str]]:
    """Assigning each key in a dictionary to a unique letter in the alphabet where the value is a list of the words that start with that letter."""
    alphabet_dict: dict[str, list[str]] = {}
    for word in l2:
        if word and word[0].isalpha():
            first_letter = word[0].lower()
            if first_letter in alphabet_dict:
                alphabet_dict[first_letter].append(word)
            else:
                alphabet_dict[first_letter] = [word]
    return alphabet_dict


def update_attendance(attendance_dict: dict[str, list[str]], day_of_week: str, student_name: str) -> dict[str, list[str]]:
    """Mutating a dictionary to have the day of the week as the key and the names of each student that attended that day as the value."""
    if day_of_week in attendance_dict:
        attendance_dict[day_of_week].append(student_name)
    else:
        attendance_dict[day_of_week] = [student_name]
    return attendance_dict

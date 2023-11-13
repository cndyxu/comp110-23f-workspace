"""List Utility Functions."""
__author__ = "730479883"


def all(l1: list[int], number: int) -> bool:
    """Find the number in the given list."""
    index: int = 0
    count: int = 0
    while index < len(l1):
        if number == l1[index]:
            count += 1
        index += 1

    if len(l1) == 0:
        return False
    elif count == len(l1):
        return True
    else:
        return False
   

def max(input: list[int]) -> int:
    """Find the largest int in the given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    second_index: int = 1
    highest_list: int = input[0]
    while second_index < len(input):
        if input[second_index] > highest_list:
            highest_list = input[second_index]
        second_index += 1
    return highest_list


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Find if every int is equal in both given lists."""
    index = 0
    if len(list1) != len(list2):
        return False
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1
    return True
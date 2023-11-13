"""Combining two lists into a dictionary."""

__author__ = "730479883"


def zip(l1: list[str], l2: list[int]) -> dict[str, int]:
    """Creating an if then statement that sets the parameters being l1 and l2 being the same length and not equaling 0 in order to have l1 be the keys and l2 be the values, otherwise returning an empty dict."""
    final_dict: dict[str, int] = {} 

    if len(l1) == len(l2) and len(l1) != 0 and len(l2) != 0:
        final_dict = {l1[i]: l2[i] for i in range(len(l1))}
    else:
        final_dict = {} 
    return final_dict

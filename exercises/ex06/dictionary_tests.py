"""Writing Unit Tests: EX07."""

__author__ = "730479883"

import pytest
from dictionary import invert, favorite_color, count, alphabetizer, update_attendance

def test_invert_expected_1():
    """Testing the the expected use case of the invert fuction."""
    d1: dict = {'mickey': 'mouse', 'donald': 'duck'}
    expected_dict = invert(d1)
    assert expected_dict == {'mouse': 'mickey', 'duck': 'donald'}


def test_invert_expected_2():
    """Testing the expected use case of the invert function with a different valid use case."""
    d2: dict = {'cindy': 'xu', 'ben': 'frens'}
    expected_dict2 = invert(d2)
    assert expected_dict2 == {'xu': 'cindy', 'frens': 'ben'}

def test_invert_edge():
    """Testing an edge case for the invert function"""
    d3: dict = {'mickey': 'mouse', 'minnie': 'mouse'}
    expected_dict3 = invert(d3)
    assert expected_dict3 == {'mouse': 'minnie'}


def test_fav_color_expected_1():
    """Testing if favorite_color returns the most common color in a valid use case."""
    color_people: dict = {'blue': 'abby', 'green': 'jake', 'blue': 'jerry'}
    result = favorite_color(color_people)
    assert result == 'blue'


def test_fav_color_expected_1():
    """Testing if favorite_color returns the most common color in another valid use case."""
    color_people2: dict = {'green': 'mary', 'pink': 'max', 'pink': 'ben'}
    result = favorite_color(color_people2)
    assert result == 'pink'


def test_fav_color_error():
    """Test favorite_color with same number values at each key."""
    color_people3: dict = {'green': 'mary', 'pink': 'jasmine', 'blue': 'ben'}
    result = favorite_color(color_people3)
    assert result == 'green, pink, blue'

   


def test_count_expected_1():
    """Testing the count funciton with valid use case."""
    l1: list = ['coke', 'sprite', 'fanta', 'pepsi']
    result = count(l1, 'coke')
    assert result == 1


def test_count_expected_2():
    """Testing the count function with another valid use case."""
    l2: list = ['mary', 'max', 'albert', 'max']
    result = count(l2, 'max')
    assert result == 2


def test_count_value_error():
    """Testing if the count function with empty list input."""
    l3: list [str]= []
    result = count(l3, "annie")
    assert result == 0


def test_alphabetizer_expected_1():
    """Testing the aphabetize function with valid use case."""
    names: list = ['Cindy', 'Ben', 'Candy', 'Adam']
    result = alphabetizer(names)
    assert result == {'A': 'Adam', 'B': 'Ben', 'C': 'Cindy, Candy'}


def test_alphabetizer_expected_2():
    """Testing the alphabetizer function with another valid use case."""
    grocery_list: list = ['Banana', 'Apple', 'Strawberry', 'Milk']
    result = alphabetizer(grocery_list)
    assert result == {'A': 'Apple', 'B': 'Banana', 'M': 'Milk', 'S': 'Strawberry'}

def test_alphabetizer_empty():
    """Test if the alphabetize function returns an empty dictionary with empty input list."""
    result = alphabetizer([])
    assert result == {}


def test_update_attendance_expected_1():
    """Testing the update_attendance function with valid use case."""
    day_of_week: str = "Monday"
    student_name: list[str] = ['Cindy', 'Ben', 'Eva', 'Charlie']
    result = update_attendance(student_name)
    assert result == {'Monday': 'Cindy, Ben, Eva, Charlie'}

def test_update_attendance_expected_2():
    """Testing the update_attendance function with another valid use case."""
    day_of_week: str = "Tuesday"
    student_name: list[str] = ['Sally', 'Ben', 'Cindy', 'Charlie']
    result = update_attendance(student_name)
    assert result == {'Tuesday': 'Sally, Ben, Cindy, Charlie'}

def test_update_attendance_edge():
    """Test update_attendance function with empty list input"""
    day_of_the_week: str = "Monday"
    student_name: list[str] = []
    result = update_attendance(student_name)
    assert result == {}
"""Writing Unit Tests: EX07."""

__author__ = "730479883"

from dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_expected_1():
    """Testing the the expected use case of the invert fuction."""
    input_dict = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
    assert invert(input_dict) == {'apple': 'a', 'banana': 'b', 'cherry': 'c'}


def test_invert_expected_2():
    """Testing the expected use case of the invert function with a different valid use case."""
    d2: dict = {'cindy': 'xu', 'ben': 'frens'}
    expected_dict2 = invert(d2)
    assert expected_dict2 == {'xu': 'cindy', 'frens': 'ben'}


def test_invert_edge():
    """Testing an edge case for the invert function"""
    d4: dict = {}
    expected_dict4 = invert(d4)
    assert expected_dict4 == {}


def test_fav_color_expected_1():
    """Testing if favorite_color returns the most common color in a valid use case."""
    input_dict = {'Alice': 'blue', 'Bob': 'red', 'Charlie': 'blue'}
    assert favorite_color(input_dict) == 'blue'


def test_fav_color_expected_1():
    """Testing if favorite_color returns the most common color in another valid use case."""
    input_dict = {'Alice': 'blue', 'Bob': 'red', 'Charlie': 'red'}
    assert favorite_color(input_dict) in ['blue', 'red']


def test_fav_color_edge():
    """Test favorite_color with same number values at each key."""
    color_people3: dict = {}
    result = favorite_color(color_people3)
    assert '' is None

   
def test_count_expected_1():
    """Testing the count funciton with valid use case."""
    input_list = ['apple', 'banana', 'apple', 'orange', 'banana']
    assert count(input_list) == {'apple': 2, 'banana': 2, 'orange': 1}


def test_count_expected_2():
    """Testing the count function with another valid use case."""
    l2: list = ['mary', 'max', 'albert', 'max']
    result = count('max')
    assert result == 2


def test_count_value_error():
    """Testing if the count function with empty list input."""
    l3: list [str] = []
    assert count(l3) == {}


def test_alphabetizer_expected_1():
    """Testing the aphabetize function with valid use case."""
    input_list = ['apple', 'banana', 'cherry', 'pear']
    assert alphabetizer(input_list) == {'a': ['apple'], 'b': ['banana'], 'c': ['cherry'], 'p': ['pear']}


def test_alphabetizer_expected_2():
    """Testing the alphabetizer function with another valid use case."""
    input_list = ['apple', 'banana', 'cherry', 'pear', 'avocado']
    assert alphabetizer(input_list) == {'a': ['apple', 'avocado'], 'b': ['banana'], 'c': ['cherry'], 'p': ['pear']}


def test_alphabetizer_empty():
    """Test if the alphabetize function returns an empty dictionary with empty input list."""
    result = alphabetizer([])
    assert result == {}


def test_update_attendance_expected_1():
    """Testing the update_attendanpython -m tools.submission exercises/ex06ce function with valid use case."""
    input_dict = {'Monday': ['Alice', 'Bob'], 'Wednesday': ['Charlie']}
    updated_dict = update_attendance(input_dict, 'Friday', 'Dave')
    assert updated_dict == {'Monday': ['Alice', 'Bob'], 'Wednesday': ['Charlie'], 'Friday': ['Dave']}



def test_update_attendance_expected_2():
    """Testing the update_attendance function with another valid use case."""
    input_dict = {'Monday': ['Alice', 'Bob'], 'Wednesday': ['Charlie']}
    updated_dict = update_attendance(input_dict, 'Monday', 'Dave')
    assert updated_dict == {'Monday': ['Alice', 'Bob', 'Dave'], 'Wednesday': ['Charlie']}


def test_update_attendance_edge():
    """Test update_attendance function with empty list input"""
    day_of_the_week: str = "Monday"
    student_name: list[str] = []
    result = update_attendance(day_of_the_week, student_name)
    assert result == {}

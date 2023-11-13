"""Test my zip function."""
from lessons.zip import zip

def test_zip_edgecase():
    result1 = zip([], [1, 2]) 
    result2 = zip(["Hello", "Hi"], [])
    if result1 == {} and result2 == {}:
        print("Edge case passed")
    else:
        print("Test Failed")

def test_usecase1():
    result1 = zip(["Hello", "Hi"], [1])
    result2 = zip(["Hello"], [1, 3])
    if len(result1) != 0 and len(result2) != 0:
        print("Test Failed")
    else:
        print("Use case past")

def test_usecase2():
    results = zip(["Hello", "hi"], [1, 3])
    expected = {"Hello": 1, "hi": 3}
    if results == expected:
        print("Use case 2 passed")
    else:
        print("Test failed")





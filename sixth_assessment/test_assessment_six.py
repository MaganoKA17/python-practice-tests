import pytest
from assessment_six import *

# =========================
# BASIC TESTS
# =========================

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0

def test_count_even():
    assert count_even([1, 2, 3, 4]) == 2
    assert count_even([1, 3, 5]) == 0

def test_capitalize_sentence():
    assert capitalize_sentence("hello world") == "Hello World"
    assert capitalize_sentence("") == ""

def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""

def test_max_in_list():
    assert max_in_list([1, 5, 3]) == 5
    assert max_in_list([]) is None

# =========================
# INTERMEDIATE TESTS
# =========================

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)

def test_remove_duplicates():
    assert remove_duplicates([1,2,2,3,1]) == [1,2,3]
    assert remove_duplicates([]) == []

def test_sum_of_squares():
    assert sum_of_squares([1,2,3]) == 14
    assert sum_of_squares([]) == 0

def test_sort_dict_by_values():
    assert sort_dict_by_values({'a':3,'b':1,'c':2}) == [('b',1),('c',2),('a',3)]
    assert sort_dict_by_values({}) == []

def test_print_multiplication_table():
    assert print_multiplication_table(2) == [[1,2],[2,4]]
    assert print_multiplication_table(0) == []

# =========================
# ADVANCED TESTS
# =========================

def test_rotate_list():
    assert rotate_list([1,2,3,4],2) == [3,4,1,2]
    assert rotate_list([],5) == []

def test_fibonacci_list():
    assert fibonacci_list(5) == [0,1,1,2,3,5]
    assert fibonacci_list(0) == [0]

def test_flatten_list():
    assert flatten_list([1,[2,3],[4,[5]]]) == [1,2,3,4,5]
    assert flatten_list([]) == []

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True

def test_count_inversions():
    assert count_inversions([2,4,1,3,5]) == 3
    assert count_inversions([1,2,3,4]) == 0

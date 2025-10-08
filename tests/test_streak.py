import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test with an empty list, expecting 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_positive_streaks():
    """Test with multiple positive streaks, checking for the longest."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 0, 1]) == 3

def test_with_zeros_and_negatives():
    """Test with lists containing zeros and negative numbers."""
    assert longest_positive_streak([1, 2, -1, 3, 4, 0, 5]) == 2
    assert longest_positive_streak([-1, -2, -3]) == 0
    assert longest_positive_streak([0, 0, 0]) == 0

def test_all_positive():
    """Test with a list of all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_element_list():
    """Test with single element lists."""
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([-1]) == 0
    assert longest_positive_streak([0]) == 0
import pytest
from lib.count_words import count_words 

"""A function called count_words that takes a string as an argument and returns the number of words in that string."""


def test_returns_empty_result():
 result = count_words("")
 assert result == 0

def test_count_five_words_in_string():
    result = count_words("this string has five words")
    assert result == 5

def test_extra_spaces_are_ignored():
    assert count_words("  two   words  ") == 2
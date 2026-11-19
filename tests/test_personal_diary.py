import pytest
from lib.make_snippet import make_snippet

#empty dtring 
def test_given_empty_string_returns_empty():
    result = make_snippet("")
    assert result == ""

#five wordsw 
def test_five_words_return_five_words():
    result = make_snippet("Hello this is five words")
    assert result == "Hello this is five words"

def test_if_eight_words_returns_short_text():
    result = make_snippet("Hello my name is fay but I cant")
    assert result == "Hello my name is fay..."



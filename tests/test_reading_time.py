import pytest
from lib.reading_time import estimate_reading_time

def test_200_words():
    result = estimate_reading_time("word " * 200)
    assert result == 1

def test_400_words():
    result = estimate_reading_time("word " * 400)
    assert result == 2

def test_300_words():
    result = estimate_reading_time("word " * 300)
    assert result == 1.5

def test_empty_text_raises_error():
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    error_message = str(e.value)
    assert error_message == "Can't estimate reading time due to empty text"

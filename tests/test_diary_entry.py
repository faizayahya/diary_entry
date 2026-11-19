import pytest
from lib.classes.diary_entry import DiaryEntry 

#Initially tests title and contents are stored
def test_empty_list():
    entry = DiaryEntry("Title", "Contents")
    assert entry.title == "Title"
    assert entry.contents == "Contents"

#Fails if there is no title
def test_empty_title_wont_move_to_content():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "Contents")
    assert str(e.value) == "Please input title"

#Format returns formatted entry and content 
def test_format_title_and_content():
    diary_entry = DiaryEntry("Title", "Contents")
    result = diary_entry.format()
    assert result == "Title: Contents"

#Returns the number of words in the diary entry 
def test_return_number_of_words_in_diary_entry():
    diary_entry = DiaryEntry("Title", "Contents")
    result = diary_entry.count_words()
    assert result == 2

"""Reading Time Tests"""
def test_two_wpm_two_words():
    diary_entry = DiaryEntry("Title", "one two")
    result = diary_entry.reading_time(2)
    assert result == 1

#def test_two_wpm_three_words():
#def test_reading_time_400_words():
#def test_reading_time_rounds_up():
#def test_reading_time_empty_contents():

"""Returnig words per minute with a timer"""
#wpm x minutes reading chunk 
#test first chunk
#test it returns next chunk
#tests it restarts to beginning 

def test_words_per_minute_with_a_minute_timer():
    diary_entry = DiaryEntry("Title", "here is a text of 7 words")
    result = diary_entry.reading_chunk(2, 1) #2 wpm, 1 minute
    assert result == "here is"

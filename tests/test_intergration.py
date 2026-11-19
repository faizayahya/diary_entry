from lib.classes.diary import Diary 
from lib.classes.diary_entry import DiaryEntry

#Add two entries, see them back in a list

def test_adds_and_lists_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title", "Contents")
    entry_2 = DiaryEntry("Title", "Contents")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]
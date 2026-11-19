# Diary Entry

A small Python class that stores a diary entry and helps you read it. Built with TDD (test-driven development) using pytest.

## What it does

`DiaryEntry(title, contents)` makes one diary entry. It has these methods:

| Method | What it does |
|---|---|
| `format()` | Returns the entry as text: `"Title: Contents"` |
| `count_words()` | Returns how many words are in the formatted entry (title and contents) |
| `reading_time(wpm)` | Returns how many minutes it takes to read the contents at `wpm` words per minute (can be a decimal, like `0.5`) |
| `reading_chunk(wpm, minutes)` | Returns the first `wpm * minutes` words of the contents |

## Diary

`Diary()` holds a list of entries.

| Method | What it does |
|---|---|
| `add(entry)` | Adds a `DiaryEntry` to the diary |
| `all()` | Returns all the entries as a list |

## Errors

- An empty title raises `Exception("Please input title")`.

## Still to do

- `reading_time` should round up to whole minutes.
- `reading_time` should raise an error for empty contents.
- `reading_chunk` should return the next chunk each time it's called, and start again after the end.

## Usage

```python
from lib.classes.diary_entry import DiaryEntry
from lib.classes.diary import Diary

entry = DiaryEntry("My day", "I went for a long walk")
diary = Diary()
diary.add(entry)
diary.all()                  # [entry]
entry.format()               # "My day: I went for a long walk"
entry.reading_time(200)      # 0.03 (6 words at 200 wpm)
entry.reading_chunk(2, 1)    # "I went"
```

## Setup

```
python -m venv venv
source venv/bin/activate
pip install pytest
```

## Run the tests

Run this from the project root (the folder that contains `lib` and `tests`):

```
pytest
```

For more detail:

```
pytest -v
```

## Project layout

```
lib/classes/diary_entry.py     the DiaryEntry class
lib/classes/diary.py           the Diary class
tests/test_diary_entry.py      unit tests for DiaryEntry
tests/test_intergration.py     integration test for Diary and DiaryEntry together
```

## Other files
 
The other files in `lib` (such as `check_grammar.py`, `count_words.py`, `factorial.py`, `make_snippet.py`, `reading_time.py` and `vowel_remover.py`) are separate practice exercises. They aren't used by the diary.
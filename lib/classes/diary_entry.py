class DiaryEntry:
    def __init__(self, title, contents):
        if title == "":
            raise Exception("Please input title")
        self.title = title
        self.contents = contents 

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
        contents_word_count = len(self.contents.split())
        return contents_word_count / wpm


    def reading_chunk(self, wpm, minutes):
        contents = self.contents.split()
        word_limit = wpm * minutes 
        chunk = contents[:word_limit]
        return " ".join(chunk)
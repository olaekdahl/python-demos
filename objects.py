class Movie:
    def __init__(self, title, year, minutes, category_id=-1):
        self.category_id = category_id
        self.title = title
        self.year = year
        self.minutes = minutes
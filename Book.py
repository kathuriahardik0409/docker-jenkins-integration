class Book:
    def __init__(self, bookId, title, author, year):
        self._id = bookId
        self._title = title
        self._author = author
        self._year = year

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @id.setter
    def id(self, bookId):
        self._id = bookId

    @title.setter
    def title(self, title):
        self._title = title

    @author.setter
    def author(self, author):
        self._author = author

    @year.setter
    def year(self, year):
        self._year = year


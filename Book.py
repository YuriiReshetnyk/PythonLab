

class Book:

    def __init__(self, price: float, pages: int, name_of_the_book: str, name_of_author: str) -> None:
        self._price = price
        self._pages = pages
        self._name_of_author = name_of_author
        self._name_of_the_book = name_of_the_book

    def __str__(self):
        return f"The book \"{self._name_of_the_book.title()}\", which has {self._name_of_author.title()} as an author, " \
               f"has {self._pages} pages and cost {self._price}$"

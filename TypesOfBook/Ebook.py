from Book import *


class Ebook(Book):

    def __init__(self, price: float, pages: int, name_of_the_book: str, name_of_author: str, charge: float):
        super().__init__(price, pages, name_of_the_book, name_of_author)
        self.__charge = charge

    def __str__(self):
        return f"The e-book \"{self._name_of_the_book.title()}\", " \
               f"which has {self._name_of_author.title()} as an author, " \
               f"has {self._pages} pages and cost {self._price}$ and has {self.__charge} charge"

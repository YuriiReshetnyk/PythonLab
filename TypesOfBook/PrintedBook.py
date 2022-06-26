from Book import *


class PrintedBook(Book):

    def __init__(self, price: float, pages: int, name_of_the_book: str,
                 name_of_author: str, name_of_manufacturer: str):
        super().__init__(price, pages, name_of_the_book, name_of_author)
        self.__name_of_manufacturer = name_of_manufacturer

    def __str__(self):
        return f"The printed book \"{self._name_of_the_book.title()}\", which has {self._name_of_author.title()} " \
               f"as an author and was made by {self.__name_of_manufacturer}," \
               f"has {self._pages} pages and cost {self._price}$"

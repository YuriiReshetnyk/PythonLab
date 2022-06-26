from Book import *


class AudioBook(Book):

    def __init__(self, price: float, pages: int, name_of_the_book: str, name_of_author: str, time: float):

        super().__init__(price, pages, name_of_the_book, name_of_author)
        self.__time = time

    def __str__(self):
        return f"The audiobook \"{self._name_of_the_book.title()}\", " \
               f"which has {self._name_of_author.title()} as an author, " \
               f"has {self._pages} pages in paper format and cost {self._price}$ and last {self.__time} minutes"

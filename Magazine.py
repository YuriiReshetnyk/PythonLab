

class Magazine:

    def __init__(self, name: str, name_of_author: str, price: float,
                 pages: int, time_between_release: int):
        self.__name = name
        self.__name_of_author = name_of_author
        self.__price = price
        self.__pages = pages
        self.__time_between_release = time_between_release  # in days

    def __str__(self):
        return f"The magazine \"{self.__name.title()}\", which has {self.__name_of_author.title()} as author, " \
               f"cost {self.__price}$ and has {self.__pages} pages and " \
               f"has {self.__time_between_release} days between releases"



class Monograph:

    def __init__(self, name: str, name_of_author: str, topic_of_work: str, pages: int):

        self.__name = name
        self.__name_of_author = name_of_author
        self.__topic_of_work = topic_of_work
        self.__pages = pages

    def __str__(self):
        return f"The monograph \"{self.__name.title()}\",which has {self.__name_of_author.title()} as an author, " \
               f"has {self.__topic_of_work.title()} as a topic and consist of {self.__pages} pages"

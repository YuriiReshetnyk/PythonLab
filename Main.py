from TypesOfBook.Audiobook import AudioBook
from TypesOfBook.Ebook import Ebook
from Magazine import Magazine
from Monograph import Monograph
from TypesOfBook.PrintedBook import PrintedBook


def main() -> None:
    first_book = PrintedBook(100, 254, "The best day of the year", "Coby", "ManaBanana")
    print(first_book)
    print("___________________________________________________________________________________________________________")
    second_book = Ebook(35.5, 154, "The best week of the year", "Oleh", 95.5)
    print(second_book)
    print("___________________________________________________________________________________________________________")
    third_book = AudioBook(35.5, 154, "The best mouth of the year", "Oleh", 95.5)
    print(third_book)
    print("___________________________________________________________________________________________________________")
    magazine = Magazine("the best author of the year", "Cody", 29.9, 30, 7)
    print(magazine)
    print("___________________________________________________________________________________________________________")
    monograph = Monograph("Secrets of the solar system", "Cory", "astronomy", 548)
    print(monograph)


if __name__ == '__main__':
    main()

# 1 задание
from dataclasses import dataclass, field
from typing import Optional


class InvalidAuthorValueError(Exception):
    pass


class InvalidPageCountError(Exception):
    pass


class InvalidYearError(Exception):
    pass


class InvalidPriceError(Exception):
    pass


@dataclass(order=True)
class Book:
    pages: int
    year: int
    author: str
    price: float
    book_id: Optional[int] = field(init=False, default=None, compare=False)

    def __post_init__(self):
        if self.pages <= 0 or not isinstance(self.pages, int):
            raise InvalidPageCountError("Кол-во страниц должно быть больше 0")
        elif (2024 < self.year < 0) or not isinstance(self.year, int):
            raise InvalidYearError("Год не может быть меньше 0 и больше нынешнего года")
        elif self.author == "" or not isinstance(self.author, str):
            raise InvalidAuthorValueError("Автор не указан")
        elif self.price <= 0 or not isinstance(self.price, (int, float)):
            raise InvalidPriceError("Цена не может быть отрицательной")

    def comparasion_price(self, other):
        if self.price == other.price:
            return f"The price of book with ID {self.book_id} = book with ID {other.book_id}"
        elif self.price < other.price:
            return f"The price of book with ID {self.book_id} < than a book with ID {other.book_id}"
        elif self.price > other.price:
            return f"The price of book with ID {self.book_id} > than a book with ID {other.book_id}"

    def __str__(self):
        return f"""
        Book_ID = {self.book_id},
        author = {self.author},
        pages = {self.pages},
        year = {self.year},
        price = {self.price}
        """


class Library:

    def __init__(self):
        self.dict_books = dict()
        self.id = 1
        pass

    def add_book(self, book: Book):
        if book.book_id is None:
            book.book_id = self.id
            self.id += 1
        self.dict_books.update({book.book_id: book})

    def get_book_info(self, book_id):
        for id in self.dict_books.keys():
            if id == book_id:
                return self.dict_books.get(id)

    def find_author(self, author):
        for book in self.dict_books.values():
            if author in book.author:
                return book

    def __str__(self):
        return f"Books {self.dict_books.values()}"


book1 = Book(215, 2003, "Price", 19.2)
book2 = Book(312, 2012, "Ann", 13.7)

lib = Library()
lib.add_book(book1)
lib.add_book(book2)


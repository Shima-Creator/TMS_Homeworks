# 1 задание
from dataclasses import dataclass


class BookValueError(Exception):
    pass


@dataclass(order=True)
class Book:
    pages: int
    year: int
    author: str
    price: float
    book_id: int = None

    def __post_init__(self):
        if self.pages <= 0 or not isinstance(self.pages, int):
            raise BookValueError("Кол-во страниц должно быть больше 0")
        elif (2024 < self.year < 0) or not isinstance(self.year, int):
            raise BookValueError("Год не может быть меньше 0 и больше нынешнего года")
        elif self.author == "" or not isinstance(self.author, str):
            raise BookValueError("Автор не указан")
        elif self.price <= 0 or not isinstance(self.price, (int, float)):
            raise BookValueError("Цена не может быть отрицательной")

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
        self.list_books = list()
        self.id = 1
        pass

    def add_book(self, book: Book):
        if book.book_id is None:
            book.book_id = self.id
            self.id += 1
        self.list_books.append(book)

    def get_book_info(self, book_id):
        for book in self.list_books:
            if book.book_id == book_id:
                return book

    def find_author(self, authors):
        for book in self.list_books:
            if book.author in self.list_books:
                return book

    def __str__(self):
        return f"Books {self.list_books}"




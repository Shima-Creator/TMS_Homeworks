import classes


book1 = classes.Book(pages=176, year=2013, author="Shima", price=10)
book2 = classes.Book(pages=180, year=2017, author="Shuba", price=12)
book3 = classes.Book(pages=111, year=2011, author="Kirill", price=17)

print(book1)

lib = classes.Library()

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

print(lib)

print(book2.comparasion_price(book1))
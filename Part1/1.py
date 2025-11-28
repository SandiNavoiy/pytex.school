class Book:
    pages = 300
    genre = "Фантастика"

book1 = Book()
book2 = Book()
book1.title = "Гарри Поттер"
book2.title = "Властелин Колец"
book1.author = "Джоан Роулинг"
book2.author = "Джон Толкин"
def decrease_book(book):
    print(f"Title : {book.title}")
    print(f"Author : {book.author}")
    print(f"Pages : {book.pages}")
    print(f"Genre : {book.genre}")

decrease_book(book1)
decrease_book(book2)

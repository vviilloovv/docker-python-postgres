from demo.fib import fib
from demo.db.setting import session
from demo.db.models.user import User
from demo.db.models.book import Book


def add_user(name: str, age: int):
    user = User()
    user.name = name
    user.age = age
    session.add(user)
    session.commit()


def all_users() -> list[User]:
    return session.query(User).all()


def add_book(title: str, author: str):
    book = Book()
    book.title = title
    book.author = author
    session.add(book)
    session.commit()


def all_books() -> list[Book]:
    return session.query(Book).all()


def main():
    print(fib(5))
    add_user(name="Alice", age=17)
    add_book(title="SLAM DUNK", author="井上雄彦")

    for user in all_users():
        print(f"id: {user.id} name: {user.name} age: {user.age}")

    for book in all_books():
        print(f"id: {book.id} title: {book.title} author: {book.author}")


if __name__ == "__main__":
    main()

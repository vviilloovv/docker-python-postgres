from sqlalchemy import Column, Integer, String, Sequence
from demo.db.setting import Base


class Book(Base):
    """
    Book
    """
    __tablename__ = "books"
    id = Column(Integer, Sequence("book_id_seq"), primary_key=True)
    title = Column(String(30))
    author = Column(String(30))

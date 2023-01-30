from sqlalchemy import Column, Integer, String, Sequence
from demo.db.setting import Base


class User(Base):
    """
    User
    """
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(20))
    age = Column(Integer)

from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Table, Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True)
    username = Column(String)
    password = Column(String)
    books = relationship('Book', back_populates='users')
    reviews = relationship('Review', back_populates= 'users')

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    stocked = Column(Boolean)
    owner_id = Column(Integer,ForeignKey('users.id'))
    rating = Column(Integer)
    owner = relationship('User', back_populates= 'book_owners')
    reviews = relationship('Review', back_populates= 'books')

class Review(Base):
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    comment = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    users = relationship('User', back_populates='user_reviews')
    books =relationship('Book', back_populates='book_reviews')

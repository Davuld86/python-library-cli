from sqlalchemy import create_engine, delete
from sqlalchemy import ForeignKey, Table, Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

class Base(DeclarativeBase):
    pass

engine = create_engine('sqlite:///library.sql', echo= True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


class User_db(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True)
    username = Column(String)
    password = Column(String)
    books = relationship('Book_db', back_populates='owner_id')
    reviews = relationship('Review_db', back_populates= 'user_id')

class Book_db(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    stocked = Column(Boolean)
    owner_id = Column(Integer,ForeignKey('users.id'))
    rating = Column(Integer)
    owner = relationship('User_db', back_populates= 'book_owners')
    reviews = relationship('Review_db', back_populates= 'books')

class Review_db(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    comment = Column(String)
    book_title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    users = relationship('User_db', back_populates='user_reviews')
    books =relationship('Book_db', back_populates='book_reviews')

def save_users(session, users):
    session.add_all([users])
    session.commit()

def save_books(session, book):
    session.add_all([book])
    session.commit()

def save_reviews(session, review):
    session.add_all([review])
    session.commit()

def delete_account(session, user):
    session.delete(session.query(User).filter(User.id == user.id).one())

def delete_review(session, review):
    session.delete(session.query(Review).filter(Review.id == review.id).one())

def edit_review(session, review, score, comment):
    session.query(Review.filter(Review.id == review.id).update({'score': score, 'comment': comment}))

def get_all_users(session):
    return[user.username for user in session.query(User).all()]

def get_all_books(session):
    return [book.title for book in session.query(Book).all()]
def get_all_reviews(session):
    return [review for review in session.query(Review).all()]

def find_by_title(session, title):
    return [book.title for book in session.query(Book).filter(Book.title.lower() == title.lower()).all()]

def find_by_author(session, author):
    return[book.title for book in session.query(Book).filter(Book.author.lower() == author.lower()).all()]

def find_by_genre(session, genre):
  return [book.title for book in session.query(Book).filter(Book.genre.lower() == genre.lower()).all()]

def find_by_owner(session, owner):
    return [book.title for book in session.query(Book).filter(Book.owner == owner).all()]

def find_by_rating(session, rating):
    return [book.title for book in session.query(Book).filter(Book.rating >= rating).all()]

def get_all_user_reviews(session, user):
    return [(review.title, review.score,review.comment) for review in session.query(Review,Book
                                                                    ).filter(Review.user_id == user.id
                                                                    ).filter(Review.book_id == Book.id
                                                                    ).all()]

def find_reviews_by_book(session, book):
    return[(review.score, review.comment) for review in session.query(Review).filter(Book.id == book.id).all()]

def checkout(session, user, book):
    session.query(Book).filter(Book.id == book.id).update({'owner': user.id, 'stocked':False})
    session.commit()

def restock(session,book):
     session.query(Book).filter(Book.id == book.id).update({'owner': None, 'stocked': True})



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
    user_books = relationship('Book_db', back_populates='owner')
    user_reviews = relationship('Review_db', back_populates= 'users')

class Book_db(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    stocked = Column(Boolean,default=True)
    owner_id = Column(Integer,ForeignKey('users.id'), default=0)
    rating = Column(Integer, default=0)
    owner = relationship('User_db', back_populates= 'user_books')
    book_reviews = relationship('Review_db', back_populates= 'books')

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

#SAVE FUNCTIONS
#saves and commits users to DB (tested)
def save_users(session, users):
    session.add_all([users])
    session.commit()
#saves and commits books to DB (tested)
def save_books(session, book):
    session.add_all([book])
    session.commit()
#saves and commits reviews to DB (tested)
def save_reviews(session, review):
    session.add_all([review])
    session.commit()

#GET FUNCTIONS
#gets the username and password of ALL users (tested)
def get_all_users(session):
    return[(user.username, user.password) for user in session.query(User_db).all()]
#gets a specific user, DOES NOT output a list (tested)
def find_user(session, name):
    user = session.query(User_db).filter(User_db.username == name).one()
    return(user.username, user.password, user.id)
#gets attributes of ALL books (tested)
def get_all_books(session):
    return [(book.id,book.title, book.author, book.genre, book.rating) for book in session.query(Book_db).all()]
#gets all books that are in stock (tested)
def get_books_in_stock(session):
    return[(book.id,book.title, book.author, book.genre, book.rating) for book in session.query(Book_db).filter(Book_db.stocked == True).all()]
#gets attributes of ALL reviews (tested)
def get_all_reviews(session):
    return [(review.book_title, review.score, review.comment) for review in session.query(Review_db).all()]
# gets all reviews based on the user's id (tested)
def get_all_user_reviews(session, user_id):
    return [(review.book_title, review.score,review.comment) for review in session.query(Review_db).filter(Review_db.user_id == user_id).all()]
#returns a book object based on its id  ⭐
def find_book_by_id(session, id):
    b = session.query(Book_db).filter(Book_db.id == id).one()
    return b
# tested
def find_by_title(session, title):
    return [(book.id,book.title, book.author, book.genre, book.rating) for book in session.query(Book_db).filter(Book_db.title == title).all()]
# tested
def find_by_author(session, author):
    return[(book.id,book.title, book.author, book.genre, book.rating) for book in session.query(Book_db).filter(Book_db.author == author).all()]
# tested
def find_by_genre(session, genre):
  return [(book.id,book.title, book.author, book.genre, book.rating) for book in session.query(Book_db).filter(Book_db.genre == genre).all()]
# tested
def find_by_owner(session, owner):
    return [(book.id,book.title, book.author, book.genre, book.rating) for book in session.query(Book_db).filter(Book_db.owner_id == owner).all()]
# tested
def find_by_rating(session, rating):
    return [(book.id,book.title, book.author, book.genre, book.rating) for book in session.query(Book_db).filter(Book_db.rating >= rating).all()]
#tested
def find_reviews_by_book(session, title):
    return[(review.book_title,review.score, review.comment) for review in session.query(Review_db).filter(Review_db.book_title == title.title()).all()]

#UPDATE FUNCTIONS
#UPDATES the review in db (tested )
def edit_review(session, review_id, score, comment):
    session.query(Review_db).filter(Review_db.id == review_id).update({'score': score, 'comment': comment})
    session.commit()
#UPDATES the owner_id to the user's id and makes it unstocked (tested)
def checkout(session, user_id, book_id):
    session.query(Book_db).filter(Book_db.id == book_id).update({'owner_id': user_id, 'stocked':False})
    session.commit()
#UPDATES the owner_id to None and changes the stocked value (tested)
def restock(session,book_id):
     session.query(Book_db).filter(Book_db.id == book_id).update({'owner_id': None, 'stocked': True})
     session.commit()

def update_score(session,book_id):
    scores =[r.score for r in session.query(Review_db).filter(Review_db.book_id == book_id).all()]
    scores = int(sum(scores)/len(scores))
    session.query(Book_db).filter(Book_db.id == book_id).update({'rating':scores})
    session.commit()
# DELETE FUNCTIONS
#DELETES account info from db (tested)
def delete_account(session, user_id):
    session.delete(session.query(User_db).filter(User_db.id == user_id).one())
    session.commit()
#DELETES review from db (tested)
def delete_review(session, review_id):
    session.delete(session.query(Review_db).filter(Review_db.id == review_id).one())
    session.commit()



#-------------- TESTING ZONE -------------------------
update_score(session,4)

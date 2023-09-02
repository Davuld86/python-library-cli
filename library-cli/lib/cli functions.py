from db.objects import *
from db.orm import *
class Current():
    def __init__(self, user=None, user_id= 0, book = None, book_id = 0, review= None, review_id=0):
        self.user = user
        self.user_id = user_id
        self.book = book
        self.book_id = book_id
        self.review = review
        self.review_id = review_id

def login():
    print('*** Login type "exit" to quit ***')
    username = input('Enter username: ')
    if username == 'exit':
        return 0
    password = input('Enter password: ')
    if password == 'exit':
        return 0
    if username not in User.users.keys():
        print('Username/Password incorrect')
    elif User.users[username][1] == password:
        print(f'Welcome {username}!')
        User.append_to_log(User.users[username][0])
        return 1
    else:
        print('Username/Password incorrect')
        return 0

def register():
    print('Please enter a username and password to create an account.')
    username = input("Enter Username: ")
    if username == ' ' or username == '':
        print('Please enter a valid username.')
        return 1
    elif username in User.users.keys():
        print('Username already taken.')
        return 1
    password = input('Enter Password: ')
    if password == ' ' or password=='':
        print('Please enter a valid password.')
        return 1
    else:
         username= User(username, password)
    print('Thank you for making an account!')

def pick_book(book):
    current.update({'book': book})

def view_reviews(user):
    print(get_all_user_reviews(user))

def delete_review(book,review):
    delete_review(review)
    book.scores.remove(review.score)
    book.comment.remove(review.comment)

def edit_user_review(review, score, comment):
    edit_review(review, score, comment)

def view_owned_books(user):
    print(find_by_owner(user))

def return_book(user, book):
    user.return_book(book)
    book.restock()
    restock(book)

def write_review():
    score = int(input('Give this book a score from 0-5.'))
    if abs(score) > 5:
        print('The score must be between 0-5.')
        return 0
    comment = input('Give this book a brief review.')
    if comment == '' or comment == ' ':
        print('Please write a few words about the book.')
        return 0
    else:
        r = Review(score,comment,current['user'], current['book'])







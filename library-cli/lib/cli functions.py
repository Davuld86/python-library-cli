from db.objects import *
from db.orm import *
engine = create_engine('sqlite:///library.sql', echo= True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# this helps to easily keep track of data
class Current():
    def __init__(self, user=None, user_id= 0, book = None, book_id = 0, review= None, review_id=0):
        self.user = user
        self.user_id = user_id
        self.book = book
        self.book_id = book_id
        self.review = review
        self.review_id = review_id
c = Current()

#need a fctn that grabs all the previouis data
def initialization():
    print(get_all_books(session))

# checks the username & password against the dictionary of users to login
def login():
    print('*** Login type "exit" to quit ***')
    username = input('Enter username: ')
    if username == 'exit':
        return 0
    password = input('Enter password: ')
    if password == 'exit':
        return 0
    info = find_user(session, username)
    if info[0]==username and info[1] == password:
        print(f'Welcome back, {username}!')
        User.append_to_log(info[2])
        c.user_id = info[2]
        return 1
    else:
        print('Username/Password incorrect')
        return 0

# CREATES a new user class and saves it to SQL
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
         username= User_db(username=username, password=password)
         save_users(session,username)
    print('Thank you for making an account!')

#changes the current book to this one
def pick_book(book):
    c.book = book
    c.book_id = book.id

#changes the current review to this one
def pick_review(review):
    c.review = review
    c.review_id = review.id
#GETs all reviews that the user created
def view_reviews(user):
    print(get_all_user_reviews(user))

#DELETES a review
def delete_review(book,review):
    delete_review(review)
    book.scores.remove(review.score)
    book.comment.remove(review.comment)

#EDITS a review
def edit_user_review(review, score, comment):
    edit_review(review, score, comment)

#GETS all books owned by the user
def view_owned_books(user):
    print(find_by_owner(user))

#calls all functions that 'returns' the book
def return_book(user, book):
    user.return_book(book)
    book.restock()
    restock(book)

#CREATES a book object
def donate_book():
    title = input("What's the book's title?")
    if title == '' or ' ':
        print('Please input a valid title.')
        return 0
    else:
        title.title()
    author = input('Who was the author?')
    if author == '' or ' ':
        print('Please input a valid name.')
        return 0
    else:
        author.title()
    genre = input('Who was the author?')
    if genre == '' or ' ':
        print('Please input a valid genre.')
        return 0
    else:
        n_book = Book(title, author, genre)
        save_books(n_book)
        return 1

#CREATES a review object
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
        r = Review(score,comment,c.user_id, c.book)
        return 1

#displays all books that comes from the SQL database
# CREATE A WAY TO CHOOSE THE BOOK FROM THE LIST
def display_book_list(books):
    for book in books:
        print(f'{book.id}. {book.title} {"★"*book.rating}\n')
        i+=1
    i = input('Which book would you like to choose?')
    #STUFF HERE

#presents all the data from the book
def display_book_data(book):
    print( f'Title: {book.title}\n'
           f'Author: {book.author}\n'
           f'Genre: {book.author}\n'
           f'Rating: {book.author}\n'
          )

#displays all reviews from database
def display_review_list(reviews):
    for review in reviews:
        print(f'{review.id}. {review.book_title}')
    i = input('Which book would you like to choose?')

#display review attributes
def display_review_data(review):
    print(
        f'Book Title:{review.book_title}\n'
        f'Score:{review.score}\n'
        f'Comment:{review.comment}\n'
    )

#Menu to search through all the books
def search_books():
    i = input('What would you like to search the books by?\n'
              '1. View All\n'
              '2. Search by Title\n'
              '3. Search by Author\n'
              '4. Search by Genre\n'
              '5. Search by Rating\n'
              '6. Back\n'
              )
    match i:
        case '1':
            print(get_all_books())
        case '2':
            author = input('Please enter an author.')
            if find_by_author(author) is not None:
                print(find_by_author(author))
            else:
                print('No books whith that author found')
        case '3':
            title = input('Please enter a title.')
            if find_by_title(title) is not None:
                print(find_by_title(title))
            else:
                print('No books whith that title found.')
        case '4':
            genre = input('Please input a genre')
            if find_by_genre(genre) is not None:
                 print(find_by_genre(genre))
            else:
                print('No books in that genre found.')
        case '5':
            rating = input('Please input the minimum rating')
            if find_by_rating(int(rating)) is not None:
                print(find_by_rating(int(rating)))
            else:
                print('No books whith that rating found')
        case '6':
            return 1

# Menu to search reviews
def search_reviews():
    i = input('What would you like to search the reviews by?\n'
              '1. View all reviews\n'
              '2. Search by book title\n'
              '3. Go back \n'
              )
    match i:
        case '1':
            display_review_list(get_all_reviews())
        case '2':
            title = input('Please input the title of the book.')
            if find_reviews_by_book(title) is not None:
                print(find_reviews_by_book(title))
            else:
                print('No review found!')
        case '3':
            return 1


#-----------------------TESTING ZONE DO NOT CROSS-----------------------------------
login()

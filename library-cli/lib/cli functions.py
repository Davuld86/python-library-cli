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
        self.last_list = None
c = Current()

#start menu
def welcome():
    pass

# checks the username & password against the dictionary of users to login (tested)
def login():
    print('*** Login type "exit" to quit ***')
    username = input('Enter username:  ')
    if username == 'exit':
        return 0
    password = input('Enter password:  ')
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

# CREATES a new user class and saves it to SQL (tested)
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

# main menu once logged in
def main_menu():
    print('What would you like to do?  \n')
    n = input(
            f'1. View book catalog\n'
            f'2. View reviews\n'
            f'3. View your checked out books\n'
            f'4. View your reviews\n'
            f'5. Delete your account\n'
            f'6. Log out\n'
    )
    match n:
        case '1':
            search_books()
        case '2':
            search_reviews()
        case '3':
            display_book_list(find_by_owner(session, c.user_id))
        case '4':
            display_review_list(get_all_user_reviews(session, c.user_id))
        case '5':
            delete_account()
        case '6':
            print('Please come again!')
            return 1

#Menu to search through all the books
def search_books():
    i = input('What would you like to search the books by?  \n'
              '1. View All\n'
              '2. Search by Title\n'
              '3. Search by Author\n'
              '4. Search by Genre\n'
              '5. Search by Rating\n'
              '6. Back\n'
              )
    match i:
        case '1':
            c.last_list=(get_books_in_stock(session))
            display_book_list(get_books_in_stock(session))

        case '2':
            title = input('Please enter a title.  ')
            title = title.title()
            title_l = find_by_title(session,title)
            if title_l is not []:
                c.last_list=title_l
                display_book_list(title_l)
            else:
                print('No books whith that title found.')

        case '3':
            author = input('Please enter an author.  ')
            if find_by_author(session,author.title()) is not []:
                c.last_list=find_by_author(session,author)
                display_book_list(find_by_author(session,author))

            else:
                ('No books whith that author found')
        case '4':
            genre = input('Please input a genre')
            genre_l = find_by_genre(session,genre)
            if genre_l is not []:
                c.last_list=genre_l
                display_book_list(genre_l)

            else:
                print('No books in that genre found.')
        case '5':
            rating = input('Please input the minimum rating')
            if find_by_rating(session,int(rating)) is not []:
                c.last_list=find_by_rating(session,int(rating))
                display_book_list(find_by_rating(session,int(rating)))

            else:
                print('No books whith that rating found')
        case '6':
            main_menu()

# Menu to search reviews
def search_reviews():
    i = input('What would you like to search the reviews by?  \n'
              '1. View all reviews\n'
              '2. Search by book title\n'
              '3. Go back \n'
              )
    match i:
        case '1':
            display_review_list(get_all_reviews(session))
        case '2':
            title = input('Please input the title of the book.  ')
            if find_reviews_by_book(title) is not None:
                print(find_reviews_by_book(title))
            else:
                print('No review found!')
        case '3':
            main_menu()

#displays all books that comes from the SQL database
def display_book_list(books):
    for book in books:
        print(f'{book[0]}. {book[1]}, Rating: {"Unrated" if book[4] == None else"★"* book[4]}{""if book[4]==None else"☆"*(5-book[4])} \n')
    i = input('Please input the number of the book you would like to choose. Press ENTER to go back.')
    if i== '' or i== ' ' or i=='0':
        main_menu()
    else:
        display_book_data(find_book_by_id(session,i))

#presents all the data from book
def display_book_data(book):
    print( f'Title: {book.title}\n'
           f'Author: {book.author}\n'
           f'Genre: {book.genre}\n'
           f'Rating: {"Unrated" if book.rating == None else "★"*book.rating}\n'
          )
    if book.stocked ==False:
        p = input('What would you like to do with this book?  \n'
                f'1. Return book\n'
                f'2. Write review\n'
                f'3. Go back\n'
                )
        match p:
            case '1':
                print(f'{book.title} was returned, thank you. ')
                restock(session, book)
            case '2':
                write_review(book)
            case '3':
                display_book_list(c.last_list)
    else:
        i = input('What would you like to do with this book?   \n'
                f'1. Check out book\n'
                f'2. Write review\n'
                f'3. Go back\n'
                )
        match i:
            case '1':
                print(f'{book.title} has been checked out. ')
                checkout(session,c.user_id,book.id)
                return 1
            case '2':
                write_review(book)
                return 1
            case '3':
                display_book_list(c.last_list)
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

def check_out_book(user_id, book_id):
    checkout(session, user_id, book_id)

#CREATES a book object ⭐
def donate_book():
    title = input("What's the book's title?")
    if title == '' or title== ' ':
        print('Please input a valid title.')
        return 0
    else:
        title.title()
    author = input('Who was the author?')
    if author == '' or author== ' ':
        print('Please input a valid name.')
        return 0
    else:
        author.title()
    genre = input('What is the books genre?')
    if genre == '' or genre==' ':
        print('Please input a valid genre.')
        return 0
    else:
        n_book = Book_db(title=title, author=author, genre=genre)
        save_books(session, n_book)
        return 1

#CREATES a review object
def write_review(book):
    score = int(input('Give this book a score from 0-5.  '))
    if abs(score) > 5:
        print('The score must be between 0-5.')
        return 0
    comment = str(input('Give this book a brief review.  '))
    if comment == '' or comment == ' ':
        print('Please write a few words about the book.  ')
        return 0
    else:
        comment=str(comment)
        r = Review_db(score=score,comment=comment,user_id=c.user_id,book_id=book.id, book_title= book.title)
        save_reviews(session, r)
        update_score(session,book.id)
        return 1


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


#-----------------------TESTING ZONE DO NOT CROSS-----------------------------------
print(c.user_id)
main_menu()

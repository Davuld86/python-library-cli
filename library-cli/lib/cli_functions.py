from db.objects import *
from db.orm import *

engine = create_engine('sqlite:///library.sql', echo= False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# this helps to easily keep track of data
class Current():
    def __init__(self, user='ben', user_id= 2):
        self.username=user
        self.user_id = user_id
        self.last_list = None
c = Current()

#start menu⭐
def welcome():
    print('___________________: Welcome to the InkWell Library :__________________\n')

def start():
    while True:
        i = input('What would you like to do? \n'
                '1. Login  \n'
                '2. Register  \n'
                '3. Donate book \n'
                '4. Exit  \n'
                )
        match i:
            case '1':
                if login() == 1:
                    if main_menu()==1:
                        start()
                else:
                    start()
            case '2':
                register()
                start()
            case '3':
                donate_book()
                start()
            case '4':
                print('Goodbye')
                exit()
            case _:
                search_error('invalid input', start)

# checks the username & password against the dictionary of users to login ⭐
def login():
    print('__________Login____________\n Type "exit" to quit')
    username = input('Enter username:  ')
    if username == 'exit':
        return 0
    password = input('Enter password:  ')
    if password == 'exit':
        return 0
    info = find_user_by_username(session, username)
    if info is None:
        print('Username/Password incorrect')
        return 0
    elif info[0]==username and info[1] == password:
        print(f'Welcome back, {username}!')
        User.append_to_log(info[2])
        c.user_id = info[2]
        return 1
    print('Username/Password incorrect')
    return 0

# CREATES a new user class and saves it to SQL (tested)⭐
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

# main menu once logged in⭐
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
            #user book list
            ubl = find_by_owner(session, c.user_id)
            if ubl != []:
                c.last_list= ubl
                display_book_list(ubl)
            else:
                search_error('No books checked out', main_menu)
        case '4':
            #url > user review list
            url = get_all_user_reviews(session, c.user_id)
            if url !=[]:
                c.last_list = url
                display_review_list(url)
            else:
                search_error('You do not have any reviews',main_menu)
        case '5':
            handle_delete()

        case '6':
            print('Please come again!')
            start()

        case _:
            search_error('invalid input', main_menu)

#Menu to search through all the books⭐
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
            title = input('Please enter a title.  \n')
            title = str(title.title())
            title_l = find_by_title(session,title)
            if title_l !=[]:
                c.last_list=title_l
                display_book_list(title_l)
            else:
                search_error('No books with that title found!',search_books)

        case '3':
            author = input('Please enter an author.  \n')
            author_l =find_by_author(session,author.title())
            if author_l!=[]:
                c.last_list=author_l
                display_book_list(author_l)
            else:
                search_error('No books with that author found!',search_books)
        case '4':
            genre = input('Please input a genre\n')
            genre_l = find_by_genre(session,genre)
            if genre_l != []:
                c.last_list=genre_l
                display_book_list(genre_l)
            else:
                search_error('No books in that genre found!',search_books)
        case '5':
            rating = input('Please input the minimum rating')
            rlst = find_by_rating(session,int(rating))
            if rlst != []:
                c.last_list=rlst
                display_book_list(rlst)
            else:
                search_error('No books with that rating found!',search_books)
        case '6':
            main_menu()
        case _:
            search_error('Please input a valid number', search_books)


# Menu to search reviews⭐
def search_reviews():
    i = input('What would you like to search the reviews by?  \n'
              '1. View all reviews\n'
              '2. Search by book title\n'
              '3. Search by review score\n'
              '4. Go back \n'
              )
    match i:
        case '1':
            c.last_list = get_all_reviews(session)
            display_review_list(get_all_reviews(session))
        case '2':
            title = input('Please input the title of the book.  ')
            title_l = find_reviews_by_book(session,title.title())
            if title_l != []:
                c.last_list = title_l
                display_review_list(title_l)
            else:
                search_error('No reviews with that book title found!',search_reviews)
        case '3':
            score = input('Please enter the score:  ')
            score_l = (find_reviews_by_score(session, score))
            if score_l != []:
                c.last_list = score_l
                display_review_list(score_l)
            else:
                search_error('No reviews with that score found!', search_reviews)
        case '4':
            main_menu()
        case _:
            search_error('Please input a valid number', search_reviews)

#displays all books that comes from the SQL database⭐
def display_book_list(books):
    for book in books:
        print(f'{book[0]}. {book[1]}, Rating: {"Unrated" if book[4] == None else"★"* book[4]}{""if book[4]==None else"☆"*(5-book[4])} \n')
    i = input('Please input the number of the book you would like to choose. Press ENTER to go back.\n')
    if i=='':
         main_menu()
    elif find_book_by_id(session,i)==None:
        print('Please input a valid number\n')
        i=input('Press any key to go back\n')
        display_book_list(c.last_list)
    else:
        display_book_data(find_book_by_id(session,i))

#presents all the data from book ⭐
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
                f'3. View reviews of this book\n'
                f'4. Go back\n'
                )
        match p:
            case '1':
                print(f'{book.title} was returned, thank you. ')
                restock(session, book.id)
                main_menu()
            case '2':
                if usercheck(c.user_id,book.id)==1:
                    write_review(book)
                    main_menu()
                else:
                    display_book_list(c.last_list)
            case '3':
                l = find_reviews_by_book(session, book.title)
                c.last_list=l
                display_review_list(l)
            case '4':
                display_book_list(c.last_list)
            case _:
                print('Please input a valid number\n')
                i=input('Press any key to go back\n')
                if i=='' or ' ':
                    display_book_data(book)

    else:
        i = input('What would you like to do with this book?   \n'
                f'1. Check out book\n'
                f'2. Write review\n'
                f'3. View reviews of this book\n'
                f'4. Go back\n'
                )
        match i:
            case '1':
                print(f'{book.title} has been checked out. ')
                checkout(session,c.user_id,book.id)
                press_enter()
                main_menu()
            case '2':
                if usercheck(c.user_id,book.id)==1:
                    write_review(book)
                    main_menu()
                else:
                    display_book_list(c.last_list)
                main_menu()
            case '3':
                l = find_reviews_by_book(session, book.title)
                c.last_list =l
                display_review_list(l)
            case '4':
                display_book_list(c.last_list)
            case _:
                print('Please input a valid number')
                i=input('Press any key to go back\n')
                if i=='' or ' ':
                    display_book_data(book)

#handles no books/reviews found ⭐
def search_error(message,func):
    print(f'{message}\n')
    i=input('Press any key to go back\n')
    if i=='' or ' ':
        func()
    else:
        print("How'd you get here?")

def usercheck(uid, bid):
    x= session.query(Review_db).filter(Review_db.book_id==bid).first()
    if x == None:
        return 1
    elif x.user_id == uid:
        print('You have already written a review for this book.')
        i= input('Press ENTER to go back. \n')
        return 0
    else:
        return 1
#displays all reviews given a list ⭐
def display_review_list(reviews):
    for review in reviews:
        x= find_user_by_id(session,review[4])
        u_name = x.username if x is not None else 'Deleted User'
        print(f'{review[0]}. Book: {review[1]}, Score:{"★"* review[2]}{"☆"*(5-review[2])}, Created by: {u_name}')
    i = input('Please input the number of the book you would like to choose. Press ENTER to go back.\n')
    if i== '' or i== ' ' or i=='0':
        main_menu()
    elif find_reviews_by_id(session,i)==None:
        print('Please input a valid number')
        i=input('Press any key to go back\n')
        if i=='' or ' ':
            display_review_list(c.last_list)
    else:
        display_review_data(find_reviews_by_id(session,i))

#display review attributes of review object⭐
def display_review_data(review):
    x= find_user_by_id(session,review.user_id)
    u_name = x.username if x is not None else 'Deleted User'
    print(
        f'Book: {review.book_title}\n'
        f'Score: {"★"* review.score}{"☆"*(5-review.score)}\n'
        f'Review: {review.comment}\n'
        f'Created by: {u_name}\n'
    )
    if review.user_id ==c.user_id:
        print('What would you like to do with this review?\n')
        i = input(
            '1. Edit reivew\n'
            '2. Delete review\n'
            '3. Go back\n'
            )
        match i:
            case '1':
                edit_user_review(review.id, review.book_id)
            case '2':
                delete_user_review(review.id, review.book_id)
            case '3':
                display_review_list(c.last_list)
            case _:
                print('Please input a valid number')
                i=input('Press any key to go back\n')
                if i=='' or ' ':
                    display_review_data(review)
    else:
        i = input('Press ENTER to go back\n')
        if i == '' or  ' ':
            display_review_list(c.last_list)

#DELETE review menu ⭐
def delete_user_review(rid,rbid):
    i = input('Delete this review? (y/n)\n')
    if i.lower() == 'y' or i.lower()== 'yes':
        delete_review(session,rid)
        update_score(session,rbid)
        print('Review deleted')
        i=input('Press ENTER to continue')
    main_menu()
#DELETES accout
def handle_delete():
    ubl = find_by_owner(session, c.user_id)
    if ubl != []:
        print('You have these books checked out:\n')
        for book in ubl:
            print(f'{book[0]}. {book[1]}\n')
        search_error('You cannot delete your account whiile you still have books checked out.\n', main_menu)
    i = input('Delete your account? (y/n)\n')
    if i == 'y' or i=='yes':
        p_check= input('Please enter password:\n')
        if p_check == find_user_by_id(session,c.user_id).password:
            print('Account deleted, sorry to see you go.')
            delete_account(session, c.user_id)
            start()
        else:
            search_error('Incorrect passowrd', main_menu)

#EDIT review menu ⭐
def edit_user_review(rid,rbid):
    i= input(' Edit this review? (y/n)\n')
    if i.lower()== 'y' or i.lower()== 'yes':
        score = input('Please input the new score:  \n')
        comment= input('Please input the new comment  \n')
        edit_review(session,rid,score,comment)
        update_score(session,rbid)
    main_menu()

#handles cheking out a book ⭐
def check_out_book(user_id, book_id):
    checkout(session, user_id, book_id)

#CREATES a book object ⭐
def donate_book():
    title = input("What's the book's title?\n ")
    if title == '' or title== ' ':
        print('Please input a valid title.\n ')
        return 0
    else:
        title.title()
    author = input('Who was the author?\n ')
    if author == '' or author== ' ':
        print('Please input a valid name.')
        return 0
    else:
        author.title()
    genre = input('What is the books genre?\n ')
    if genre == '' or genre==' ':
        print('Please input a valid genre.')
        return 0
    else:
        n_book = Book_db(title=title, author=author, genre=genre)
        save_books(session, n_book)
        print(f'{title} was donated to the Inkwell Library, thank you!')
        press_enter()
        return 1

#CREATES a review object⭐
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
        print('Review submitted!')
        press_enter()
        return 1
#does nothing, more user interaction.⭐
def press_enter():
    i=input('Press ENTER to continue.')
    if i== '' or ' ':
        pass
#-----------------------TESTING ZONE DO NOT CROSS-----------------------------------


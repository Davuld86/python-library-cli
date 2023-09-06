from db.orm import *
#users
users = [
    User_db(id=1, username="coding_ninja", password="secret123"),
    User_db(id=2, username="bookworm_jane", password="mypassword"),
    User_db(id=3, username="lit_lover42", password="ilovebooks"),
    User_db(id=4, username="python_master", password="python123"),
    User_db(id=5, username="wanderlust_trekker", password="wanderlust"),
    User_db(id=6, username="music_melody", password="musiclover"),
    User_db(id=7, username="cinema_aficionado", password="cinemafan"),
    User_db(id=8, username="sports_enthusiast", password="go_team"),
    User_db(id=9, username="chef_cuisine", password="delicious"),
    User_db(id=10, username="art_appreciator", password="creative")
]

#books
books = [
    Book_db(id=1, title="To Kill a Mockingbird", author="Harper Lee", genre="Fiction"),
    Book_db(id=2, title="1984", author="George Orwell", genre="Dystopian"),
    Book_db(id=3, title="Pride and Prejudice", author="Jane Austen", genre="Classic"),
    Book_db(id=4, title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction"),
    Book_db(id=5, title="The Hobbit", author="J.R.R. Tolkien", genre="Fantasy"),
    Book_db(id=6, title="The Catcher in the Rye", author="J.D. Salinger", genre="Fiction"),
    Book_db(id=7, title="Brave New World", author="Aldous Huxley", genre="Dystopian"),
    Book_db(id=8, title="To the Lighthouse", author="Virginia Woolf", genre="Modernist"),
    Book_db(id=9, title="Moby-Dick", author="Herman Melville", genre="Adventure"),
    Book_db(id=10, title="War and Peace", author="Leo Tolstoy", genre="Historical Fiction"),
    Book_db(id=11, title="The Odyssey", author="Homer", genre="Epic Poetry"),
    Book_db(id=12, title="The Shining", author="Stephen King", genre="Horror"),
    Book_db(id=13, title="The Road", author="Cormac McCarthy", genre="Post-Apocalyptic"),
    Book_db(id=14, title="The Alchemist", author="Paulo Coelho", genre="Adventure")
]

#reviews
reviews = [
    Review_db(score=4, comment="Great book!", user_id=1, book_id=1, book_title="To Kill a Mockingbird"),
    Review_db(score=5, comment="One of my favorites!", user_id=2, book_id=2, book_title="1984"),
    Review_db(score=3, comment="Enjoyed it, but not my top pick.", user_id=3, book_id=3, book_title="Pride and Prejudice"),
    Review_db(score=2, comment="Could have been better.", user_id=4, book_id=4, book_title="The Great Gatsby"),
    Review_db(score=5, comment="Absolutely fantastic!", user_id=5, book_id=5, book_title="The Hobbit"),
    Review_db(score=4, comment="A classic for a reason.", user_id=6, book_id=6, book_title="The Catcher in the Rye"),
    Review_db(score=2, comment="Not my cup of tea.", user_id=7, book_id=7, book_title="Brave New World"),
    Review_db(score=3, comment="An interesting read.", user_id=8, book_id=8, book_title="To the Lighthouse"),
    Review_db(score=4, comment="An epic adventure!", user_id=9, book_id=9, book_title="Moby-Dick"),
    Review_db(score=5, comment="A masterpiece!", user_id=10, book_id=10, book_title="War and Peace"),
    Review_db(score=4, comment="A timeless epic.", user_id=1, book_id=11, book_title="The Odyssey"),
    Review_db(score=2, comment="A bit disappointing.", user_id=2, book_id=12, book_title="The Shining"),
    Review_db(score=3, comment="A haunting post-apocalyptic tale.", user_id=3, book_id=13, book_title="The Road"),
    Review_db(score=5, comment="Life-changing journey.", user_id=4, book_id=14, book_title="The Alchemist")
]

def plant_seed():
    for user in users:
        save_users(session,user)
    for book in books:
        save_books(session,book)
    for review in reviews:
        save_reviews(session,review)
        update_score(session,review.book_id)

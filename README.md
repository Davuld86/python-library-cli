# Library CLI

The Library CLI is a Python command-line tool that allows users to browse, check out, and review books from a library collection. This tool provides a simple and efficient way to manage library resources and keep track of borrowed books.

## Features
- Browse the library catalog.
- Create an accout.
- Search for books by title, author, or genre.
- Add, edit and delete book reviews.
- User-friendly command-line interface via menu traversal.

## Installation

1. Clone this repository:


2. Navigate to the project directory:

   ```bash
   python-library-cli/library-cli/lib
   ```

3. Install the required dependencies using pipenv
   ```bash
   pipenv install
   pipenv shell
   ```
4. Run the CLI:

   ```bash
   python library_cli.py
   ```
## Things you can do
- Login / Register
- Donate book: creates a new book object
- Search books: searches the books by different attributes
- Search reviews: searches the books by different attributes
- Write review: creates a reveiw

### Example Usage
#### Creating a new account and checking out a book0
- On startup:

   ```bash
   What would you like to do?
  1. Login
  2. Register
  3. Donate book
  4. Exit
   ```

- Enteriing '2' to register prompts to enter a username and password:

   ```bash
   Please enter a username and password to create an account.
   Enter Username: demo_name
   Enter Password: some_password
   ```

- Returns to the start menu to login:

   ```bash
   __________Login____________
   Type "exit" to quit
   Enter username:  demo_name
   Enter password:  some_password
   ```

- Main menu after logging in:

   ```bash
   Welcome back, demo_name!
   What would you like to do?

  1. View book catalog
  2. View reviews
  3. View your checked out books
  4. View your reviews
  5. Delete your account
  6. Log out
   ```

- Entering '1' leads us to the book search menu:

   ```bash
   What would you like to search the books by?
  1. View All
  2. Search by Title
  3. Search by Author
  4. Search by Genre
  5. Search by Rating
  6. Back
   ```

- Entering '1' to view all books in stock:
   ```bash
   1. Redwall, Rating: ★★★☆☆

   2. The Iliad, Rating: ★★★★★

   4. Fight Club, Rating: ★★★★☆

   5. The Legend of Luke , Rating: ★★★★☆

   6. The Giver, Rating: ★★★★★

   Please input the number of the book you would like to choose. Press ENTER to go back.
   ```

- Let's view The Iliad (entering '2')
   ```bash
   Title: The Iliad
   Author: Homer
   Genre: Epic
   Rating: ★★★★★

   What would you like to do with this book?
   1. Check out book
   2. Write review
   3. Go back
   ```
- Entering '1' here will check out the book and move us back to the main menu
   ```bash
   The Iliad has been checked out.
   Press ENTER to continue.
   What would you like to do?

   1. View book catalog
   2. View reviews
   3. View your checked out books
   4. View your reviews
   5. Delete your account
   6. Log out
   ```
## Dependencies

- [SQLite](https://www.sqlite.org/) for database management.
- [SQLalchemy](https://www.sqlalchemy.org/) for database management.

## Contributing

If you'd like to add onto this project, feel free to do so.

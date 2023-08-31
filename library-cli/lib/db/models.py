class User:
    log =[]
    users = {}
    id = 0

    def __init__(self, username, password):
        self.id = User.add_id()
        self.books = []
        self.username = username
        self.password = password
        User.add_new_user(username,password)
        User.append_to_log()

    def checkout(self,book):
        self.books.append(book.title)
        book.checkout(self.id)

    def return_book(self, book):
        self.books.remove(book.title)
        book.restock()

    @classmethod
    def add_new_user(self,username, password):
        self.users.update({username: password})
    @classmethod
    def append_to_log(self):
        self.log.append(self.username)
    @classmethod
    def add_id(self):
         self.id += 1
         return self.id

    # username methods
    def _get_username(self):
        return self._username

    def _set_username(self, input):
        if input in User.users.keys():
            raise AttributeError(f'Username: "{input}" is already taken!')
        elif type(input) != str:
            raise ValueError('Please input a valid username.')
        else:
            self._username = input
    # password methods
    def _get_password(self):
        print('Passwords are secret!')

    def _set_password(self, p):
        if type(p) != str:
            raise ValueError('Please input a valid password!')
        else:
            self._password = p

    #username property
    username = property(
        fget = _get_username,
        fset = _set_username,
        doc= 'The username property.'
    )

    #password property
    password = property(
        fget = _get_password,
        fset = _set_password,
        doc = 'The password property'
    )

class Book:
    id = -1
    def __init__(self, title, author, genre):
        self.id = Book.add_id()
        self.title = title
        self.author = author
        self.genre = genre
        self.stocked = True
        self.scores = []
        self.reviews = []
        self.rating = self.get_rating()



    def get_rating(self):
        if self.scores==[]:
            self.rating = 0
        else:
            self.rating = round(sum(self.scores)/len(self.scores), 1)
        return self.rating
    def checkout(self,id):
        self.stocked = False
        self.owner = id

    def restock(self):
        self.stocked = True
        self.owner = 0

    def add_score(self,review):
        self.scores.append(review.score)
        self.reviews.append(review.comment)
        self.get_rating()

    @classmethod
    def add_id(self):
        self.id += 1
        return self.id

    #owner methods
    def _get_owner(self):
        return self._owner
    def _set_owner(self, o):
        self._owner = o


    #owner property
    owner = property(
        fget = _get_owner,
        fset = _set_owner,
        doc= 'The owner property'
    )

class Review:
    id = -1
    def __init__(self, score, comment, user, book):
        self.id  = Review.add_id()
        self.score = score
        self.comment = comment
        self.user = user.id
        self.book = book.id
        book.add_score(self)

    @classmethod
    def add_id(self):
        self.id += 1
        return self.id

    #score methods
    def _get_score(self):
        return self._score
    def _set_score(self, s):
        if type(s) != (int) or s > 10:
            raise ValueError('Please enter a number from 0  - 10')
        else:
             self._score = s
    #comment methods
    def _get_comment(self):
        return self._comment
    def _set_comment(self, c):
        if type(c) != str or c =='' or c == ' ':
            raise AttributeError('Please enter a comment.')
        else:
            self._comment = c

    #score property
    score = property(
        fget= _get_score,
        fset= _set_score
    )
    #comment property
    comment = property(
        fget= _get_comment,
        fset= _set_comment
    )

#Note: to reference the book's owner's name: list(User.users.keys())[BOOKHERE.owner -1]

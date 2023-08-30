from statistics import mean
class User:
    id = 1
    log =[]
    users = {}

    def __init__(self, username, password):
        self.books = []
        self._username = username
        self._password = password
        User.add_new_user(username,password)
        User.append_to_log()

    def checkout(self,book):
        self.books.append(book.title)
        book.check_out(self.id)

    def return_book(self, book):
        self.books.remove(book.title)
        book.restock()

    @classmethod
    def add_new_user(self,username, password):
        self.users.update({username: password})
    @classmethod
    def append_to_log(self):
        self.log.append(self.username)

    # id property methods
    def _get_id(self):
        return self._id

    def _set_id(self):
        if self._id == None:
            self._id = 0
        else:
            self._id += 1
        return self._id

    # username methods
    def _get_username(self):
        return self._username

    def _set_username(self, input):
        if type(input) != str:
            raise ValueError('Please input a valid username.')
        elif self._username in self.users.keys:
            print(f'Username already taken!')
        else:
            self._username = input
    # password methods
    def _get_password(self):
        raise AttributeError('Passwords are secret!')

    def _set_password(self, p):
        if type(p) != str:
            raise ValueError('Please input a valid password!')
        else:
            self._password = p

    #id property
    id = property(
        fget = _get_id,
        fset = _set_id,
        doc = 'The id property'
        )

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

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.stocked = True
        self._scores = []

    #id methods
    def _get_id(self):
        return self._id
    def _set_id(self):
        if self._id == None:
            self._id = 0
        else:
            self._id += 1
        return self._id

    #owner methods
    def _get_owner(self):
        return self._owner
    def _set_owner(self, o):
        self._owner = o

    #scores methods
    def _get_scores(self):
        return self._scores
    def _set_scores(self, sc):
        self._scores.append(sc)

     #reviews methods
    def _get_reviews(self):
        return self._reviews
    def _set_reviews(self,rev):
        if rev == '' or rev == ' ':
            raise AttributeError('Please input a review.')
        else:
            self._reviews.append(rev)

    #rating methods
    def _get_rating(self):
        return self._rating
    def _set_rating(self):
        self._rating =int(mean(self.scores))


    #id property
    id = property(
        fget = _get_id,
        fset = _set_id,
        doc = 'The id property'
        )

    #owner property
    owner = property(
        fget = _get_owner,
        fset = _set_owner,
        doc= 'The owner property'
    )

    #scores property
    scores = property(
        fget= _get_scores,
        fset= _set_scores,
        doc= "The scores property"
    )

    #reviews property
    reviews = property(
        fget= _get_reviews,
        fset = _set_reviews,
        doc = 'The reviews property'
    )

    #rating property
    rating = property(
        fget= _get_rating,
        fset= _set_rating,
        doc= 'The rating property'
    )






class User:
    id = 1
    log =[]
    users = {}

    def __init__(self, username, password):
        self.books = []
        self._username = username
        self._password = password
        User.add_new_user(username,password)

    def checkout(self,book):
        self.books.append(book.title)
        book.check_out(self.id)

    def return_book(self, book):
        self.books.remove(book.title)
        book.restock()

    # id property methods
    def _get_id(self):
        return self._id
    def _set_id(self):
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






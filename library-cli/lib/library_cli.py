from cli_functions import *

class Base(DeclarativeBase):
    pass
engine = create_engine('sqlite:///library.sql', echo= True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def start():
    while True:
        i = input('What would you like to do? \n'
                '1. Login  '
                '2. Register  '
                '3. Donate book  '
                '4. Exit  '
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
                break

welcome()
start()

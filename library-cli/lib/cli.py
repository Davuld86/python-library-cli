from cli_functions import *

engine = create_engine('sqlite:///library.sql', echo= True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

welcome()
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
                    main_menu()
                else:
                    start()
            case '2':
                register()
                start()
            case '3':
                donate_book()
                start()
            case '4':
                break

start()

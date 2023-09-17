from cli_functions import *
from seed import plant_seed
class Base(DeclarativeBase):
    pass
engine = create_engine('sqlite:///library.sql', echo= False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

welcome()
start()

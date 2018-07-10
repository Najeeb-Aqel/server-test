from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

# connecting to the category database
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

category1 = Category(name="Math")

session.add(category1)
session.commit()

category2 = Category(name="History")

session.add(category2)
session.commit()

category3 = Category(name="Science")

session.add(category3)
session.commit()

category4 = Category(name="Health")

session.add(category4)
session.commit()

category5 = Category(name="Travel")

session.add(category5)
session.commit()

category6 = Category(name="Self Help")

session.add(category6)
session.commit()

category7 = Category(name="Autobiographies")

session.add(category7)
session.commit()

category8 = Category(name="Poetry")

session.add(category8)
session.commit()

category9 = Category(name="Diaries")

session.add(category9)
session.commit()


print "Categories has been created"
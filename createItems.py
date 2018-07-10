from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

# connecting to the category database
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#items of category1
category1 = Category(name="Math")

Item1 = Item(name="A Mind for Numbers", description="Whether you are a student struggling to fulfill a math or science requirement, or you are embarking on a career change that requires a new skill set, A Mind for Numbers offers the tools you need to get a better grasp of that intimidating material. Engineering professor Barbara Oakley knows firsthand how it feels to struggle with math.",
                     category=category1)

session.add(Item1)
session.commit()

Item2 = Item(name="Be a Human Calculator", description="There are plenty of books available in the market on faster calculations but more often than not the authors of such books had not tested the techniques they propound and promote in real life problem solving situations. However, the techniques that you shall find in this book have been tested and used (not only by the author but by countless other people) in examinations time and again. ",
                     category=category1)

session.add(Item2)
session.commit()



#items of category3
category3 = Category(name="Science")

Item4 = Item(name="Origin Story", description="Most historians study the smallest slivers of time, emphasizing specific dates, individuals, and documents. But what would it look like to study the whole of history, from the big bang through the present day -- and even into the remote future? How would looking at the full span of time change the way we perceive the universe, the earth, and our very existence?",
                     category=category3)

session.add(Item4)
session.commit()



# items of category4
category4 = Category(name="Health")

Item5 = Item(name="The Good Gut", description="The Good Gut is a groundbreaking work that offers a new plan for health that focuses on how to nourish your microbiota, including recipes and a menu plan. The Sonnenburgs show how we can keep our microbiota off the endangered species list and strengthen the community that inhabits our gut and thereby improve our own health. In this important and timely investigation, they look at safe alternatives to antibiotics; dietary and lifestyle choices to encourage microbial health; the management of the aging microbiota; and the nourishment of your own individual microbiome.",
                     category=category4)

session.add(Item5)
session.commit()



print "Items has been created"
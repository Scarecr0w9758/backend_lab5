from sqlalchemy import create_engine,ForeignKey, Column, String, Integer,CHAR,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
import sys
sys.path.append('..')
import dbconfig
# host,user,password,db_name
Base = declarative_base()

class Product(Base):
    __tablename__="Products"
    ID=Column("Id",Integer,primary_key=True)
    NAME=Column('Name', String)    
    DESCRIPTION=Column('Description', String)    
    PRICE=Column('Price', String)    
    CATEGORY_ID=Column('Category_Id', String)    
    MODIFIED=Column('Modified', Integer)    
    CREATED=Column('Created', Integer)    

    def __init__(self,ID, NAME, DESCRIPTION,PRICE,CATEGORY_ID,MODIFIED,CREATED):
        self.ID=ID
        self.NAME=NAME    
        self.DESCRIPTION=DESCRIPTION
        self.PRICE=PRICE
        self.CATEGORY_ID=CATEGORY_ID
        self.MODIFIED=MODIFIED
        self.CREATED=CREATED

    def __repr__(self):
        return f"({self.NAME} {self.DESCRIPTION} {self.PRICE} {self.CATEGORY_ID} {self.MODIFIED} {self.CREATED})"

# Подключение к серверу MySQL на localhost с помощью PyMySQL DBAPI. 
# Формат подключения: dialect+driver://username:password@host:port/database
engine = create_engine(f"mysql+pymysql://{dbconfig.user}:{dbconfig.password}@{dbconfig.host}/{dbconfig.db_name}")
# engine = create_engine("sqlite://mydb.db", echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

product=Product("Ma","tvey",300,1,1,1)
session.add(product)
session.commit()

p1=Product("Mu","te",400,0,0,0)
session.add(p1)
session.commit()

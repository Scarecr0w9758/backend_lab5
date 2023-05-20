from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, VARCHAR, String, DateTime
from sqlalchemy.orm import DeclarativeBase,sessionmaker
import sys
sys.path.append('..')
import dbconfig
from datetime import datetime

# строка подключения
# engine_name = f"postgresql+psycopg2://{dbconfig.user}:{dbconfig.password}@{dbconfig.host}:{dbconfig.port}/{dbconfig.db_name}"
engine_name = f"mysql+pymysql://{dbconfig.user}:{dbconfig.password}@{dbconfig.host}/{dbconfig.db_name}"
# создаем движок SqlAlchemy
engine = create_engine(engine_name)
#создаем базовый класс для моделей
class Base(DeclarativeBase): pass
  
# создаем модель, объекты которой будут храниться в бд
class Product(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    category_id = Column(Integer)
    created=Column(DateTime(), default=datetime.now),
    modified=Column(DateTime(), default=datetime.now, onupdate=datetime.now)
  
Base.metadata.create_all(bind=engine)

 































# import pymysql
# import sys
# sys.path.append('..')
# from dbconfig import host,user,password,db_name
# try:
#     connection=pymysql.connect(
#         host=host,
#         user=user,
#         password=password,
#         port=3306,
#         cursorclass=pymysql.cursors.DictCursor,
#         database=db_name,
#     )
       
# except Exception as ex:
#     # finally:
#     #     connection.close()
#     print("connection refused with: ", ex)

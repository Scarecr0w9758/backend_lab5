from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, VARCHAR, String, DateTime
from sqlalchemy.orm import DeclarativeBase,sessionmaker
import sys
sys.path.append('..')
import dbconfig
import datetime
# строка подключения
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
  
Base.metadata.create_all(bind=engine)
# with Session(autoflush=True, bind=engine) as db:
#     bread=Product(name="bread",description="empty desc", price=50,category_id=14)
#     db.add(bread)
#     db.commit()
#     print(bread.id)

# создаем таблицы
 
print("База данных и таблица созданы")
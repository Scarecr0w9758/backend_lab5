from mainImports import *
# TODO: pagination
def getProductList():
    with Session(autoflush=True, bind=engine) as db:
        product_query=db.query(Product).all()
        # Доделавй цикл фор ин в котором вызывай чтение по ID
        db.commit()
        return product_query[0].name

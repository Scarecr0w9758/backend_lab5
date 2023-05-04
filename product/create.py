from mainImports import *
def createProduct(productName, productDescription, productPrice, productCategoryId):
    with Session(autoflush=True, bind=engine) as db:
        bread=Product(name=productName,description=productDescription, price=productPrice,category_id=productCategoryId)
        db.add(bread)
        db.commit()
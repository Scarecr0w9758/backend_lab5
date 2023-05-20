from mainImports import *
from read_one import getProductById
def createProduct(productName, productDescription, productPrice, productCategoryId):
    with Session(autoflush=True, bind=engine) as db:
        tmp_product=Product(name=productName,description=productDescription, price=productPrice,category_id=productCategoryId)
        db.add(tmp_product)
        db.commit()
        return getProductById(tmp_product.id),201
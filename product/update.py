from datetime import datetime
from mainImports import *
from read_one import getProductById
def updateProduct(productId, productName="", productDescription="", productPrice=0, productCategoryId=0):
    with Session(autoflush=True, bind=engine) as db:
        productQuery=db.query(Product).get(productId)
        if (productName!=""):
            productQuery.name = productName
        if (productDescription!=""):
            productQuery.description = productDescription
        if (productPrice!=0):
            productQuery.price= productPrice
        if (productCategoryId!=0):
            productQuery.category_id = productCategoryId
        db.commit()
        return getProductById(productId)
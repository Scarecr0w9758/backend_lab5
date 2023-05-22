from mainImports import *
def getProductById(productId):
    with Session(autoflush=True, bind=engine) as db:
        product_query=db.query(Product).get(productId)
        to_json = {
            "id" : product_query.id,
            "name" : product_query.name,
            "description" : product_query.description,
            "price" : product_query.price,
            "category_id" : product_query.category_id,
        }
        db.commit()
        return to_json

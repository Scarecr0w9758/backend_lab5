from mainImports import *
def deleteProductById(rowId):
    with Session(autoflush=True, bind=engine) as db:
        record_obj = db.query(Product).filter(Product.id==rowId).first()
        db.delete(record_obj)
        db.commit()
        return "was deleted succesfully"
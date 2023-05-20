from mainImports import *
# TODO: pagination
def getProductList(page=1,perPage=50):
    with Session(autoflush=True, bind=engine) as db:
        product_query_all=db.query(Product).limit(perPage).offset(int(perPage)*(int(page)-1))
        to_json_array=[]
        for element in product_query_all:
            tmp_json={}
            tmp_json['id'] = element.id
            tmp_json['name'] = element.name
            tmp_json['description'] = element.description
            tmp_json['price'] = element.price
            tmp_json['category_id'] = element.category_id
            to_json_array.append(tmp_json)
        db.commit()
        return to_json_array
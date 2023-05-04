from mainImports import *
def createProduct(productName, productDescription, productPrice, productCategoryId):
    try:
        print('success connected')
        try:
            with app.app_context():
                with connection.cursor() as cursor:
                    insert_query=\
                    f"INSERT INTO `PRODUCTS`\
                    (NAME,DESCRIPTION,\
                    PRICE,CATEGORY_ID)\
                    VALUES\
                    ('{productName}','{productDescription}',\
                    '{productPrice}','{productCategoryId}');"
                    cursor.execute(insert_query)
                    connection.commit()
                    rows=cursor.fetchall()
                    print("insert successfully")
                    return jsonify(rows)
        finally:
            connection.close()
    except Exception as ex:
        print("connection refused with: ", ex)

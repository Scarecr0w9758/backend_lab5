from mainImports import *
def createProduct(productName, productDescription, productPrice, productCategoryId):
    try:
        print('success connected')
        try:
            with app.app_context():
                with connection.cursor() as cursor:
                    # tmp_name='vlad'
                    # tmp_password='123'
                    # tmp_email='be@killed.ru'
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

                # with connection.cursor() as cursor:
                #     select_all_rows="SELECT * FROM `PRODUCTS`"
                #     cursor.execute(select_all_rows)
                #     rows=cursor.fetchall()
                #     # print("rows: ", rows)
                #     # for row in rows:
                #     #     print('row: ', jsonify(row))
                #     # print('#'*20)  
                #     # print("rows: After", jsonify(rows))
        finally:
            connection.close()
    except Exception as ex:
        print("connection refused with: ", ex)

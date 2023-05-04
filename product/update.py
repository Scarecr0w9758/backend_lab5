from datetime import datetime
from mainImports import *
def updateProduct(productId, productName, productDescription, productPrice, productCategoryId):
    try:
        MODIFIED_DATE=datetime.now()
        print("mDate",MODIFIED_DATE)
        print('success connected')
        try:
            with app.app_context():
                with connection.cursor() as cursor:
                    update_query=f"UPDATE `PRODUCTS`\
                    SET NAME='{productName}',\
                    DESCRIPTION='{productDescription}',\
                    PRICE='{productPrice}',\
                    CATEGORY_ID='{productCategoryId}',\
                    MODIFIED='{MODIFIED_DATE}'\
                    WHERE ID ='{productId}';"
                    cursor.execute(update_query)
                    connection.commit()
                    rows=cursor.fetchall()
                    return jsonify(rows)
        except Exception as ex:
            print("connection refused with: ", ex)

        finally:
            connection.close()
    except Exception as ex:
        print("connection refused with: ", ex)

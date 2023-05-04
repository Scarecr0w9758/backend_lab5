from mainImports import *

def deleteProductById(rowId):
    try:
        print('success connected')
        try:
            with app.app_context():
                 with connection.cursor() as cursor:
                    delete_query=f"DELETE FROM `PRODUCTS` WHERE id = '{rowId}';" 
                    cursor.execute(delete_query)
                    rows=cursor.fetchall()
                    connection.commit()
                    return jsonify(rows)
        finally:
            connection.close()
    except Exception as ex:
        print("connection refused with: ", ex)


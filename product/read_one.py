from mainImports import *
# TODO: pagination
def getProductById(productId):
    try:
        try:
            with app.app_context():
                with connection.cursor() as cursor:
                    select_all_rows=f"SELECT * FROM `PRODUCTS` WHERE ID={productId}"
                    cursor.execute(select_all_rows)
                    rows=cursor.fetchall()
                    return jsonify(rows)
        finally:
            connection.close()
    except Exception as ex:
        print("connection refused with: ", ex)

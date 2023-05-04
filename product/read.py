from mainImports import *
# TODO: pagination
def getProductList():
    try:
        print('success connected')
        try:
            with app.app_context():
                with connection.cursor() as cursor:
                    select_all_rows="SELECT * FROM `PRODUCTS`"
                    cursor.execute(select_all_rows)
                    rows=cursor.fetchall()
                    return jsonify(rows)
        finally:
            connection.close()
    except Exception as ex:
        print("connection refused with: ", ex)

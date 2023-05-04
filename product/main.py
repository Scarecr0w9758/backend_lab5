from read import getProductList
from read_one import getProductById
from create import createProduct 
from delete import deleteProductById 
from update import updateProduct
from flask import Flask, jsonify

# Все методы (импортированные) настроены и готовы к работе
# осталось:
# • Пагинация
# • Товары с пагинацией (по урлу в гет запросе)
# • +++ Получение ОДНОГО товара по ID - сделал
# •


# getProductList()

# deleteProductById(5)

# updateProduct(3,'Jora2', "1just a regular product to improve uyour lfe",400,2)
print(getProductList())
app=Flask(__name__)

# @app.route('/productList',methods=['GET'])
# getProductList()


if __name__ == '__main__':
    pass
    # app.run()
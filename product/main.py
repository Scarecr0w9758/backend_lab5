from read import getProductList
from read_one import getProductById
from create import createProduct 
from delete import deleteProductById 
from update import updateProduct
from flask import Flask, Request, jsonify, request
import requests

# Все методы (импортированные) настроены и готовы к работе
# осталось:
# • Пагинация
# • Товары с пагинацией (по урлу в гет запросе)
# • +++ Получение ОДНОГО товара по ID - сделал
# •
app=Flask(__name__)

# Наверное декораторы надо в отд. файлах юзать
@app.route('/',methods=['GET'])
def hello():
    return "<h1>Main page of the productList</h1>"

@app.route('/products',methods=['GET'])
def getProducts():
    page=request.args.get('page',default=1)
    perPage=request.args.get('perPage',default=50)
    print(page)
    print(perPage)
    return getProductList(page,perPage)

@app.route('/products/create',methods=['POST'])
def createNewProduct():
    request_data=request.get_json(force=True)
    return createProduct(
    productName = request_data["name"],
    productDescription = request_data["description"],
    productPrice = request_data["price"],
    productCategoryId= request_data["category_id"])


# разобраться почему не работает делит и пут, а также добавить прокидку параметров элементов 
@app.route('/products/<id>',methods=["GET" ,"DELETE", "PUT"])
def changeOneProduct(id):
    if request.method=="DELETE":
        return deleteProductById(id)    
    elif request.method=="PUT":
        request_data=request.get_json(force=True)
        return updateProduct(id,
        productName = request_data["name"],
        productDescription = request_data["description"],
        productPrice = request_data["price"],
        productCategoryId= request_data["category_id"])    
    elif request.method=="GET":
        return getProductById(id)    


if __name__ == '__main__':
    app.run(port=5050)
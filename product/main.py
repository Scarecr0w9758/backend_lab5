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
    return getProductList()

@app.route('/products/create',methods=['POST'])
def createProduct():
    return request.get_json()["name"]


# разобраться почему не работает делит и пут, а также добавить прокидку параметров элементов 
@app.route('/products/<id>',methods=["GET" ,"DELETE", "POST"])
def changeOneProduct(id):
    request_data=request.get_json()
    if request.method=="DELETE":
        return deleteProductById(id)    
    elif request.method=="POST":
        return updateProduct(id,request_data["name"])    
    elif request.method=="GET":
        return getProductById(id)    


if __name__ == '__main__':
    app.run(port=8080)
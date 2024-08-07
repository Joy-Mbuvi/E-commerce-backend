from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from .models import Product
product_blueprint = Blueprint('product', __name__)

@product_blueprint.route("/products", methods=['GET'])
@jwt_required()
def get_all_product():#unapat all product
 products = Product.query.all()  
 products_list = []
 for product in products:
        products_list.append({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock": product.stock,
            "image_url":product.image_url
        })

 return jsonify(products_list)

@product_blueprint.route("/products/search", methods=['GET'])
@jwt_required() #unaserach na product name
def search_product():
    query = request.args.get('query', '')
    products = Product.query.filter(Product.name == query).all()

    if not products:
        return jsonify({"message": "We dont have that here :)"}), 404


    products_list = []
    for product in products:
        products_list.append({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock": product.stock,
            "image_url":product.image_url

        })

    return jsonify(products_list)
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from .models import Product
market_blueprint = Blueprint('market', __name__)

@market_blueprint.route("/products", methods=['GET'])
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
        })

 return jsonify(products_list)

@market_blueprint.route("/products/<int:product_id>", methods=['GET'])#read
@jwt_required() #get a single product
def get_one_product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    
    if not product:
        return jsonify({"message": "We dont have that here :)"}), 404


    product_data = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock,
    }

    return jsonify(product_data)


from flask import Blueprint,jsonify,request
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import db
from .models import Favourite,Product

favourite_blueprint=Blueprint("favourite_route",__name__)

@favourite_blueprint.route("/favourites",methods=['GET'])
@jwt_required()
def view_favourites():
    current_user=get_jwt_identity()
    user_id = current_user['id']

    favourites=Favourite.query.filter_by(user_id=user_id).all()
    fav_products=[]
    for favourite in favourites:
        product=Product.query.get(favourite.product_id)
        fav_products.append({
            "id":product.id,
            "name":product.name,
            "description":product.description,
            "price":product.price,
            "stock":product.stock,
            "image_url":product.image_url

        })

    return jsonify(fav_products)


@favourite_blueprint.route("/favourites/add",methods=['POST'])
@jwt_required()
def add_favourites():
    current_user=get_jwt_identity()
    user_id = current_user['id']
    data = request.get_json()

    product_id=data.get("product_id")

    favourites=Favourite.query.filter_by(user_id=user_id,product_id=product_id).first()
    if  favourites:
        return jsonify({"message": "Product already in Favourites"}),200
    
    new_favourite = Favourite(user_id=user_id, product_id=product_id)
    db.session.add(new_favourite)
    db.session.commit()
    return jsonify({"message":"Product successfully added to favourites"})
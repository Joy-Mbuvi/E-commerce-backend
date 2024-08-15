from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import db
from .models import Cart, Product, User, CartItem

cart_routes = Blueprint('cart_routes', __name__)

@cart_routes.route('/cart', methods=['GET'])
@jwt_required()
def view_cart():
    current_user = get_jwt_identity()
    user = User.query.get(current_user['id'])
    cart = Cart.query.filter_by(user_id=user.id).first()
    
    if not cart:
        return jsonify({'message': 'Cart is empty'}), 200
    
    cart_items = []
    for item in cart.items:
        product = Product.query.get(item.product_id)
        cart_items.append({
            'product_id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': item.quantity,
            "image_url" : product.image_url,
            "description":product.description

        })
    
    return jsonify({'cart_items': cart_items}), 200

@cart_routes.route('/cart/add', methods=['POST'])
@jwt_required()
def add_to_cart():
    try:
        current_user = get_jwt_identity()
        user = User.query.get(current_user['id'])
        if not user:
            return jsonify({'message': 'User not found'}), 404

        data = request.get_json()
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        product = Product.query.get(product_id)
        if not product:
            return jsonify({'message': 'Product not found :('}), 404

        if not user.cart:
            cart = Cart(user_id=user.id)
            db.session.add(cart)
            db.session.flush()  # This will assign an ID to the cart without committing the transaction
        else:
            cart = user.cart

        cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
            db.session.add(cart_item)

        db.session.commit()
        return jsonify({'message': 'Item added to cart'}), 201
    except Exception as e:
        db.session.rollback()
        print(f"Error in add_to_cart: {str(e)}")
        return jsonify({'message': 'An error occurred while processing your request'}), 500

@cart_routes.route('/cart/update', methods=['PUT'])
@jwt_required()
def update_cart_item():
    current_user = get_jwt_identity()
    user = User.query.get(current_user['id'])
    data = request.get_json()
    
    product_id = data.get('product_id')
    new_quantity = data.get('quantity')
    
    cart = Cart.query.filter_by(user_id=user.id).first()
    if not cart:
        return jsonify({'message': 'Cart not found'}), 404
    
    cart_item = next((item for item in cart.items if item.product_id == product_id), None)
    if not cart_item:
        return jsonify({'message': 'Item not in cart'}), 404
    
    if new_quantity > 0:
        cart_item.quantity = new_quantity
    else:
        db.session.delete(cart_item)
    
    db.session.commit()
    return jsonify({'message': 'Cart updated'}), 200

@cart_routes.route('/cart/remove', methods=['DELETE'])
@jwt_required()
def remove_from_cart():
    current_user = get_jwt_identity()
    user = User.query.get(current_user['id'])
    data = request.get_json()
    
    product_id = data.get('product_id')
    
    cart = Cart.query.filter_by(user_id=user.id).first()
    if not cart:
        return jsonify({'message': 'Cart not found'}), 404
    
    cart_item = next((item for item in cart.items if item.product_id == product_id), None)
    if not cart_item:
        return jsonify({'message': 'Item not in cart'}), 404
    
    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({'message': 'Item removed from cart'}), 200

@cart_routes.route('/cart/clear', methods=['DELETE'])
@jwt_required()
def clear_cart():
    current_user = get_jwt_identity()
    user = User.query.get(current_user['id'])
    
    cart = Cart.query.filter_by(user_id=user.id).first()
    if not cart:
        return jsonify({'message': 'Cart is already empty'}), 200
    
    for item in cart.items:
        db.session.delete(item)
    
    db.session.commit()
    return jsonify({'message': 'Cart cleared'}), 200



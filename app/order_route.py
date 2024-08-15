from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, Order, Cart, Product
from datetime import datetime

order_routes = Blueprint('order_routes', __name__)


@order_routes.route('/orders/<int:order_id>', methods=['GET'])
@jwt_required()
def get_order_details(order_id):
    current_user = get_jwt_identity()
    order = Order.query.filter_by(id=order_id, user_id=current_user['id']).first()
    
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    return jsonify({
        'order_id': order.id,
        'user_id': order.user_id,
        'cart_id': order.cart_id,
        'status': order.status,
        'total_price': order.total_price
    }), 200

@order_routes.route('/orders/<int:order_id>', methods=['PUT'])
@jwt_required()
def update_order_details(order_id):
    current_user = get_jwt_identity()
    order = Order.query.filter_by(id=order_id, user_id=current_user['id']).first()
    
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    data = request.get_json()
    if 'total_price' in data:
        order.total_price = data['total_price']
    
    db.session.commit()
    return jsonify({'message': 'Order updated successfully'}), 200

@order_routes.route('/orders/<int:order_id>/status', methods=['PATCH'])
@jwt_required()
def update_order_status(order_id):
    current_user = get_jwt_identity()
    order = Order.query.filter_by(id=order_id, user_id=current_user['id']).first()
    
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    data = request.get_json()
    if 'status' in data:
        order.status = data['status']
    
    db.session.commit()
    return jsonify({'message': 'Order status updated successfully'}), 200

@order_routes.route('/orders', methods=['GET'])
@jwt_required()
def list_orders():
    current_user = get_jwt_identity()
    orders = Order.query.filter_by(user_id=current_user['id']).all()

    if not orders:
        print(f"No orders found for user ID {current_user['id']}")
        
    return jsonify([{
        'order_id': order.id,
        'cart_id': order.cart_id,
        'status': order.status,
        'total_price': order.total_price
    } for order in orders]), 200

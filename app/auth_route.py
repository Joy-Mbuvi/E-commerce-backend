from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from .import db, bcrypt
from .models import User
from datetime import timedelta, datetime

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route("/signup", methods=["POST"])
def signup():
    body = request.get_json()
    username = body.get('username')
    email = body.get('email')
    password = body.get('password')

    # Validation
    if not email or not password or not username:
        return jsonify({'message': "Required field missing"}), 400
    
    if len(username) < 3:
        return jsonify({'message': "Username too short"}), 400
    
    if len(email) < 4:
        return jsonify({'message': "Email too short"}), 400
    
    if len(password) < 6:
        return jsonify({'message': "Password too short"}), 400
    
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
       return jsonify({'message': f"Email already in use {email}"}), 400
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf8')
    
    person = User(username=username, email=email, hash_password=hashed_password)
    db.session.add(person)
    db.session.commit()
    
    return jsonify({"message": "Sign up successful"}), 201

@auth_blueprint.route("/login", methods=["POST"])
def login():
    body = request.get_json()
    email = body.get('email')
    password = body.get('password')

    # Validation
    if not email or not password:
        return jsonify({'message': "Required field missing"}), 400
    
    person = User.query.filter_by(email=email).first()
    if not person:
        return jsonify({'message': "User not found"}), 404
    
    pass_ok = bcrypt.check_password_hash(person.hash_password.encode('utf-8'), password)
    if not pass_ok:
        return jsonify({"message": "Invalid password"}), 401

    expires = datetime.utcnow() + timedelta(hours=24)
    access_token = create_access_token(
        identity={"id": person.id, "username": person.username},
        expires_delta=(expires - datetime.utcnow())
    )
   
    return jsonify({
        'user': {
            'id': person.id,
            'username': person.username,
            'email': person.email
        },
        'token': access_token
    })


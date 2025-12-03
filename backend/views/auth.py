from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Vendor

auth_bp = Blueprint('auth', __name__, url_prefix='/api')
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    is_vendor = data.get('is_vendor', False)

    if not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Missing required fields"}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400
    
    hashed_password = generate_password_hash(data['password'])
    new_user = User(username=data['username'], 
                        email=data['email'], 
                        password=hashed_password, 
                        is_vendor=is_vendor)
    db.session.add(new_user)
    db.session.flush()

    if is_vendor:
        new_vendor = Vendor(user_id=new_user.id, name=username)
        db.session.add(new_vendor)
        db.session.commit()

    return jsonify({"success": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data.get('email') or not data.get('password'):
        return jsonify({"error": "Missing email or password"}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity={'id': user.id, 'is_vendor': user.is_vendor})
    return jsonify({"access_token": access_token}), 200
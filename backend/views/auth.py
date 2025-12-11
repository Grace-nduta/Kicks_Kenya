from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Vendor

auth_bp = Blueprint('auth', __name__, url_prefix='/api')
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = "user"   # Fixed role for all new registrants

    
    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    hashed_password = generate_password_hash(password)

    # Create normal user
    new_user = User(
        username=username,
        email=email,
        password=hashed_password,
        role=role
    )
    db.session.add(new_user)
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

    access_token = create_access_token(identity={'id': user.id, 'role': user.role})
    return jsonify({"access_token": access_token}), 200
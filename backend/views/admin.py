from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
from models import db, User, Vendor

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')

@admin_bp.route('/create-vendor', methods=['POST'])
@jwt_required()
def create_vendor():
    current_user = get_jwt_identity()

    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    vendor_user = User(
        username=username,
        email=email,
        password=generate_password_hash(password),
        role='vendor'
    )
    db.session.add(vendor_user)
    db.session.flush()

    vendor_profile = Vendor(
        username=username,
        email=email,
        user_id=vendor_user.id
    )
    db.session.add(vendor_profile)

    db.session.commit()

    return jsonify({"success": "Vendor created successfully"}), 201

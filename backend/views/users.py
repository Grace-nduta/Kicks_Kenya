from flask import Blueprint, request, jsonify
from models import db, User, Shoe

users_bp = Blueprint('users', __name__, url_prefix='/api')

@users_bp.route('/shoes', methods=['GET'])
def get_shoes():
    shoes =Shoe.query.all()
    return jsonify([{
        'id': shoe.id,
        'name': shoe.name,
        'size': shoe.size,
        'color': shoe.color,
        'price': shoe.price
    } for shoe in shoes]), 200





    
from flask import Blueprint, request, jsonify
from models import db, Shoe

shoes_bp = Blueprint('shoes', __name__, url_prefix='/api')

@shoes_bp.route('/shoes', methods=['GET'])
def get_shoes():
    shoes = Shoe.query.all()
    shoes_list = [{"id": shoe.id, "name": shoe.name, "brand": shoe.brand, "status":shoe.status, "image_url":shoe.image_url} for shoe in shoes]
    return jsonify(shoes_list), 200
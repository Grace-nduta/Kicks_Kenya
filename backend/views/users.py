from flask import Blueprint, request, jsonify
from models import db, User, Shoe

users_bp = Blueprint('users', __name__, url_prefix='/api')

@users_bp.route('/shoes', methods=['GET'])
def get_shoes():
    shoes =Shoe.query.all()
    result = []
    
    for shoe in shoes:
        variants = [ v for v in shoe.variants if v.stock > 0 ]
        
        if not variants:
            continue # Skip shoes with no available variants/stock
        
        prices = [v.price for v in variants]
        sizes = sorted({v.size for v in variants})
        colors = sorted({v.color for v in variants})
        
        result.append({
            'id': shoe.id,
            'name': shoe.name,
            'brand': shoe.brand,
            'status': shoe.status,
            'image_url': shoe.image_url,
            'available_sizes': sizes,
            'available_colors': colors,
            'min_price': min(prices),
            'max_price': max(prices),
            'vendor_id': shoe.vendor_id 
        })    
    return jsonify(result), 200





    
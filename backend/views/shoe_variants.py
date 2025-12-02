from flask import Blueprint, request, jsonify
from models import db, ShoeVariant

shoe_variants_bp = Blueprint('shoe_variants', __name__, url_prefix='/shoe_variants')
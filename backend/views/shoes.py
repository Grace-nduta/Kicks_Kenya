from flask import Blueprint, request, jsonify
from models import db, Shoe

shoes_bp = Blueprint('shoes', __name__, url_prefix='/shoes')

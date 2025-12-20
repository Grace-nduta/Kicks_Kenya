from flask import Blueprint, request, jsonify
from models import db, Favorite

favorites_bp = Blueprint('favorites', __name__, url_prefix='/favorites')
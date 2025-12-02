from flask import Blueprint, request, jsonify
from models import db, User, Vendor

auth_bp = Blueprint('auth', __name__, url_prefix='/api')
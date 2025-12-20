from flask import Blueprint, request, jsonify
from models import db, Vendor

vendors_bp = Blueprint('vendors', __name__, url_prefix='/vendors')
from flask import Blueprint, request, jsonify
from models import db, Sale

sales_bp = Blueprint('sales', __name__, url_prefix='/sales')
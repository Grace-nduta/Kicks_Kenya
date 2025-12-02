from flask import Blueprint, request, jsonify
from models import db, User

users_bp = Blueprint('users', __name__, url_prefix='/users')
from flask import Flask
from models import db, User, Vendor, Shoe, ShoeVariant, Sale, Favorite
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
load_dotenv()
import os

app = Flask(__name__)

# Import Blueprints
from views.users import users_bp
from views.vendors import vendors_bp
from views.shoes import shoes_bp
from views.shoe_variants import shoe_variants_bp
from views.sales import sales_bp
from views.favorites import favorites_bp
from views.auth import auth_bp

# Register Blueprints
app.register_blueprint(users_bp)
app.register_blueprint(vendors_bp)
app.register_blueprint(shoes_bp)
app.register_blueprint(shoe_variants_bp)
app.register_blueprint(sales_bp)
app.register_blueprint(favorites_bp)
app.register_blueprint(auth_bp)

# configurations
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback_secret")   # Needed by Flask
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "fallback_jwt")  # Needed by JWT
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI", "sqlite:///shoes.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
jwt=JWTManager(app)

@app.route('/')
def home():
    return "Welcome to the Shoe Store API"

if __name__ == '__main__':
    app.run(debug=True)
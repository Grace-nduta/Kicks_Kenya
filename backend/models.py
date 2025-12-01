from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

# ------------------- USERS --------------------
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    sales = db.relationship('Sale', back_populates='user', cascade='all, delete-orphan', lazy=True)
    favorites = db.relationship('Favorite', back_populates='user', cascade='all, delete-orphan' lazy=True)
 
# ------------------- VENDORS --------------------
class Vendor(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    
    # Relationships
    shoes = db.relationship('Shoe', backref='vendor', lazy=True)   

# ------------------- SHOES --------------------
class Shoe(db.Model):
    __tablename__ = 'shoes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='available')
    image_url = db.Column(db.String(255), nullable=False)
    
    # Relationships
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    variants = db.relationship('ShoeVariant', backref='shoe', lazy=True)
    favorites = db.relationship('Favorite', back_populates='shoe', lazy=True)
    
# ------------------- SHOE VARIANTS --------------------
class ShoeVariant(db.Model):
    __tablename__ = 'shoe_variants'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Float, nullable=False)
    color = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    
    # Relationships
    shoe_id = db.Column(db.Integer, db.ForeignKey('shoes.id'), nullable=False)
    sales = db.relationship('Sale', back_populates='shoe_variant', lazy=True)
 
# ------------------- SALES --------------------   
class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    shoe_variant_id = db.Column(db.Integer, db.ForeignKey('shoe_variants.id'), nullable=False)
    
    user = db.relationship('User', back_populates='sales')
    shoe_variant = db.relationship('ShoeVariant', back_populates='sales')
 
# ------------------- FAVORITES --------------------   
class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    
    # Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    shoe_id = db.Column(db.Integer, db.ForeignKey('shoes.id'), nullable=False)
    
    user = db.relationship('User', back_populates='favorites')
    shoe = db.relationship('Shoe', back_populates='favorites')
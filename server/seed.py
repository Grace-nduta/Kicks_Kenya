from app import app
from models import db, User, Vendor, Shoe, ShoeVariant, Sale, Favorite
from werkzeug.security import generate_password_hash

def seed_data():
    with app.app_context():

        print("Clearing existing data...")
        Favorite.query.delete()
        Sale.query.delete()
        ShoeVariant.query.delete()
        Shoe.query.delete()
        Vendor.query.delete()
        User.query.delete()

        # ------------------- USERS --------------------
        admin = User(
            username="Grace Kahare",
            email="ndutak6466@gmail.com",
            password=generate_password_hash("ndutakahare"),
            role="admin"
        )

        vendor_user = User(
            username="Kicks Kenya Official",
            email="gg@kickskenya.com",
            password=generate_password_hash("ggkickskenya123"),
            role="vendor"
        )

        normal_user = User(
            username="Grace Nduta",
            email="grace.nduta@example.com",
            password=generate_password_hash("password123"),
            role="user"
        )

        db.session.add_all([admin, vendor_user, normal_user])
        db.session.commit()

        # ------------------- VENDOR --------------------
        vendor = Vendor(
            username="Kicks Kenya Official",
            email="vendor@kickskenya.com",
            phone_number="+254700000000",
            user_id=vendor_user.id
        )

        db.session.add(vendor)
        db.session.commit()

        # ------------------- SHOES --------------------
        airforce = Shoe(
            name="Air Force 1",
            brand="Nike",
            image_url="https://example.com/airforce.jpg",
            vendor_id=vendor.id
        )

        yeezy = Shoe(
            name="Yeezy Boost 350",
            brand="Adidas",
            image_url="https://example.com/yeezy.jpg",
            vendor_id=vendor.id
        )

        jordan = Shoe(
            name="Air Jordan 1",
            brand="Nike",
            image_url="https://example.com/jordan.jpg",
            vendor_id=vendor.id
        )

        db.session.add_all([airforce, yeezy, jordan])
        db.session.commit()

        # ------------------- SHOE VARIANTS --------------------
        variants = [
            ShoeVariant(size=42, color="White", price=12000, stock=10, shoe_id=airforce.id),
            ShoeVariant(size=43, color="Black", price=12500, stock=5, shoe_id=airforce.id),

            ShoeVariant(size=41, color="Cream", price=30000, stock=3, shoe_id=yeezy.id),
            ShoeVariant(size=42, color="Grey", price=32000, stock=2, shoe_id=yeezy.id),

            ShoeVariant(size=44, color="Red/Black", price=18000, stock=6, shoe_id=jordan.id),
            ShoeVariant(size=45, color="White/Blue", price=18500, stock=4, shoe_id=jordan.id),
        ]

        db.session.add_all(variants)
        db.session.commit()

        print("Database seeded successfully.")

if __name__ == "__main__":
    seed_data()

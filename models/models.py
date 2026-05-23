from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# ==========================================
# MENU MODEL
# ==========================================
class Menu(db.Model):

    __tablename__ = "menu"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    category = db.Column(db.String(100), nullable=False)

    price = db.Column(db.Float, nullable=False)

    image = db.Column(db.String(500))

    offer = db.Column(db.String(100))

    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "category": self.category,

            "price": self.price,

            "image": self.image,

            "offer": self.offer

        }


# ==========================================
# ORDER MODEL
# ==========================================
class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    customer_name = db.Column(db.String(100), nullable=False)

    items = db.Column(db.Text, nullable=False)

    total_price = db.Column(db.Float, nullable=False)

    def to_dict(self):

        return {

            "id": self.id,

            "customer_name": self.customer_name,

            "items": self.items,

            "total_price": self.total_price

        }
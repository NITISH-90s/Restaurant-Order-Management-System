from flask import Flask, render_template

# -----------------------------
# EXTENSIONS
# -----------------------------

from flask_socketio import SocketIO
from flask_mail import Mail
from flask_jwt_extended import JWTManager

# -----------------------------
# DATABASE
# -----------------------------

from models.models import db

# -----------------------------
# BLUEPRINT ROUTES
# -----------------------------

from routes.menu_routes import menu_bp
from routes.order_routes import order_bp
from routes.analytics_routes import analytics_bp
from routes.auth_routes import auth_bp


# =========================================================
# CREATE FLASK APP
# =========================================================

app = Flask(__name__)


# =========================================================
# CONFIGURATION
# =========================================================

app.config["SECRET_KEY"] = "restaurant_secret_key"

app.config["JWT_SECRET_KEY"] = "jwtsecretkey"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurant.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# =========================================================
# MAIL CONFIGURATION
# =========================================================

app.config["MAIL_SERVER"] = "smtp.gmail.com"

app.config["MAIL_PORT"] = 587

app.config["MAIL_USE_TLS"] = True

app.config["MAIL_USE_SSL"] = False

app.config["MAIL_USERNAME"] = "your_email@gmail.com"

app.config["MAIL_PASSWORD"] = "your_app_password"


# =========================================================
# INITIALIZE EXTENSIONS
# =========================================================

db.init_app(app)

socketio = SocketIO(app, cors_allowed_origins="*")

mail = Mail(app)

jwt = JWTManager(app)


# =========================================================
# REGISTER BLUEPRINTS
# =========================================================

app.register_blueprint(auth_bp)

app.register_blueprint(menu_bp)

app.register_blueprint(order_bp)

app.register_blueprint(analytics_bp)


# =========================================================
# HOME ROUTE
# =========================================================

@app.route("/")
def home():

    return render_template("index.html")


# =========================================================
# LOGIN PAGE
# =========================================================

@app.route("/login")
def login():

    return render_template("login.html")


# =========================================================
# BILLING PAGE
# =========================================================

@app.route("/billing-page")
def billing():

    return render_template("invoice.html")

# =========================================================
# MENU PAGE
# =========================================================

@app.route("/menu-page")
def menu():

    return render_template("menu.html")


# =========================================================
# ORDERS PAGE
# =========================================================

@app.route("/orders-page")
def orders_page():

    return render_template("orders.html")


# =========================================================
# ANALYTICS PAGE
# =========================================================

@app.route("/analytics-page")
def analytics_page():

    return render_template("analytics.html")


# =========================================================
# DASHBOARD PAGE
# =========================================================

@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")


# =========================================================
# CREATE DATABASE TABLES
# =========================================================

with app.app_context():

    db.create_all()


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    socketio.run(

        app,
        host="0.0.0.0",
        port=5000,
        debug=True

    )
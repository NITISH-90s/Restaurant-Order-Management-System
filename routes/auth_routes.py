from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth_bp = Blueprint('auth_bp', __name__)


# ==========================================
# LOGIN ROUTE
# ==========================================
@auth_bp.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    # GET USER INPUT
    username = data.get('username')
    password = data.get('password')

    # SIMPLE ADMIN LOGIN
    if username == 'admin' and password == 'admin123':

        # CREATE JWT TOKEN
        token = create_access_token(
            identity=username,
            expires_delta=timedelta(hours=5)
        )

        return jsonify({
            "status": "success",
            "message": "Login Successful",
            "token": token,
            "user": username
        }), 200

    # MANAGER LOGIN
    elif username == 'manager' and password == 'manager123':

        token = create_access_token(
            identity=username,
            expires_delta=timedelta(hours=5)
        )

        return jsonify({
            "status": "success",
            "message": "Manager Login Successful",
            "token": token,
            "user": username
        }), 200

    # INVALID LOGIN
    return jsonify({
        "status": "error",
        "message": "Invalid Username or Password"
    }), 401


# ==========================================
# REGISTER ROUTE (DEMO)
# ==========================================
@auth_bp.route('/register', methods=['POST'])
def register():

    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:

        return jsonify({
            "status": "error",
            "message": "Username and Password required"
        }), 400

    return jsonify({
        "status": "success",
        "message": f"User {username} registered successfully"
    })


# ==========================================
# HEALTH CHECK
# ==========================================
@auth_bp.route('/auth-status', methods=['GET'])
def auth_status():

    return jsonify({
        "status": "running",
        "message": "Authentication API Working"
    })
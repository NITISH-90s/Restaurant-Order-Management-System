from flask import Blueprint, request, jsonify, render_template
from models.models import db, Menu

menu_bp = Blueprint('menu_bp', __name__)


# ==========================================
# GET ALL MENU ITEMS
# ==========================================
@menu_bp.route('/menu', methods=['GET'])
def get_menu():

    items = Menu.query.all()

    return jsonify([
        item.to_dict()
        for item in items
    ])


# ==========================================
# GET SINGLE MENU ITEM
# ==========================================
@menu_bp.route('/menu/<int:id>', methods=['GET'])
def get_single_item(id):

    item = Menu.query.get(id)

    if not item:
        return jsonify({
            "status": "error",
            "message": "Item not found"
        }), 404

    return jsonify(item.to_dict())


# ==========================================
# ADD NEW FOOD ITEM
# ==========================================
@menu_bp.route('/menu', methods=['POST'])
def add_menu():

    data = request.get_json()

    try:

        item = Menu(

            name=data['name'],
            category=data['category'],
            price=float(data['price']),
            image=data.get('image', ''),
            offer=data.get('offer', 'No Offer')

        )

        db.session.add(item)

        db.session.commit()

        return jsonify({

            "status": "success",
            "message": "Food Item Added Successfully",
            "data": item.to_dict()

        }), 201

    except Exception as e:

        return jsonify({

            "status": "error",
            "message": str(e)

        }), 500


# ==========================================
# DELETE MENU ITEM
# ==========================================
@menu_bp.route('/menu/<int:id>', methods=['DELETE'])
def delete_item(id):

    item = Menu.query.get(id)

    if not item:

        return jsonify({

            "status": "error",
            "message": "Item Not Found"

        }), 404

    db.session.delete(item)

    db.session.commit()

    return jsonify({

        "status": "success",
        "message": "Food Item Deleted Successfully"

    })


# ==========================================
# UPDATE MENU ITEM
# ==========================================
@menu_bp.route('/menu/<int:id>', methods=['PUT'])
def update_item(id):

    item = Menu.query.get(id)

    if not item:

        return jsonify({

            "status": "error",
            "message": "Food Item Not Found"

        }), 404

    data = request.get_json()

    item.name = data.get('name', item.name)

    item.category = data.get('category', item.category)

    item.price = data.get('price', item.price)

    item.image = data.get('image', item.image)

    item.offer = data.get('offer', item.offer)

    db.session.commit()

    return jsonify({

        "status": "success",
        "message": "Food Item Updated Successfully",
        "data": item.to_dict()

    })


# ==========================================
# SEARCH MENU ITEMS
# ==========================================
@menu_bp.route('/menu/search/<string:keyword>', methods=['GET'])
def search_menu(keyword):

    items = Menu.query.filter(
        Menu.name.ilike(f"%{keyword}%")
    ).all()

    return jsonify([
        item.to_dict()
        for item in items
    ])


# ==========================================
# FILTER BY CATEGORY
# ==========================================
@menu_bp.route('/menu/category/<string:category>', methods=['GET'])
def filter_category(category):

    items = Menu.query.filter_by(
        category=category
    ).all()

    return jsonify([
        item.to_dict()
        for item in items
    ])


# ==========================================
# SPECIAL OFFERS
# ==========================================
@menu_bp.route('/menu/offers', methods=['GET'])
def special_offers():

    items = Menu.query.filter(
        Menu.offer != ''
    ).all()

    return jsonify([
        item.to_dict()
        for item in items
    ])


# ==========================================
# API STATUS
# ==========================================
@menu_bp.route('/menu-status', methods=['GET'])
def menu_status():

    return jsonify({

        "status": "running",
        "message": "Menu API Working Successfully"

    })

# ============================================
# MENU HTML PAGE
# ============================================

@menu_bp.route('/menu-page')
def menu_page():

    items = Menu.query.all()

    return render_template(
        "menu.html",
        items=items
    )
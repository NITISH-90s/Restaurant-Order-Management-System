from flask import Blueprint, jsonify
from models.models import Order

analytics_bp = Blueprint('analytics_bp', __name__)


# ==============================
# TOTAL REVENUE
# ==============================
@analytics_bp.route('/analytics/revenue', methods=['GET'])
def total_revenue():

    orders = Order.query.all()

    revenue = sum(order.total_price for order in orders)

    return jsonify({
        "total_revenue": revenue
    })


# ==============================
# TOTAL ORDERS
# ==============================
@analytics_bp.route('/analytics/orders', methods=['GET'])
def total_orders():

    count = Order.query.count()

    return jsonify({
        "total_orders": count
    })


# ==============================
# MOST SOLD ITEM
# ==============================
@analytics_bp.route('/analytics/most-sold', methods=['GET'])
def most_sold_item():

    orders = Order.query.all()

    item_count = {}

    for order in orders:

        if order.item_name in item_count:
            item_count[order.item_name] += order.quantity
        else:
            item_count[order.item_name] = order.quantity

    if not item_count:
        return jsonify({
            "message": "No orders yet"
        })

    most_sold = max(item_count, key=item_count.get)

    return jsonify({
        "most_sold_item": most_sold,
        "quantity_sold": item_count[most_sold]
    })


# ==============================
# DAILY SALES ANALYTICS
# ==============================
@analytics_bp.route('/analytics/daily-sales', methods=['GET'])
def daily_sales():

    orders = Order.query.all()

    sales_data = {
        "Mon": 0,
        "Tue": 0,
        "Wed": 0,
        "Thu": 0,
        "Fri": 0,
        "Sat": 0,
        "Sun": 0
    }

    # Demo logic
    # You can later connect real datetime

    index = 0
    days = list(sales_data.keys())

    for order in orders:

        day = days[index % 7]

        sales_data[day] += order.total_price

        index += 1

    return jsonify(sales_data)


# ==============================
# TOP 5 ORDERS
# ==============================
@analytics_bp.route('/analytics/top-orders', methods=['GET'])
def top_orders():

    orders = Order.query.order_by(
        Order.total_price.desc()
    ).limit(5).all()

    result = []

    for order in orders:

        result.append({
            "customer_name": order.customer_name,
            "item_name": order.item_name,
            "quantity": order.quantity,
            "total_price": order.total_price
        })

    return jsonify(result)


# ==============================
# ORDER STATUS
# ==============================
@analytics_bp.route('/analytics/status', methods=['GET'])
def analytics_status():

    return jsonify({
        "status": "Running",
        "message": "Analytics API Working Successfully"
    })
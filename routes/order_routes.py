from flask import Blueprint, request, jsonify, send_file
from models.models import db, Order
from reportlab.pdfgen import canvas
import io

order_bp = Blueprint('order_bp', __name__)


# ==========================================
# GET ALL ORDERS
# ==========================================
@order_bp.route('/orders', methods=['GET'])
def get_orders():

    orders = Order.query.all()

    return jsonify([
        order.to_dict()
        for order in orders
    ])


# ==========================================
# GET SINGLE ORDER
# ==========================================
@order_bp.route('/orders/<int:id>', methods=['GET'])
def get_single_order(id):

    order = Order.query.get(id)

    if not order:

        return jsonify({

            "status": "error",

            "message": "Order not found"

        }), 404

    return jsonify(order.to_dict())


# ==========================================
# CREATE MULTIPLE ITEMS ORDER
# ==========================================
@order_bp.route('/orders', methods=['POST'])
def create_order():

    data = request.get_json()

    try:

        customer_name = data['customer_name']

        items = data['items']

        subtotal = float(data['total_price'])

        # GST 5%
        gst = subtotal * 0.05

        # FINAL TOTAL
        final_total = subtotal + gst

        # CREATE ORDER
        order = Order(

            customer_name=customer_name,

            items=items,

            total_price=final_total

        )

        db.session.add(order)

        db.session.commit()

        return jsonify({

            "status": "success",

            "message": "Final Order Created Successfully",

            "customer_name": customer_name,

            "items": items,

            "subtotal": subtotal,

            "gst": gst,

            "final_total": final_total

        })

    except Exception as e:

        return jsonify({

            "status": "error",

            "message": str(e)

        }), 500


# ==========================================
# DELETE ORDER
# ==========================================
@order_bp.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):

    order = Order.query.get(id)

    if not order:

        return jsonify({

            "status": "error",

            "message": "Order Not Found"

        }), 404

    db.session.delete(order)

    db.session.commit()

    return jsonify({

        "status": "success",

        "message": "Order Deleted Successfully"

    })


# ==========================================
# DOWNLOAD PDF INVOICE
# ==========================================
@order_bp.route('/download-invoice', methods=['POST'])
def download_invoice():

    data = request.get_json()

    customer = data['customer_name']

    items = data['items']

    subtotal = float(data['total_price'])

    gst = subtotal * 0.05

    final_total = subtotal + gst

    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)

    # TITLE
    p.setFont("Helvetica-Bold", 22)

    p.drawString(170, 800, "Restaurant Invoice")

    # LINE
    p.line(50, 780, 550, 780)

    # CUSTOMER DETAILS
    p.setFont("Helvetica", 14)

    p.drawString(50, 740, f"Customer Name : {customer}")

    p.drawString(50, 700, f"Ordered Items :")

    p.drawString(70, 670, f"{items}")

    p.drawString(50, 620, f"Subtotal : ₹{subtotal}")

    p.drawString(50, 580, f"GST (5%) : ₹{gst}")

    # FINAL TOTAL
    p.setFont("Helvetica-Bold", 16)

    p.drawString(50, 520, f"Final Total : ₹{final_total}")

    # THANK YOU
    p.setFont("Helvetica", 13)

    p.drawString(180, 430, "Thank You! Visit Again")

    p.save()

    buffer.seek(0)

    return send_file(

        buffer,

        as_attachment=True,

        download_name="invoice.pdf",

        mimetype="application/pdf"

    )


# ==========================================
# TOTAL SALES
# ==========================================
@order_bp.route('/orders/total-sales', methods=['GET'])
def total_sales():

    orders = Order.query.all()

    total = sum(order.total_price for order in orders)

    return jsonify({

        "total_sales": total

    })


# ==========================================
# TOTAL ORDERS COUNT
# ==========================================
@order_bp.route('/orders/count', methods=['GET'])
def orders_count():

    count = Order.query.count()

    return jsonify({

        "total_orders": count

    })


# ==========================================
# ORDER API STATUS
# ==========================================
@order_bp.route('/orders-status', methods=['GET'])
def orders_status():

    return jsonify({

        "status": "running",

        "message": "Orders API Working Successfully"

    })
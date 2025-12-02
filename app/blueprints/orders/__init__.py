from flask import Blueprint

orders_bp = Blueprint('orders_bp', __name__)

from app.blueprints.orders import routes
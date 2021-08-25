from flask import Blueprint
stock_bp = Blueprint('stock_bp',__name__)
from app.stock import routes
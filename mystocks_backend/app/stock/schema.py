from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from app.stock.models import stock
from app import db

class StockSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = stock
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    number = fields.String(required=True)
    price = fields.Float(required=True)
    buy_price = fields.Float(required=True)
    position = fields.Number(required=True)
    yest_price = fields.Float(required=True)
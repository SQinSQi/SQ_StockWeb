from app import db

class stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column(db.Integer,primary_key=True, auto_increment=True)
    number = db.Column(db.String(10))
    name = db.Column(db.String(10))
    price = db.Column(db.Float(10))
    position = db.Column(db.Integer)
    buy_price = db.Column(db.Float(10))
    yest_price = db.Column(db.Float(10))

    def __init__(self,number,name,price,position,buy_price,yest_price):
        self.name = name
        self.number = number
        self.price = price
        self.buy_price = buy_price
        self.position = position
        self.yest_price = yest_price

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self



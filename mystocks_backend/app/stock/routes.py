from flask import request
from app import db
from app.stock import stock_bp
from app.stock.models import stock
from app.stock.schema import StockSchema
from app.utils.responses import response_with
from app.utils import responses as resp

## 查询全部
@stock_bp.route('/',methods=['GET'])
def get_stocks():
    get_stocks = stock.query.all()
    stock_schema = StockSchema(many=True)
    stocks = stock_schema.dump(get_stocks)
    # resp.headers['Access-Control-Allow-Origin'] = '*' 
    return response_with(resp.SUCCESS_200,value={"stocks":stocks})

## 查询单个
@stock_bp.route('/<int:id>',methods=['GET'])
def get_stock_by_id(id):
    get_stock = stock.query.get_or_404(id)
    stock_schema = StockSchema()
    stock_by_id = stock_schema.dump(get_stock)
    # resp.headers['Access-Control-Allow-Origin'] = '*' 
    return response_with(resp.SUCCESS_200,value={"stock":stock_by_id})

## 新增
@stock_bp.route('/',methods=['POST'])
def create_stocks():
    data = request.get_json()
    stock_schema = StockSchema()
    stock_add = stock_schema.load(data)
    result = stock_schema.dump(stock_add.create())
    # resp.headers['Access-Control-Allow-Origin'] = '*' 
    return response_with(resp.SUCCESS_201,value={"stock":result})

## 更新
@stock_bp.route('/<int:id>',methods=['PUT'])
def update_stocks_by_id(id):
    data = request.get_json(force=True)
    get_stocks = stock.query.get_or_404(id)
    if data.get('number'):
        get_stocks.number = data['number']

    if data.get('name'):
        get_stocks.name = data['name']

    if data.get('price'):
        get_stocks.price = data['price']

    if data.get('buy_price'):
        get_stocks.buy_price = data['buy_price']

    if data.get('position'):
        get_stocks.position = data['position']

    db.session.add(get_stocks)
    db.session.commit()
    stocks_schema = StockSchema(only=['id','name','number','price','buy_price','position'])
    stocks = stocks_schema.dump(get_stocks)
    # resp.headers['Access-Control-Allow-Origin'] = '*' 
    return response_with(resp.SUCCESS_200,value={"name":stocks})

## 删除
@stock_bp.route('/<int:id>',methods=['DELETE'])
def delete_stock_by_id(id):
    get_stock = stock.query.get_or_404(id)
    db.session.delete(get_stock)
    db.session.commit()
    # resp.headers['Access-Control-Allow-Origin'] = '*' 
    return response_with(resp.SUCCESS_200)
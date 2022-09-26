import bson
from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson import ObjectId


def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = PyMongo(current_app).db    
    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)


def get_price(product_id):
    try:
        price = db.prices.find_one({"product_id": product_id})
        return price
    except Exception as e:
        return e


def update_price_db(product_id, price=None, currency_code=None):
    if price is None and currency_code is None:
        return
    elif price is not None and currency_code is None:
        response = db.prices.update_one(
            {"product_id": product_id},
            {"$set": {"value ": price}}
        )
    elif price is None and currency_code is not None:
        response = db.prices.update_one(
            {"product_id": product_id},
            {"$set": {"currency_code ": currency_code}}
        )
    # error handling
    return response


def create_price_db(product_id, price, currency_code='USD'):
    price = {'product_id': product_id, 'value': price, 'currency_code': currency_code}
    response = db.prices.insert_one(price)
    print(response)

    return response
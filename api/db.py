from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo


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


def update_price_db(product_id, data):
    filter = {'product_id': product_id}

    if "value" not in data.keys() and "currency_code" not in data.keys():
        return
    elif "value" in data.keys() and "currency_code" not in data.keys():
        update_set = {"$set": {"value": data["value"]}}
    elif "value" not in data.keys() and "currency_code" in data.keys():
        update_set = {"$set": {"currency_code": data["currency_code"]}}
    elif "value" in data.keys() and "currency_code" in data.keys():
        update_set = {"$set": {
            "value": data["value"],
            "currency_code": data["currency_code"]}}
    try:
        result = db.prices.update_one(filter, update_set)
        return result
    except Exception as e:
        print(str(e))
        return e

import logging
import os
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from pymongo.errors import DuplicateKeyError

from redskyclient import RedSkyClient
from db import get_price, update_price_db


app = Flask(__name__)

try:
    app.config["MONGO_URI"] = os.environ['MONGODB_CONNSTRING']
except KeyError:
    pass

redskyclient = RedSkyClient()


@app.errorhandler(404)
def resource_not_found(e):
    """
    An error-handler to ensure that 404 errors are returned as JSON.
    """
    return jsonify(error=str(e)), 404


@app.errorhandler(DuplicateKeyError)
def duplicate_resource_found(e):
    """
    An error-handler to ensure that MongoDB duplicate key errors are returned as JSON.
    """
    return jsonify(error=f"Duplicate key error."), 400


@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    try:
        response = redskyclient.get_product(id)
        product = response["data"]["product"]
        price = get_price(id)
        return jsonify(
                        {
                            "id": int(product["tcin"]),
                            "title": product["item"]['product_description']['title'],
                            "current_price": {
                                "value": price['value'],
                                "currency_code": price['currency_code']
                            }
                        },
                    ), 200
    except KeyError:
        if response['status_code'] == 404:
            return jsonify(error="Not Found"), 404


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify(hello='in there'), 200

# @app.route('/product/<int:id>', methods=['PUT'])
# def update_price(id):
#     try:
#         update_price_db(id, price=20.54)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400


# @app.route('/product/<int:id>/price', methods=['POST'])
# def create_price(id):
#     try:
#         create_price_db(id, price=20.54)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400

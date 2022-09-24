import os
from flask import Flask, jsonify
from flask_pymongo import PyMongo

from redskyclient import RedSkyClient


app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
mongo = PyMongo(app)

db = mongo.db
prices = db.prices
redskyclient = RedSkyClient()


@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    try:
        product = redskyclient.get_product(id)["data"]["product"]
        return jsonify(
                        {
                            "id": product["tcin"],
                            "title": product["item"]['product_description']['title'],
                            "current_price": {
                                "value": 13.49,
                                "currency_code": "USD"
                            }
                        },
                    ), 200
    except KeyError:
        return jsonify({"error": "Not Found"}), 404

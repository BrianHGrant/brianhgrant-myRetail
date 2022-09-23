from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.flask_db
prices = db.prices

@app.route('/product/<int:id>')
def get_product(id):
    return jsonify({'name':'Jimit',
                    'address': id}), 200
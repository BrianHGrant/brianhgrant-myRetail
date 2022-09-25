db = db.getSiblingDB("flaskdb");
db.prices.drop();

db.prices.insertMany([
    {
        "product_id": 54456119,
        "value": 20.59,
        "currency_code": "USD"
    },
    {
        "product_id": 13860428,
        "value": 13.59,
        "currency_code": "USD"
    },
    {
        "product_id": 13264003,
        "value": 28.59,
        "currency_code": "USD"
    },
    {
        "product_id": 12954218,
        "value": 99.59,
        "currency_code": "USD"
    },
]);
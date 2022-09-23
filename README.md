# brianhgrant-myRetail
Products API

Products API for MyRetail Store

## Methods

* GET `/products/{id}`  
params: id (int)  
return: product.json  

## Models

* Product  
    ```
    { 
        "id":1368,
        "name": "The Big",
        "current_price": {
	        "value": 13.49,
	        "currency_code": "USD"	
        }
    }
    ```
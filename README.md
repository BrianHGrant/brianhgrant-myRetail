# brianhgrant-myRetail

Products API for MyRetail Store

## About

API returns product and pricing info. Uses Flask(python) and MongoDB on backend. 

## To Run

This project contains a `docker-compose.yaml` file for running in a local development environment (including dev server + live reloading).

To run:

1. `cp` the `env.example` file to `.env` ie: `$ cp env.example .env`
2. run `docker-compose up`
3. To confim working cURL `/ping`:
    ```
    curl 'http://localhost:8000/ping'
    
    200 OK

    {
        "hello": "in there"
    }
    ```

## Methods

* GET `/products/{id}`  
params: id (int)  
return: product.json  

* PUT `/products/{id}`  
params: id (int)
body: {
    "value": (string)
    "currency_code": (string)
} 
return: product.json 

* GET `/ping`  
params: None
return: ping.json 

## Models

* Product  
    ```
    { 
        "id":<int>,
        "name": <string>
        "current_price": {
	        "value": <float>,
	        "currency_code": <string>
        }
    }
    ```
* Ping
    ```
    {
        "hello":"in there"
    }
    ```

## Testing

This repo includes integration testing via Postman Collections. These are run as part of docker-compose up via a Newman Docker Container.

## Postman Collection

This repo includes a Postman Collection that can be [imported to Postman](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/) or run via [Newman CLI](https://www.npmjs.com/package/newman)

You will want to use the `/postman/environments/MyRetailAPI.postman_environment.json` for running outside of Docker Compose environment to run the collection.
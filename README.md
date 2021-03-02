# Hackathon Repo: Shopping Cart 2018 Submission
A shopping cart API that allows you to create and post your own items and
then search through the items using various filters.

The entire application is contained in the `application.py` file

`test_application.py` runs a simple test of the API
 
# API documentation
The shopping cart API is described below. 

## Post an item on the shop
### Request
`POST /api/items`

URL:

    http://127.0.0.1:5000/api/

### Response
## Get a list of all the items created
### Request
`GET /api/items`

URL:
 
    http://127.0.0.1:5000/api/items

JSON input:
 
    {
      "id": 4,
      "name": "tshirt",
      "description": "oversized",
      "price": 5,
      "size": 2,
      "color": "red",
      "availability": "Yes"
    }

### Response
     
     HTTP/1.1" 200
     content-length: 150 
     content-type: application/json 
     date: Tue, 02 Mar 2021 08:00:13 GMT 
     server: Werkzeug/0.16.1 Python/3.9.2 

## Get items by their availability
### Request
`GET /api/items/availability/{availability}`

URL:

JSON input:

### Response

http status code:

JSON output:

## Get items of a specific color
### Request
`GET /api/items/color/{color}`

URL:

JSON input:

### Response

http status code:

JSON output:

## Delete items by their id
### Request
`DELETE /api/items/delete/{id}`

URL:

JSON input:

### Response

http status code:

JSON output:

## Get items by their id
### Request
`GET /api/items/id/{id}`

URL:

JSON input:

### Response

http status code:

JSON output:

## Get items by their name
### Request
`GET /api/items/name/{name}`

URL:

JSON input:

### Response

http status code:

JSON output:

## Change an item's description
### Request
`PATCH /api/items/patch/{id}/{new_description}`

URL:

JSON input:

### Response

http status code:

JSON output:

## Get items that are lower than a price
### Request
`GET /api/items/price/max/{max}`

URL:

JSON input:

### Response

http status code:

JSON output:

## Get items that are greater than a price
### Request
`GET /api/items/price/min/{min}`

URL:

JSON input:

### Response

http status code:

JSON output:

## Get items that are within a price range
### Request
`GET /api/items/price/range/{max}/{min}`

URL:

JSON input:

### Response

http status code:

JSON output:

## Get items that are exactly a price
### Request
`GET /api/items/price/{price}`

URL:

JSON input:

### Response

http status code:

JSON output:

## Get items of a certain size
### Request
`GET /api/items/size/{size}`

URL:

JSON input:

### Response

http status code:

JSON output:

## Get an 418 http status code: "I'm a teapot"
### Request
`GET /api/teapot`

URL:

JSON input:

### Response

http status code:

JSON output:

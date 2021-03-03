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

    http://127.0.0.1:5000/api/items
    
JSON input:

    { 
        \"name\": \"tshirt\", 
        \"description\": \"oversized\", 
        \"price\": 5, 
        \"size\": 2, 
        \"color\": \"red\", 
        \"availability\": \"True\"
    }

### Response
HTTP Status Code:

    HTTP/1.1" 200
    
JSON Output:

    content-length: 151 
    content-type: application/json 
    date: Wed, 03 Mar 2021 06:04:14 GMT 
    server: Werkzeug/0.16.1 Python/3.9.2 
    
    
    {
      "id": 1,
      "name": "tshirt",
      "description": "oversized",
      "price": 5,
      "size": 2,
      "color": "red",
      "availability": "True"
    }

## Get a list of all the items created

### Request
`GET /api/items`

URL:
 
    http://127.0.0.1:5000/api/items

JSON input:

### Response
HTTP Status Code:

     HTTP/1.1" 200

JSON Output:

     content-length: 191 
     content-type: application/json 
     date: Wed, 03 Mar 2021 06:15:58 GMT 
     server: Werkzeug/0.16.1 Python/3.9.2 
     
     [
      {
        "id": 1,
        "name": "tshirt",
        "description": "oversized",
        "price": 5,
        "size": 2,
        "color": "red",
        "availability": "True"
      }
    ] 

## Get items by their availability

### Request
`GET /api/items/availability/{availability}`

URL:

    http://127.0.0.1:5000/api/items/availability/True

JSON input:

### Response

http status code:

    HTTP/1.1" 200

JSON output:
    
    content-length: 191 
    content-type: application/json 
    date: Wed, 03 Mar 2021 06:18:49 GMT 
    server: Werkzeug/0.16.1 Python/3.9.2 
    
    [
      {
        "id": 1,
        "name": "tshirt",
        "description": "oversized",
        "price": 5,
        "size": 2,
        "color": "red",
        "availability": "True"
      }
    ]
    
## Get items of a specific color

### Request
`GET /api/items/color/{color}`

URL:

    "http://127.0.0.1:5000/api/items/color/red"

JSON input:

### Response

http status code:

    HTTP/1.1" 200

JSON output:

    content-length: 191 
    content-type: application/json 
    date: Wed, 03 Mar 2021 06:22:00 GMT 
    server: Werkzeug/0.16.1 Python/3.9.2 
    
    [
      {
        "id": 1,
        "name": "tshirt",
        "description": "oversized",
        "price": 5,
        "size": 2,
        "color": "red",
        "availability": "True"
      }
    ]
## Delete items by their id

### Request
`DELETE /api/items/delete/{id}`

URL:

    http://127.0.0.1:5000/api/items/delete/1
    
JSON input:

### Response

http status code:

    HTTP/1.1" 200

JSON output:

    content-length: 151 
    content-type: application/json 
    date: Wed, 03 Mar 2021 06:26:32 GMT 
    server: Werkzeug/0.16.1 Python/3.9.2 
     
    {
     "id": 1,
     "name": "tshirt",
     "description": "oversized",
     "price": 5,
     "size": 2,
     "color": "red",
     "availability": "True"
    }
## Get items by their id

### Request
`GET /api/items/id/{id}`

URL:

    http://127.0.0.1:5000/api/items/id/2

JSON input:

### Response

http status code:

    HTTP/1.1" 200

JSON output:

    content-length: 156 
    content-type: application/json  
    date: Wed, 03 Mar 2021 06:27:25 GMT 
    server: Werkzeug/0.16.1 Python/3.9.2 
     
    {
     "id": 2,
     "name": "jeans",
     "description": "straight fit",
     "price": 25,
     "size": 2,
     "color": "blue",
     "availability": "False"
    }
    
## Get items by their name

### Request
`GET /api/items/name/{name}`

URL:

    http://127.0.0.1:5000/api/items/name/jeans

JSON input:

    content-length: 196 
    content-type: application/json 
    date: Wed, 03 Mar 2021 06:29:49 GMT 
    server: Werkzeug/0.16.1 Python/3.9.2 
    
    [
      {
        "id": 2,
        "name": "jeans",
        "description": "straight fit",
        "price": 25,
        "size": 2,
        "color": "blue",
        "availability": "False"
      }
    ]

### Response

http status code:

    HTTP/1.1" 200

JSON output:

## Update an item's description

### Request
`PATCH /api/items/patch/{id}/{new_description}`

URL:

    http://127.0.0.1:5000/api/items/patch/2/skinny

JSON input:

### Response

http status code:

    HTTP/1.1" 200

JSON output:

    content-length: 150 
    content-type: application/json 
    date: Wed, 03 Mar 2021 06:44:58 GMT 
    server: Werkzeug/0.16.1 Python/3.9.2 
    
    {
      "id": 2,
      "name": "jeans",
      "description": "skinny",
      "price": 25,
      "size": 2,
      "color": "blue",
      "availability": "False"
    }
    
## Get items that are lower than a price

### Request
`GET /api/items/price/max/{max}`

URL:

    http://127.0.0.1:5000/api/items/price/max/20

JSON input:

    

### Response

http status code:

    HTTP/1.1" 200

JSON output:

## Get items that are greater than a price

### Request
`GET /api/items/price/min/{min}`

URL:

JSON input:

### Response

http status code:

    HTTP/1.1" 200

JSON output:

## Get items that are within a price range

### Request
`GET /api/items/price/range/{max}/{min}`

URL:

JSON input:

### Response

http status code:

    HTTP/1.1" 200

JSON output:

## Get items that are exactly a price
### Request
`GET /api/items/price/{price}`

URL:

JSON input:

### Response

http status code:

    HTTP/1.1" 200

JSON output:

## Get items of a certain size
### Request
`GET /api/items/size/{size}`

URL:

    http://127.0.0.1:5000/api/items/size/2

JSON input:

### Response

http status code:

    HTTP/1.1" 200

JSON output:

    content-length: 190 
    content-type: application/json 
    date: Wed, 03 Mar 2021 06:56:02 GMT 
    server: Werkzeug/0.16.1 Python/3.9.2 
    
    [
      {
        "id": 2,
        "name": "jeans",
        "description": "skinny",
        "price": 25,
        "size": 2,
        "color": "blue",
        "availability": "False"
      }
    ]
## Get an 418 http status code: "I'm a teapot"
### Request
`GET /api/teapot`

URL:

    http://127.0.0.1:5000/api/teapot
    
JSON input:

### Response

http status code:

    HTTP/1.1" 418
    
    Error: I'M A TEAPOT
    
JSON output:
    
    content-length: 5 
    content-type: application/json 
    date: Wed, 03 Mar 2021 06:58:26 GMT 
    server: Werkzeug/0.16.1 Python/3.9.2
     
    null
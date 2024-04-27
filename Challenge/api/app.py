from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec, Response
from flask import Flask, request, jsonify
from db import Database
import models

server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='SuperMarket')
spec.register(server)
db = Database('sqlite:///app.db')

@server.get('/products')
def get_product():
    return 'List Products'

@server.post('/products')
@spec.validate(body=models.ProductModel, resp=Response(HTTP_201=models.ProductModel))
def post_product():
    data = request.context.body.dict()
    product = models.Product(**data)
    print(product)
    db.session.add(product)
    db.session.commit()
    return data

server.run(host='0.0.0.0')
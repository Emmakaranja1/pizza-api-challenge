from flask import jsonify
from server.models import Pizza

def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([p.to_dict() for p in pizzas]), 200

def register_pizza_routes(app):
    app.add_url_rule('/pizzas', 'get_pizzas', get_pizzas, methods=['GET'])

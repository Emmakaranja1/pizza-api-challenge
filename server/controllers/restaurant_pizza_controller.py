from flask import jsonify, request, abort
from server.models import RestaurantPizza, Restaurant, Pizza
from server.database import db

def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    restaurant_id = data.get('restaurant_id')
    pizza_id = data.get('pizza_id')

    # Validation
    if not (1 <= price <= 30):
        abort(400, description="Price must be between 1 and 30")
    if not Restaurant.query.get(restaurant_id):
        abort(400, description="Invalid restaurant_id")
    if not Pizza.query.get(pizza_id):
        abort(400, description="Invalid pizza_id")

    rp = RestaurantPizza(price=price, restaurant_id=restaurant_id, pizza_id=pizza_id)
    db.session.add(rp)
    db.session.commit()
    return jsonify(rp.to_dict()), 201

def register_routes(app):
    app.add_url_rule('/restaurant_pizzas', 'create_restaurant_pizza', create_restaurant_pizza, methods=['POST'])

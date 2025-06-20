from flask import jsonify, request, abort
from server.models import Restaurant, RestaurantPizza
from server.database import db

def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants]), 200

def get_restaurant_with_pizzas(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        abort(404, description="Restaurant not found")
    pizzas = []
    for rp in restaurant.restaurant_pizzas:
        p = rp.pizza.to_dict()
        p['price'] = rp.price
        pizzas.append(p)
    data = restaurant.to_dict()
    data['pizzas'] = pizzas
    return jsonify(data), 200

def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        abort(404, description="Restaurant not found")
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204

def register_routes(app):
    app.add_url_rule('/restaurants', 'get_restaurants', get_restaurants, methods=['GET'])
    app.add_url_rule('/restaurants/int:<int:restaurant_id>', 'get_restaurant_with_pizzas', get_restaurant_with_pizzas, methods=['GET'])
    app.add_url_rule('/restaurants/int:<int:restaurant_id>', 'delete_restaurant', delete_restaurant, methods=['DELETE'])
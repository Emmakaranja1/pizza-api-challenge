from flask import Flask
from flask_migrate import Migrate
from server.database import db
from server.config import DATABASE_URL
from server.controllers import register_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register routes
    register_routes(app)

    return app

app = create_app()

# Initialize Flask-Migrate after app and db are ready
migrate = Migrate(app, db)





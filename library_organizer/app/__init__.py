from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db
from .routes import register_routes

def create_app():
    app = Flask(__name__)

    # Configure the app for SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Register routes
    register_routes(app)

    with app.app_context():
        db.create_all()  # Ensure tables are created

    return app

from flask import Flask
from flask_cors import CORS
from backend.extensions.db import db
def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS

    # Configure your Flask app for development, production, etc.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/betting_model'  # Or another database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .routes.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
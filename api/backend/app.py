from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from api.backend.config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS
    CORS(app, resources={r"/*": {"origins": ["https://project-4v2b.vercel.app", "http://localhost:5174"]}}, supports_credentials=True)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from backend.routes.authRoutes import auth
    app.register_blueprint(auth)

    return app

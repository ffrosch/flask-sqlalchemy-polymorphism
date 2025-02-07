import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from app import models  # Import models here to avoid circular imports

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        if not database_exists(db.engine.url):
            create_database(db.engine.url)

        db.create_all()  # Create all tables

        # Inserts employee test data if no Employees exist
        from app.test_data import insert_employees

        insert_employees(db)

    # define the shell context
    @app.shell_context_processor
    def shell_context():  # pragma: no cover
        ctx = {"db": db}
        for attr in dir(models):
            model = getattr(models, attr)
            if hasattr(model, "__bases__") and db.Model in getattr(model, "__bases__"):
                ctx[attr] = model
        return ctx

    @app.route("/")
    def index():
        return "Hello, Flask with PostGIS!"

    return app

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
        heading = "<h1>Polymorphism with Flask-SQLAlchemy</h1>"
        users = models.User.query.all()
        if users:
            return heading + "<table><tr><th>ID</th><th>Type</th><th>Account ID</th><th>Email</th></tr>" + "".join(
                f"<tr><td>{user.id}</td><td>{user.type}</td><td>{user.account_id if hasattr(user, 'account_id') else ''}</td><td>{user.email if hasattr(user, 'email') else ''}</td></tr>"
                for user in users) + "</table>"
        return heading + "No users available"

    return app

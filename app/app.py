import os

from flask import Flask, render_template
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
    def shell_context():
        from app.test_data import insert_users

        ctx = {"db": db, "insert_users": insert_users}
        for attr in dir(models):
            model = getattr(models, attr)
            if hasattr(model, "__bases__") and db.Model in getattr(model, "__bases__"):
                ctx[attr] = model

        return ctx

    @app.route("/")
    def index():
        users_table_query = db.session.execute(
            db.select(models.User.__table__)
        ).fetchall()
        users = models.User.query.all()
        registered_users = models.RegisteredUser.query.all()
        unregistered_users = models.UnregisteredUser.query.all()
        accounts = models.Account.query.all()

        return render_template(
            "index.html",
            users=users,
            registered_users=registered_users,
            unregistered_users=unregistered_users,
            accounts=accounts,
            users_table_query=users_table_query,
        )

    return app

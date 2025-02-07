from sqlalchemy.orm import Mapped, mapped_column
from app.app import db


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]

    __mapper_args__ = {
        "polymorphic_on": "type",
        # Uncomment this to allow the use of the "User" model, too!
        # "polymorphic_identity": "user",
    }


class RegisteredUser(User):
    account_id: Mapped[int] = mapped_column(nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "account",
    }


class UnregisteredUser(User):
    email: Mapped[str] = mapped_column(nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "no_account",
    }

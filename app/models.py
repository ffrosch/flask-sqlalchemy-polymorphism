from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.app import db


class Account(db.Model):
    __tablename__ = "account"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)

    registered_user: Mapped[RegisteredUser] = relationship(back_populates="account")


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
    account_id: Mapped[int] = mapped_column(db.ForeignKey(Account.id), nullable=True)

    account: Mapped[Account] = relationship(
        back_populates="registered_user",
        single_parent=True,
        cascade="all, delete-orphan",
    )

    @property
    def email(self):
        return self.account.email

    __mapper_args__ = {
        "polymorphic_identity": "account",
    }


class UnregisteredUser(User):
    email: Mapped[str] = mapped_column(nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "no_account",
    }

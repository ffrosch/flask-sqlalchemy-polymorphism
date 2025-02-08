from app.models import RegisteredUser, UnregisteredUser, User, Account


def insert_users(db):
    if not db.session.query(User).first():
        try:
            # Create users
            for i in range(5):
                account = Account(email=f"user{i + 1}@example.com")
                user = RegisteredUser(account=account)
                db.session.add(user)

            for i in range(5, 10):
                user = UnregisteredUser(email=f"user{i + 1}@example.com")
                db.session.add(user)

            # Uncomment "polymorphic_identity" of "User" to allow the use of the "User" model, too!
            # users.append(
            #     User()
            # )

            # This will lead to an error when querying data if "no polymorphic identity 'user' is defined"
            # users.append(
            #     User(
            #         type="user"
            #     )
            # )

            # Add and commit to the session
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

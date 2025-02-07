from app.models import RegisteredUser, UnregisteredUser, User


def insert_users(db):
    if not db.session.query(User).first():
        # Create users
        users = []
        for i in range(5):
            users.append(
                RegisteredUser(
                    account_id=i + 1,
                )
            )
            users.append(
                UnregisteredUser(
                    email=f"user{i + 1}@example.com",
                )
            )

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
        db.session.bulk_save_objects(users)
        db.session.commit()

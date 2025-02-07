# Single-Model Polymorphism with Flask-SQLAlchemy

This is a simple example of how to use single-model polymorphism with Flask-SQLAlchemy.

## Setup

Clone this repository and run `docker compose up` to start the database.

At [http://127.0.0.1:5000/] you should now see a message like "No users available".

Now add some users to the database:

```shell
docker compose exec app /bin/bash -c "flask shell -c 'from app.test_data import insert_users; insert_users(db)'"
```

Go to [http://127.0.0.1:5000/] again to see a list of users.

# Single-Model Polymorphism with Flask-SQLAlchemy

This is a simple example of how to use single-model polymorphism with Flask-SQLAlchemy.

## Setup

Clone this repository and run `docker compose up` to start the database.

At http://127.0.0.1:5000/ you should now see a message like "No users available".

Now add some users to the database:

```shell
docker compose exec app /bin/bash -c "flask shell -c 'insert_users(db)'"
```

Go to http://127.0.0.1:5000/ again to see a list of users.


## Further Exploration

Open an Flask Shell with IPython that has access to all models and play around:

```shell
docker compose exec app /bin/bash -c "flask shell"
```

## Documentation

- [Single-Table Polymorphic Inheritance in SQLAlchemy (Example)](https://docs.sqlalchemy.org/en/20/_modules/examples/inheritance/single.html)

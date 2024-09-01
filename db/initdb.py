import os
from db.db import db  # Import the centralized db instance

books_db_path = os.path.join("db", "databases", "booksdb", "books.db")

def init_db(app):  # Pass the app to the function
    os.makedirs(os.path.dirname(books_db_path), exist_ok=True)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///default.db"  # Adjust if necessary
    app.config["SQLALCHEMY_BINDS"] = {
        "books": "sqlite:///../db/databases/booksdb/books.db",
        "corpura": "sqlite:///../db/databases/corpura/corpura.db",
    }

    db.init_app(app)  # Initialize db with app

    with app.app_context():
        db.create_all()  # Create all tables
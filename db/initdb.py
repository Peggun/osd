from flask_sqlalchemy import SQLAlchemy

import os

books_db_path = os.path.join('db', 'databases', 'booksdb', 'books.db')

db = None

def init_db(): # Does what the name says.
    from src.app.website import app

    os.makedirs(os.path.dirname(books_db_path), exist_ok=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///default.db' # This works fine.

    app.config['SQLALCHEMY_BINDS'] = {'books': 'sqlite:///../db/databases/booksdb/books.db'}

    db = SQLAlchemy(app)

    with app.app_context(): # You need this with statement or program will crash.
        db.create_all() 

    return db
from flask_sqlalchemy import SQLAlchemy

import os

books_db_path = os.path.join('db', 'databases', 'booksdb', 'books.db')

db = None

def init_db():
    from src.app.website import app

    os.makedirs(os.path.dirname(books_db_path), exist_ok=True)

    app.config['SQLALCHEMY_BINDS'] = {
        'books': f'sqlite:///db/databases/booksdb'
    }
    
    print(app.config['SQLALCHEMY_BINDS']) # For seeing why the database is throwing errors. I plan to use binds to manage multiple databases

    db = SQLAlchemy(app)

    with app.app_context():
        db.create_all()

    return db
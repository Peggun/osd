from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

books_db_path = os.path.join(os.getcwd(), 'db', 'databases', 'books')

db = None

def init_db():
    from src.app.website import app

    db = SQLAlchemy(app)

    app.config['SQLALCHEMY_BINDS'] = {
        'books': 'sqlite:///{books_db_path}books.db'
    }

    app.config['SQLALCHEMY_BINDS']['books'] = f'sqlite:///{books_db_path}'
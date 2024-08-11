import os 
from db.initdb import db, books_db_path
from db.models import book_model
from bs4 import BeautifulSoup

books_file_path = "../../src/data/books"
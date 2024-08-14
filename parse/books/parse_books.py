import os
from db import db
from bs4 import BeautifulSoup

books_file_path = "../../src/data/books"

def parse_books():
    for (root, dirs, files) in os.walk(books_file_path):
        print(files)

parse_books()
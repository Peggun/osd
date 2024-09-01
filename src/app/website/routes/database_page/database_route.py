from flask import Blueprint, render_template, request, jsonify
from db.models.book_model import Book
from db.models.corpus_model import Corpus
from db.db import db  # Ensure this is the correct import for the SQLAlchemy instance

database = Blueprint("database", __name__)

@database.route('/database')
def database_page():
    return render_template('database_page/html/html-database-page.html')

@database.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()
    results = []
    print(f"Search query: {query}")  # Debugging output

    if query:
        try:
            print("Querying Book model...")  # Debugging output
            db1_results = Book.query.filter(Book.title.ilike(f'%{query}%')).all()
            print(f"Book results: {db1_results}")  # Debugging output

            print("Querying Corpus model...")  # Debugging output
            db2_results = Corpus.query.filter(Corpus.name.ilike(f'%{query}%')).all()
            print(f"Corpus results: {db2_results}")  # Debugging output

            results = [
                {'title': item.title} for item in db1_results
            ] + [
                {'name': item.name} for item in db2_results
            ]
        except Exception as e:
            print(f"Error during search: {e}")
            return jsonify({'error': 'Search failed'}), 500

    return jsonify(results)


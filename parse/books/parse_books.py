import os
import sys
import time
import re
from sqlalchemy.exc import OperationalError

# NOTE: Remove the <br> header from the authors in the html files and add support for parsing html files that are suitable if they have not text file in their folder.

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) # Adds all of the root paths to the system path so that it recognise local packages.

from db.models.book_model import Book
from run import db, app
from logger.logger import Logger, LogLevels

books_file_path = "../../src/data/books"

def parse_into_db(results):

    Logger.log("Starting parsing...", LogLevels.INFO)

    with app.app_context():
        try:
            books_in_db = Book.query.all()
        except OperationalError as e:  # If the database table is empty or doesn't exist.
            Logger.log(f"OperationalError occurred: {str(e)}", LogLevels.ERROR)
            db.create_all()
            books_in_db = []

        for book in results:

            if book["to_parse"] == False:
                continue

            Logger.log(f"Parsing {book} into database...", LogLevels.DEBUG)

            if book["author"] is None or book["title"] is None:
                continue

            # Check if the book is already in the database
            book_exists = any(db_book.title == book["title"] for db_book in books_in_db)

            

            if book_exists:
                Logger.log(f"Book title '{book['title']}' already in the database.", LogLevels.INFO)
            else:
                book_to_add = Book(
                    id=len(books_in_db) + 1,
                    title=book["title"],
                    author=book["author"],
                    file_path=book["file_path"]
                )

                # Add the new book to the database
                db.session.add(book_to_add)
                db.session.commit()
                Logger.log(f"Book title '{book['title']}' added to the database.", LogLevels.INFO)

                books_in_db = Book.query.all()

# Function scans through the directory and finds suitable files for parsing.
def scan_directory(directory, search_terms):
    results = []
    file_count = 0

    num_of_txt_files = 0
    num_of_html_files = 0

    num_of_txt_files_with_term = 0
    num_of_html_files_with_term = 0

    files_with_both_terms = 0
    files_without_any_term = 0
    files_with_either_term = 0

    start_time = time.time()

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_count += 1
            file_path = os.path.join(root, file)
            Logger.log(f"Scanning {file_path}...", LogLevels.DEBUG)
            
            if file_path.endswith('.txt'):
                num_of_txt_files += 1
                lines_to_scan = 15
            elif file_path.endswith('.html'):
                num_of_html_files += 1
                lines_to_scan = 100
            else:
                continue  # Skip non-txt and non-html files

            # Strip any trailing "h" from the book name before determining the folder
            if file_path.endswith('h.txt'):
                to_parse = False
            elif file_path.endswith('h.html'):
                to_parse = False
            else:
                to_parse = True

            term_instances = []
            instance_count = 0
            terms_found = 0
            author_count = 0
            title_count = 0

            author = None
            title = None

            try:
                with open(file_path, 'r', errors='ignore') as f:
                    for i, line in enumerate(f):
                        if i >= lines_to_scan:
                            break
                        for term in search_terms:
                            if line.strip().startswith(term):
                                terms_found += 1
                                instance_count += 1
                                term_instances.append(i + 1)
                                
                                # Count the specific term occurrences
                                if term == 'Author':
                                    author_count += 1
                                    author_raw = line.split(':', 1)[1].strip() if ':' in line else None
                                    # Clean up the author name
                                    if author_raw:
                                        # Remove anything inside brackets and trailing commas
                                        author = re.sub(r'\s*\([^)]*\)', '', author_raw).rstrip(',').strip()
                                        author = author.split(',')[0].strip()
                                elif term == 'Title':
                                    title_count += 1
                                    title = line.split(':', 1)[1].strip() if ':' in line else None

                                # Break to stop searching for other terms if one is found
                                break
                    
                    if instance_count > 0:
                        results.append({
                            "file_path": file_path,
                            "line_numbers": term_instances,
                            "instance_count": instance_count,
                            "exactly_one_instance_each": author_count == 1 and title_count == 1,
                            "author": author,
                            "title": title,
                            "to_parse": to_parse
                        })
                        if file_path.endswith('.txt'):
                            num_of_txt_files_with_term += 1
                        elif file_path.endswith('.html'):
                            num_of_html_files_with_term += 1

                    if terms_found == len(search_terms):
                        files_with_both_terms += 1
                    if terms_found > 0:  # If any of the terms were found
                        files_with_either_term += 1
                    elif terms_found == 0:
                        files_without_any_term += 1

            except (IOError, UnicodeDecodeError) as e:
                print(f"Could not read {file_path}: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time

    parse_into_db(results)

    return results, file_count, elapsed_time, num_of_txt_files, num_of_html_files, num_of_txt_files_with_term, num_of_html_files_with_term, files_with_both_terms, files_without_any_term, files_with_either_term

if __name__ == "__main__":
    directory_to_scan = '../../src/data/books'
    search_terms = ['Author', 'Title']  # Searching for these terms
    
    Logger.log("Starting file scan...", LogLevels.INFO)

    found_files, file_count, elapsed_time, num_of_txt_files, num_of_html_files, num_of_txt_files_with_term, num_of_html_files_with_term, files_with_both_terms, files_without_any_term, files_with_either_term = scan_directory(directory_to_scan, search_terms)

    files_with_either_term = files_with_either_term - files_with_both_terms

    if found_files:
        print("\nSearch terms found in the following files:")
        for file_info in found_files:
            print(f"File: {file_info['file_path']}")
            print(f"  Instances: {file_info['instance_count']}")
            print(f"  Line Numbers: {file_info['line_numbers']}")
            if file_info['exactly_one_instance_each']:
                print(f"  Note: This file has exactly one 'Author' and one 'Title' instance.")
            if file_info.get('author'):
                print(f"  Author: {file_info['author']}")
            if file_info.get('title'):
                print(f"  Title: {file_info['title']}")
    else:
        print("\nSearch terms not found in any files.")

    Logger.log(f"\nNumber of files scanned: {file_count}", LogLevels.DEBUG)
    Logger.log(f"Time taken: {elapsed_time:.2f} seconds", LogLevels.DEBUG)
    Logger.log(f"Number of files found with specified search term: {len(found_files)}", LogLevels.DEBUG)
    Logger.log(f"Number of text files: {num_of_txt_files}", LogLevels.DEBUG)
    Logger.log(f"Number of html files: {num_of_html_files}", LogLevels.DEBUG)
    Logger.log(f"Number of text files with term: {num_of_txt_files_with_term}", LogLevels.DEBUG)
    Logger.log(f"Number of html files with term: {num_of_html_files_with_term}", LogLevels.DEBUG)
    Logger.log(f"Number of files with both 'Author' and 'Title': {files_with_both_terms}", LogLevels.DEBUG)
    Logger.log(f"Number of files with either 'Author' or 'Title': {files_with_either_term}", LogLevels.DEBUG)
    Logger.log(f"Number of files without 'Author' or 'Title': {files_without_any_term}", LogLevels.DEBUG)
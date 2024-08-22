import os
import sys
import time
import re
import concurrent.futures
from sqlalchemy.exc import OperationalError
import multiprocessing
from inscriptis import get_text

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from db.models.book_model import Book
from run import db, app
from logger.logger import Logger, LogLevels

books_file_path = "../../src/data/books"


def parse_into_db(results):

    Logger.log("Starting parsing for book dataset...", LogLevels.INFO)

    with app.app_context():
        try:
            books_in_db = Book.query.all()
        except OperationalError as e:
            Logger.log(f"OperationalError occurred: {str(e)}", LogLevels.ERROR)
            db.create_all()
            books_in_db = []

        for book in results:
            if not book["to_parse"]:
                continue

            Logger.log(f"Parsing {book} into database...", LogLevels.DEBUG)

            if book["author"] is None or book["title"] is None:
                continue

            book_exists = any(db_book.title == book["title"] for db_book in books_in_db)

            if book_exists:
                Logger.log(
                    f"Book title '{book['title']}' already in the database.",
                    LogLevels.INFO,
                )
            else:
                book_to_add = Book(
                    id=len(books_in_db) + 1,
                    title=book["title"],
                    author=book["author"],
                    file_path=book["file_path"],
                )

                db.session.add(book_to_add)
                db.session.commit()
                Logger.log(
                    f"Book title '{book['title']}' added to the database.",
                    LogLevels.INFO,
                )

                books_in_db = Book.query.all()


def scan_file(file_path, search_terms):
    Logger.log(f"Scanning {file_path}...", LogLevels.DEBUG)

    to_parse = True
    is_html = file_path.endswith(".html")

    if file_path.endswith(".txt"):
        lines_to_scan = 15
    elif is_html:
        lines_to_scan = 100

        # Determine the path of the corresponding .txt file
        if file_path.endswith("h.html"):
            txt_file_path = file_path.split("h.html")[0].strip() + ".txt"
        else:
            txt_file_path = file_path.split(".html")[0].strip() + ".txt"

        # If the .txt file doesn't exist, create it by converting HTML to plain text
        if not os.path.exists(txt_file_path):
            with open(file_path, "r", errors="ignore") as f:
                html_content = f.read()
                text_content = get_text(html_content)

            with open(txt_file_path, "w", errors="ignore") as txt_file:
                txt_file.write(text_content)

            Logger.log(f"Created {txt_file_path} from {file_path}", LogLevels.INFO)
        else:
            to_parse = False
    else:
        return None

    term_instances = []
    instance_count = 0
    author_count = 0
    title_count = 0

    author = None
    title = None

    try:
        with open(file_path, "r", errors="ignore") as f:
            for i, line in enumerate(f):
                if i >= lines_to_scan:
                    break
                for term in search_terms:
                    if line.strip().startswith(term):
                        instance_count += 1
                        term_instances.append(i + 1)

                        if term == "Author":
                            author_count += 1
                            author_raw = (
                                line.split(":", 1)[1].strip() if ":" in line else None
                            )
                            if author_raw:
                                author = (
                                    re.sub(r"\s*\([^)]*\)", "", author_raw)
                                    .rstrip(",")
                                    .strip()
                                )
                                author = author.split(",")[0].strip()
                                author = author.split("<br>")[0].strip()

                        elif term == "Title":
                            title_count += 1
                            title_raw = (
                                line.split(":", 1)[1].strip() if ":" in line else None
                            )
                            if title_raw:
                                title = title_raw.split("<br>")[0].strip()

                        break

        if instance_count > 0:
            return {
                "file_path": file_path,
                "line_numbers": term_instances,
                "instance_count": instance_count,
                "exactly_one_instance_each": author_count == 1 and title_count == 1,
                "author": author,
                "title": title,
                "to_parse": to_parse,
            }
        else:
            Logger.log(
                f"No 'Author' or 'Title' found in {file_path}.", LogLevels.WARNING
            )

    except (IOError, UnicodeDecodeError) as e:
        Logger.log(f"Could not read {file_path}: {e}", LogLevels.ERROR)

    return None


def scan_directory(directory, search_terms):
    results = []
    file_count = 0

    num_cores = multiprocessing.cpu_count() * 2

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_cores) as executor:
        futures = []

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_count += 1
                file_path = os.path.join(root, file)
                futures.append(executor.submit(scan_file, file_path, search_terms))

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                results.append(result)

    parse_into_db(results)

    return results, file_count


if __name__ == "__main__":
    directory_to_scan = "../../src/data/books"
    search_terms = ["Author", "Title"]

    Logger.log("Starting file scan for book dataset...", LogLevels.INFO)

    start_time = time.time()

    results, file_count = scan_directory(directory_to_scan, search_terms)

    if results:
        Logger.log("\nSearch terms found in the following files:", LogLevels.DEBUG)
        for file_info in results:
            Logger.log(f"File: {file_info['file_path']}", LogLevels.DEBUG)
            Logger.log(f"  Instances: {file_info['instance_count']}", LogLevels.DEBUG)
            Logger.log(f"  Line Numbers: {file_info['line_numbers']}", LogLevels.DEBUG)
            if file_info["exactly_one_instance_each"]:
                Logger.log(
                    f"  Note: This file has exactly one 'Author' and one 'Title' instance.",
                    LogLevels.DEBUG,
                )
            if file_info.get("author"):
                Logger.log(f"  Author: {file_info['author']}", LogLevels.DEBUG)
            if file_info.get("title"):
                Logger.log(f"  Title: {file_info['title']}", LogLevels.DEBUG)
    else:
        Logger.log("\nSearch terms not found in any files.", LogLevels.WARNING)

    end_time = time.time()
    elapsed_time = end_time - start_time

    Logger.log(f"\nNumber of files scanned: {file_count}", LogLevels.DEBUG)
    Logger.log(f"Time taken: {elapsed_time:.2f} seconds", LogLevels.DEBUG)

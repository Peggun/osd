import os
import requests
from bs4 import BeautifulSoup
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import multiprocessing

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from logger.logger import Logger, LogLevels

# Downloads all of the ebooks stored at Project Gutenberg AU.


def download_book(book_link, book_file_paths, book_names, folder_counter_lock):
    try:
        book_name_ft = book_link.split("/")[-1]  # Extract the file name from the URL

        # Strip any trailing "h" from the book name before determining the folder
        if book_name_ft.endswith(".txt"):
            book_name = book_name_ft.split(".txt")[0].rstrip("h")
        elif book_name_ft.endswith(".html"):
            book_name = book_name_ft.split(".html")[0].rstrip("h")

        # Synchronize folder creation
        with folder_counter_lock:
            if book_name in book_names:
                folder_path = book_names[book_name]
            else:
                folder_path = os.path.join(
                    book_file_paths, f"book_{len(book_names) + 1}"
                )
                os.makedirs(folder_path, exist_ok=True)
                book_names[book_name] = folder_path

        # Define the file path within the folder
        file_path = os.path.join(folder_path, book_name_ft)

        # Check if the file already exists
        file_exists = os.path.exists(file_path)
        if not file_exists:
            request = requests.get(book_link)
            with open(file_path, "wb") as file:
                file.write(request.content)
            Logger.log(
                f"Downloaded '{book_name_ft}' to '{folder_path}' from {book_link}",
                LogLevels.DEBUG,
            )
        else:
            Logger.log(
                f"Skipped '{book_name_ft}' as it already exists.", LogLevels.DEBUG
            )
    except Exception as e:
        print(f"Failed to download {book_name_ft}. Error: {e}")


def download_books():
    book_file_paths = "../../src/data/books/"
    urls = [
        "https://gutenberg.net.au/ebooks/",
        "https://gutenberg.net.au/ebooks01/",
        "https://gutenberg.net.au/ebooks02/",
        "https://gutenberg.net.au/ebooks/03",
        "https://gutenberg.net.au/ebooks04/",
        "https://gutenberg.net.au/ebooks05/",
        "https://gutenberg.net.au/ebooks06/",
        "https://gutenberg.net.au/ebooks07/",
        "https://gutenberg.net.au/ebooks08/",
        "https://gutenberg.net.au/ebooks09/",
        "https://gutenberg.net.au/ebooks10/",
        "https://gutenberg.net.au/ebooks11/",
        "https://gutenberg.net.au/ebooks12/",
        "https://gutenberg.net.au/ebooks13/",
        "https://gutenberg.net.au/ebooks14/",
        "https://gutenberg.net.au/ebooks15/",
        "https://gutenberg.net.au/ebooks16/",
        "https://gutenberg.net.au/ebooks17/",
        "https://gutenberg.net.au/ebooks18/",
        "https://gutenberg.net.au/ebooks19/",
        "https://gutenberg.net.au/ebooks20/",
        "https://gutenberg.net.au/ebooks21/",
        "https://gutenberg.net.au/ebooks22/",
        "https://gutenberg.net.au/ebooks23/",
        "https://gutenberg.net.au/ebooks24/",
    ]

    links = []
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        for a in soup.find_all("a", href=True):
            if a["href"].endswith(".txt") or a["href"].endswith(".html"):
                links.append(url + a["href"])

    # Use a lock for synchronizing folder creation
    folder_counter_lock = threading.Lock()
    book_names = {}

    # Determine the optimal number of threads
    max_workers = (
        multiprocessing.cpu_count() * 2
    )  # Use double the CPU count for threads

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(
                download_book, link, book_file_paths, book_names, folder_counter_lock
            ): link
            for link in links
        }
        for future in as_completed(futures):
            link = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f"Error downloading {link}: {e}")


def compare_files(fp1, fp2):
    try:
        with open(fp1, "rb") as file1, open(fp2, "rb") as file2:
            while True:
                chunk1 = file1.read(4096)
                chunk2 = file2.read(4096)
                if chunk1 != chunk2:
                    return False
                if not chunk1:  # Both files have been read completely and are identical
                    return True
    except FileNotFoundError:
        return False


download_books()

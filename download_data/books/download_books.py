import os
import requests

def download_books():
    book_file_paths = '../../src/data/books/'

    for book_num in range(1, 70001):  # Corrected range to download books 1 to 10
        folder_path = os.path.join(book_file_paths, f"book_{book_num}")
        os.makedirs(folder_path, exist_ok=True)

        # Define the file path within the folder
        file_path = os.path.join(folder_path, f"book_{book_num}.txt")

        url = f"https://www.gutenberg.org/ebooks/{book_num}.txt.utf-8"

        # Download the book
        r = requests.get(url)

        # Save the downloaded content to the file
        with open(file_path, 'wb') as file:
            file.write(r.content)

download_books()

import os
import requests
from bs4 import BeautifulSoup

def download_books():
    book_file_paths = '../../src/data/books/'

    urls = [
        'https://gutenberg.net.au/ebooks/', 'https://gutenberg.net.au/ebooks01/', 'https://gutenberg.net.au/ebooks02/',
        'https://gutenberg.net.au/ebooks/03', 'https://gutenberg.net.au/ebooks04/', 'https://gutenberg.net.au/ebooks05/',
        'https://gutenberg.net.au/ebooks06/', 'https://gutenberg.net.au/ebooks07/', 'https://gutenberg.net.au/ebooks08/',
        'https://gutenberg.net.au/ebooks09/', 'https://gutenberg.net.au/ebooks10/', 'https://gutenberg.net.au/ebooks11/',
        'https://gutenberg.net.au/ebooks12/', 'https://gutenberg.net.au/ebooks13/', 'https://gutenberg.net.au/ebooks14/',
        'https://gutenberg.net.au/ebooks15/', 'https://gutenberg.net.au/ebooks16/', 'https://gutenberg.net.au/ebooks17/',
        'https://gutenberg.net.au/ebooks18/', 'https://gutenberg.net.au/ebooks19/', 'https://gutenberg.net.au/ebooks20/',
        'https://gutenberg.net.au/ebooks21/', 'https://gutenberg.net.au/ebooks22/', 'https://gutenberg.net.au/ebooks23/',
        'https://gutenberg.net.au/ebooks24/'
    ]

    folder_counter = 1
    links = []
    book_names = {}

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        # Collect all .txt and .html links
        for a in soup.find_all('a', href=True):
            if a['href'].endswith('.txt') or a['href'].endswith('.html'):
                links.append(url + a['href'])

        # Iterate over the links and download each book
        for book_link in links:
            book_name_ft = book_link.split('/')[-1]  # Extract the file name from the URL

            # Extract the book's base name (without extension)
            if book_name_ft.endswith('.txt'):
                book_name = book_name_ft.split('.txt')[0]
            elif book_name_ft.endswith('.html'):
                book_name = book_name_ft.split('.html')[0]

            # Check if the book name already exists in the dictionary
            if book_name in book_names:
                # If it exists, get the folder path for this book
                folder_path = book_names[book_name]
            else:
                # If not, create a new folder for this book
                folder_path = os.path.join(book_file_paths, f"book_{folder_counter}")
                os.makedirs(folder_path, exist_ok=True)
                book_names[book_name] = folder_path
                folder_counter += 1  # Increment the counter only when a new folder is created

            # Define the file path within the folder
            file_path = os.path.join(folder_path, book_name_ft)

            # Check if the file already exists and is identical
            file_exists = False
            if os.path.exists(file_path):
                file_exists = True
            else:
                # Check if any existing file in the folder is the same
                for existing_file in os.listdir(folder_path):
                    existing_file_path = os.path.join(folder_path, existing_file)
                    if compare_files(existing_file_path, file_path):
                        file_exists = True
                        print(f"Skipped downloading '{book_name_ft}' because an identical file already exists.")
                        break

            if not file_exists:
                try:
                    # Download the book file and save it to the file path
                    request = requests.get(book_link)
                    with open(file_path, 'wb') as file:
                        file.write(request.content)
                    print(f"Downloaded '{book_name_ft}' to '{folder_path}' from '{url}'")
                except Exception as e:
                    print(f"Failed to download {book_name_ft}. Error: {e}")

def compare_files(fp1, fp2):
    try:
        with open(fp1, 'rb') as file1, open(fp2, 'rb') as file2:
            while True:
                chunk1 = file1.read(4096)
                chunk2 = file2.read(4096)

                if chunk1 != chunk2:
                    return False
                if not chunk1:  # Both files have been read completely and are identical
                    return True

    except Exception as e:
        if e is FileNotFoundError:
            return False

download_books()
import os
#from db import db
from bs4 import BeautifulSoup

import os
import time

books_file_path = "../../src/data/books"

def parse_books():
    for (root, dirs, files) in os.walk(books_file_path):
        print(files)

# This function scans through every file and directory in the specified directory to find the file paths.
def scan_directory(directory, search_term):
    results = []
    file_count = 0

    num_of_txt_files = 0
    num_of_html_files = 0

    num_of_txt_files_with_term = 0
    num_of_html_files_with_term = 0

    start_time = time.time()

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_count += 1
            file_path = os.path.join(root, file)
            print(f"Scanning {file_path}")
            
            if file_path.endswith('.txt'):
                num_of_txt_files += 1
            elif file_path.endswith('.html'):
                num_of_html_files += 1

            try:
                with open(file_path, 'r', errors='ignore') as f:
                    for line in f:
                        if search_term in line:
                            if file_path.endswith('.txt'):
                                num_of_txt_files_with_term += 1
                            elif file_path.endswith('.html'):
                                num_of_html_files_with_term += 1
                            results.append(file_path)
                            break  # If you only need to know that the term is in the file
            except (IOError, UnicodeDecodeError) as e:
                print(f"Could not read {file_path}: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time

    return results, file_count, elapsed_time, num_of_txt_files, num_of_html_files, num_of_txt_files_with_term, num_of_html_files_with_term

if __name__ == "__main__":
    # Replace 'your_directory_path' with the path to the directory you want to scan
    directory_to_scan = '../../src/data/books'
    search_term = 'Author'  # Replace with the term you are searching for
    
    found_files, file_count, elapsed_time, num_of_txt_files, num_of_html_files, num_of_txt_files_with_term, num_of_html_files_with_term = scan_directory(directory_to_scan, search_term)

    if found_files:
        print("\nSearch term found in the following files:")
        for file in found_files:
            print(file)
    else:
        print("\nSearch term not found in any files.")

    print(f"\nNumber of files scanned: {file_count}")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Number of files found with specified search term: {len(found_files)}")
    print(f"Number of text files: {num_of_txt_files}")
    print(f"Number of html files: {num_of_html_files}")
    print(f"Number of text files with term: {num_of_txt_files_with_term}")
    print(f"Number of html files with term: {num_of_html_files_with_term}")
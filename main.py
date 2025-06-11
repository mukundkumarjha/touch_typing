import requests
import os
from rich import print

print("[bold red]Hello Reader!! Welcome[/bold red]")
print("⚠️ Disclaimer: This program  uses project gutenberg as ref so enter a book name avaliabel on this project")
book_name = input("Please enter book name:")


_cache = {}


def save_book(url, filename, subfolder="library"):
    current_dir = os.getcwd()
    folder_path = os.path.join(current_dir, subfolder)
    file_path = os.path.join(folder_path, filename)

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, "w", encoding= "utf-8") as f:
            f.write(response.text)
        _cache[filename] = 0
    else:
        print(f"Failed to download book! {response.status_code}")



def generate_text(book, ptr):






def find(book):
    if book in _cache:
        generate_text(book, _cache.get(book))
        return 
    query = book_name.replace(" ", "+")
    url = f"https://gutendex.com/books/?search={query}"
    response = requests.get(url)
    data = response.json()
    if data["count"] == 0:
        print("Book not found")
    else:
        book = data["results"][0]
        formats = book["formats"]
        book_url = formats.get('text/html')
        save_book(book_url, book_name)

find(book_name)

import json
import math

def convert_to_pages(text, page_limit=256):
    pages = []
    for i in range(0, len(text), page_limit):
        pages.append(text[i:i + page_limit])
    return pages

def save_to_json(book_title, author_name, pages):
    data = {
        "pools": [
            {
                "rolls": 1,
                "entries": [
                    {
                        "type": "item",
                        "weight": 1,
                        "name": "minecraft:written_book",
                        "functions": [
                            {
                                "function": "set_book_contents",
                                "title": book_title,
                                "author": author_name,
                                "pages": pages
                            }
                        ]
                    }
                ]
            }
        ]
    }
    with open(f'{book_title}.json', 'w') as f:
        json.dump(data, f, indent=2)

def main():
    book_title = input('Enter the book title: ')
    author_name = input('Enter the author name: ')
    book_text = input('Enter the book text (up to 12800 characters): ')

    pages = convert_to_pages(book_text, 256)
    save_to_json(book_title, author_name, pages)

    print(f'The book "{book_title}" has been saved as a JSON file.')

if __name__ == '__main__':
    main()

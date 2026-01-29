# Collect the list of books

book = []

def add_book(title, author):
    book.append({"title": {title}, "author": {author}, "available": True})


def get_book():
    return book
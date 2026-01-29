# Helper functions

def format_book(book):
    status = "Available" if book['available'] else "borrowed"
    return f"{book['title']} by {book['author']} - {status}"
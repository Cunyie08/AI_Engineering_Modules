# Print out
from my_data import data
from my_utils import helpers
from services import library

# Display the name of the books
data.add_book("Python", "Jane Doe")
data.add_book("English", "John Doe")

# Display all the books available
print("Library Collection")
for b in data.get_book():
    print(helpers.format_book(b))

# Borrow a book
print("\nBorrowing a book:")
print(library.borrow_book("Python"))


# Display books again
print("\nUpdated Library Collection")
for b in data.get_book():
    print(helpers.format_book(b))
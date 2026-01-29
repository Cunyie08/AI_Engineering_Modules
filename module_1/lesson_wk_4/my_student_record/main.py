# main.py
import data
import utils

# Add student info
data.add_students("Paul", "AI Engineering")
data.add_students("Kanyin", "AI Developer")

# Print the formatted student records
for s in data.get_students():
    print(utils.format_student(s))
# from pathlib import Path

# workspace = Path("workspace_files")
# workspace.mkdir(exist_ok=True)
# file_path = workspace / "notes.txt"
# file_path


# f = open(file_path, "w", encoding="utf-8")
# f.write("This is the first line in my notes.txt\n")
# f.close()

# workspace = Path("new_files")
# workspace.mkdir(exist_ok=True)
# file_path = workspace / "note.txt"
# file_path

# f = open(file_path, "w", encoding="utf-8")
# f.write("This is a testing file\n")
# f.close()

# f = open(workspace / "created_once.txt", "x", encoding="utf-8")
# f.write("Does this file exist")
# f.close

# f = open(file_path, "a", encoding="utf-8")
# f.write("This is an additional line")
# f.close()

# workspace = Path("my_journal")
# workspace.mkdir(exist_ok=True)
# file_path = workspace / "note.txt"
# file_path



# f = open(file_path, "w", encoding="utf-8")
# f.write("----My Journal----\n")
# f.write("Daily routine\n")
# f.write("Weekly routine\n")
# f.write("Monthly routine\n")
# f.close

# f = open(file_path, "a", encoding="utf-8")
# f.write("Yearly routine\n")
# f.write("Basics")
# f.close()

# f = open(file_path, "r", encoding="utf-8")
# content = f.read()
# f.close()
# print(content)

# f = open(file_path, "r", encoding="utf-8")
# content = f.read(45)
# f.close()
# print(content)

# f = open(file_path, "r", encoding="utf-8")
# print("First line:", f.readline().strip())
# print("Third line:", f.readline().strip())
# f.close()

# f = open(file_path, "r", encoding="utf-8")
# lines = f.readlines()
# f.close()
# print("Line list:", [line.rstrip() for line in lines]) # prints it as a list

# f = open(file_path, "r", encoding="utf-8")
# for line in f:
#     print("->", line.rstrip())
# f.close()

# # Using with open
# with open(file_path, "w", encoding="utf-8") as f:
#     f.write("My To do list:\n")
#     f.write("-> Code along\n")
#     f.write("-> Submit tasks\n")
#     f.write("-> push to git\n")



# with open(file_path, "a", encoding="utf-8") as f:
#     f.write("-> Say Alhamdulilah\n")


# from pathlib import Path

# workspace = Path("my_journal")
# workspace.mkdir(exist_ok=True)

# try:
#     with open(workspace / "missing.txt", "r") as f:
#         content = f.read()
#         print("File content:", content)
# except FileNotFoundError:
#     print("Sorry, file does not exist")
#     print("Lets create one first")
#     with open(workspace / "missing.txt", "w") as f:
#         f.write("file does exist now")
#         print("File created successfully")

# from pathlib import Path

# workspace = Path("my_journal")
# file_path = workspace / "notes.txt"

# # Checking if file exist
# if  file_path.exists():
#     print("File Found:", {file_path.name})

#     file_size = file_path.stat().st_size
#     print(f"File Size: {file_size} bytes")

#     with open(file_path, "r", encoding="utf-8") as f:
#         content = f.read()
#         print(f"Content preview: {content[::]}...")
# else:
#     print(f"File {file_path.name} does not exist")
#     print("Lets create it first")

# import json
# from pathlib import Path

# workspace = Path("new_files")

# # Create some student data (like a mini database)
# student_data = {
#     "name": "Oyindamola",
#     "age": 16,
#     "courses": ["Python", "Data Science", "Web Development"],
#     "grades": {"Python": "A", "Data Science": "B+", "Web Development": "A-"},
#     "is_graduated": False
# }

# # save the data to JSON file
# json_file = workspace / "student_data.json"
# with open(json_file, "w", encoding="utf-8") as f:
#     json.dump(student_data, f, indent=2)

# print("Student data saved to JSON file!")

# with open(json_file, "r", encoding="utf8") as f:
#     loaded_data = json.load(f)

# print("\nData read from JSON file:")
# print(f"Student name: {loaded_data['name']}")
# print(f"Age: {loaded_data['age']}")
# print(f"Courses: {', '.join(loaded_data['courses'])}")
# print(f"Python grade: {loaded_data['grades']['Python']}")

import csv
from pathlib import Path

workspace = Path("new_files")
csv_file = workspace / "students.csv"

students = [
    ["Name", "Age", "Course", "Grade"],  # Header row
    ["Precious", 20, "Python", "A"],
    ["Favour", 22, "JavaScript", "B+"],
    ["Ore", 21, "Python", "A-"],
    ["Susan", 23, "Data Science", "A"]
]

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)

print("Student data written to csv file!")

# Reading the csv file
print("\nReading the CSV file:")

with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row_number, row in enumerate(reader):
        if row_number == 0:
            print(f"Headers: {'|'.join(row)}")
            print("-" * 40)
        else:
            name, age, course, grade = row
            print(f"{name} ({age} years) - {course}: {grade}")


# from pathlib import Path

# workspace = Path("workspace_files")
# input_file = workspace / "original.txt"
# output_file = workspace / "processed.txt"


# sample_text = """Hi Fellas
# I am learning pyhton
# and it's quite interesting
# No challenges yet
# Ya Allah! please see me through
# """

# with open(input_file, "w", encoding="utf-8") as f:
#     f.write(sample_text)

# print("Created input file")

# with open(input_file, "r", encoding="utf-8") as infile, \
#      open(output_file, "w", encoding='utf-8') as outfile:
    
#     line_number = 1
#     for line in infile:
#         processed_line = f"Line {line_number}: {line.strip().upper()}\n"
#         outfile.write(processed_line)
#         line_number += 1


# print("File processing complete!")

# print("\nOriginal file:")
# with open(input_file, "r", encoding="utf-8") as f:
#     print(f.read())

# print("\nProcessed file:")
# with open(output_file, "r", encoding="utf-8") as f:
#     print(f.read())

# from pathlib import Path

# workspace = Path("workspace_files")
# file_path = workspace / "story.txt"

# story = """Once upon a time, there was a lady  who was very curious and inquisitive, 
# she just want to know how things work behind the scene. 
# Eventually she had an opportunity to hopp into the world of programming for the first time.
# She started with python, now she codes in Python every day.
# One day, she discovered file handling.
# It opened up a whole new world of possibilities!
# The end."""

# with open(file_path, "w", encoding="utf-8") as f:
#     f.write(story)

# print("Story file created")

# # Now lets explore moving around in the file
# with open(file_path, "r", encoding="utf-8") as f:
#     print("\nFile positioning demo:")

#     # Read first 20 characters
#     first_part = f.read(20)
#     print(f"First 20 characters: '{first_part}")

#     # Check your current position
#     current_postion = f.tell()
#     print(f"Current position in file: '{current_postion}")

#     # Jump to the beginning
#     f.seek(0)
#     print(f"After seeking to beginning: postion {f.tell()}")

#     # Jump to position 50 and read from there
#     f.seek(50)
#     rest_of_line = f.readline()
#     print(f"Reading from postion 50: '{rest_of_line.strip()}")

#     f.seek(0)
#     first_line = f.read()
#     print(f"First line: '{first_line.strip()}")
## Creating Dictionaries

# using curly braces
user_detail = {
    "name": "John",
    "age": "40",
    "gender": "Male",
    "program": "Data Science"
}
print(user_detail)

# Using dict constructor()
user_info = dict(name="Jane", age=25, gender= "Female", program= "Data Science")
print(user_info)

# Empty dictionary
empty_dict = {}
print(empty_dict)

## Dictionary Comprehension
# Syntax: {key_expression: value_expression for item in iterable if condition}

# Create a dictionary of numbers and their squares
squares = {x: x**2 for x in range(1,6)}
print(squares)

# With Condition - dict of even numbers and their cubes
evens_cube = {x: x**3 for x in range(1,15) if x %2 ==0}
print(evens_cube)

# From Existing Dictionary
students = {"Aisha": 56, "Kobe": 89, "Jane": 75}
passed_students = {name: score for name, score in students.items() if score >=60}
print(passed_students)

# Using strings Keys
names = {"Kayode", "Jay", "Tayo"}
lengths ={name: len(name) for name in names}
print(lengths)

## Accessing Dictionary Items
# Define a dictionary
student = {"name": "Jane", "age": 25, "gender": "Female", "program": "Data Science"}

# Using key
print(student["name"])

# Using get() method (avoids error if key is missing)
print(student.get("age"))
print(student.get("grade")) # returns not found


## Modifying Dictionaries


# 1. Using pop()
student = {"age": 25, "grade": "A", "program": "Data Science", "gender": "Female"}
student.pop("grade")
print(student)
# 2. Using popitem() - removes last inserted key-value
student.popitem()
print(student)
# 3. Using del keyword
del student["program"]
print(student)
# 4. Using clear() - removes all items
student.clear()
print(student)


## Dictionary methods using .keys(), .items(), .values() and .update()
user = {"name":"Jane", "age": 25,}

# Using keys 
print(user.keys())
# Using values()
print(user.values())
# Using items
print(user.items())
# Using update
print(user.update())


## Nested Dictionaires
user = {
    "user1": {"name":"Jane", "age": 25,},
    "user2": {"name":"John", "age": 28,},
}
print(user["user1"]["name"])
print(user["user2"]["age"])


## Looping through Dictionaries
# Define a dictionary
student = {"age": 25, "grade": "A", "program": "Data Science", "gender": "Female"}

# Loop through keys
for key in student:
    print(key)

# Loop though Values
for values in student.values():
    print(values)

# Loop thouh key-value-pair
for key, value in student.items():
    print(f"{key}: {value}")

# Storing a student's biodata
student = {
    "name": "Jane",
    "age": 22,
    "department": "sciences",
    "courses": ["Maths", "English", "Yoruba"],
    "is_full_time": True
}

print(f"Name: {student['name']}")
print(f"Age:{student['age']}")
print(f"courses: {'|'.join(student['courses'])}")

### How to add key-value pairs to an empty dictionary
# create an empty dictionary
student = {}

# Add key-value pairs to it
student["name"] = "Jane"
student["age"] = 20
student["hobbies"] = "Hiking"
print(student)


### List of dictionaries - each student has their own dictionary
student = [
    {"Name": "Jane", "Age": 25, "gender": "Female", "program": "Data Science"},
    {"Name": "John", "Age": 24, "gender": "Male", "program": "Data Analytics"},
    {"Name": "Mary", "Age": 21, "gender": "Female", "program": "Data Computing"},
]
print(student[0]["Name"])
print(student[-1]["program"])

### Dictionary of dictionaries - Each student is keyed by their ID 
student = {
"A002" : {"Name": "Jane", "Age": 25, "gender": "Female", "program": "Data Science"},
"A003" : {"Name": "John", "Age": 24, "gender": "Male", "program": "Data Analytics"},
"A004" : {"Name": "Mary", "Age": 21, "gender": "Female", "program": "Data Computing"},
}
print(student["A003"]["Age"])
print(student["A004"]["Name"])

### Dictionary of lists - Each course stores a list of scores
scores = {
    "Python": [69, 79, 90],
    "Git": [79, 75, 95],
    "NumPy": [88, 90, 95]
}
print(scores["Python"])
print(scores["NumPy"][-1])
print(scores["Git"][0])
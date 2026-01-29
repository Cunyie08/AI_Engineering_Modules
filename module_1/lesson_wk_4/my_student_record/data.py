# data.py
students = []

def add_students(name, track):
    students.append({"Name": name, "Track": track})


def get_students():
    return students
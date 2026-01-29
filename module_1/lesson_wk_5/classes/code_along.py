class Student:
    def __init__(self,name, course, level):
        print("Creating a new student profile")
        self.name = name
        self.course = course
        self.level = level
        print(f"Student {name} has been created")

kemi = Student("Kemi Ade", "Computer Science", 300)

class NigerianStudent:
    def __init__(self, name, state, course):
        print(f"Creating a Student object...")
        self.name = name
        self.state_of_orogin = state
        self.course = course
        self.student_id = self.generate_id()
        print(f"{name} is from {state}, studying {course}")

    def generate_id(self):
        import random
        return f"UNISAIL {random.randint(5000, 19999)}"
    
ayo = NigerianStudent("Ayo John", "Lagos", "Comp. Engr")
print(ayo.name)
print(ayo.student_id)

# Phone User

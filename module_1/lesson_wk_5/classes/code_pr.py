class newborn:
    def __init__(self, name, gender, weight, mother, complexion):
        self.name = name
        self.gender = gender
        self.weight = weight
        self.mother_name = mother
        self.complexion = complexion
        self.dob = self.generate_dob()
        print(f"""{mother} gave birth to a {gender}. Her name is {name}, 
She weighs {weight} and is {complexion} in complexion and was born {self.dob}""")

    def generate_dob(self):
        from datetime import datetime 
        return f"{datetime(2025, 8, 8).strftime("%m/%d/%Y")}"


        

baby = newborn("Baby Kay", "girl", "10lbs", "Mummy Kay", "fair")
print(baby)
print(baby.dob)

# Phone User
class phoneuser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{name} has phone number registered with {network}")

    def buy_airtime(self,amount):
        self.airtime += amount
        return f"{self.name} has successfully recharged N{self.airtime} on {self.network}"

# Create Multiple Users
ade = phoneuser("Ade Mike", "Airtel")
lilian = phoneuser("Lilian John", "Glo")

# Each person's account is credited with the amount purchased.
print(ade)
print(ade.buy_airtime(1000))
print(lilian.buy_airtime(2000))
print(ade.airtime)
print(lilian.airtime)


# Defining attributes of a student
class Student:
    def __init__(self, name, course, level, state_of_origin):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = 0.0
        print(f"{self.name} is a {self.level}l student studying {self.course}. She is from {self.state_of_origin}")
    
    def add_cgpa(self,gpa):
        self.cgpa += gpa
        return f"{self.name}'s CGPA for second semester is {self.cgpa}."
        
    

faith = Student("Faith Samuel", "Java", 200, "Osun State")
print(faith)
print(faith.course)
print(faith.level)
print(faith.state_of_origin)
print(faith.add_cgpa(4.7))




class Student:
    university = "University of Abuja"
    def __init__(self, name, course, level, state_of_origin):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.university = self.generate()
        print(f"{self.name} is studying {self.course}, she is in {self.level} at the {self.university}")

    def generate(self):
        return "University of Abuja"

student1 = Student("John Doe", "Mech. Engr.", 400, "Lagos State")
student2 = Student("Jane Daniel", "English", 100, "Plateau State")
student3 = Student("Ademide James", "Law", 300, "Ekiti State")

print(student1.name)
print(student2.name)
print(student3.name)

print(Student.university)
print(student1.university)
print(student2.university)
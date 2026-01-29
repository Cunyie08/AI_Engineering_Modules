# Ask the student for their name, age and score
#name = input("Enter your name: ")
#age = int(input("Enter your age: "))
#score = int(input("Enter your score: "))

# Check if the student is eligible for a scholarship
#eligibility = (age < 18) and (score > 70)
#print(f"Candidate: {name}\n Age: {age}\n Score: {score}\n Eligibility: {eligibility}")

# Explanation
print("""The code above is checking for eligibility. A student is eligible for scholarship
if he/she is younger or aged 18 with a requirement score of 70 or above. 
If the conditions are not met (False); the studenet is not eligible to apply. 
If the conditions are met (True); the studenet is eligible to apply for a scholarship.
""")

# Federal Government Scholarship 
# Ask for the student's details 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your score: "))
Nigerian =  "yes"
is_nigerian = Nigerian == True
citizenship = input("Are you from Nigeria: ")
Full_time = "yes"
is_full_time_UG = Full_time == True
Undergraduate_student = input("Are you a full time undergraduate student from a recognised Nigerian university: ")
other_scho = "no"
other_scholarship = other_scho == False
other_student_scho = input("Do you have a scholarship from any Oil and Gas Industry (local or international)?: ")
#resultA = "A"
#WASSCE_As = resultA == True
#resultB = "B"
#WASSCE_Bs = resultB == True
academic_subjects = input("Enter five subjects including Maths and English(separated by a comma): ").split()
academic_results= input("Enter the results of the above subject (separated by a comma): ").split()
academic_qualifications = ("A" in academic_results)
academic_qualifications1 = ("B" in academic_results)
academic_requirement = academic_qualifications == academic_qualifications1

eligibility = (age >= 18) and (score > 70) and (citizenship == is_nigerian) and (Undergraduate_student == is_full_time_UG) and (other_student_scho == other_scholarship) and (academic_requirement == academic_qualifications1 ) or (academic_requirement == academic_qualifications)
print(f"Candidate: {name}\n Age: {age}\n Score: {score}\n Citizenship: {citizenship:}\n"
f"Student program: {Undergraduate_student}\n Other Scholarships: {other_student_scho}\n"
f"Academic Qualification: {academic_qualifications}\n Eligibilty: {eligibility}")

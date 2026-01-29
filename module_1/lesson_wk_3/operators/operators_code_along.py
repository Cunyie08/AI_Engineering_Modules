# Comparison Operators
a = 10
b = 20
print(a==b) # False
print(a != b) # True
print(a > b) # False
print(a < b) # True
print(a >= 10) # True
print(b <= 25) # True

# Use case example-student exam result
score = 80
print(score >=50) # True (Passed)
print(score < 59) # False (Failed)
print(score == 100) # False (Not full marks)

# Assignment Operators
x = 10
print("Initial value:", x) # x = 10
x += 5
print("After x +=5:", x) # x = 10 + 5 = 15
x -= 3
print("After x -=3:", x) # x = 15 - 3 = 12  
x *= 3
print("After x *=3:", x) # x = 12 x 3 = 36
x /= 4
print("After x /= 4:", x) # x = 36/4 = 9
x %= 3
print("After x %= 3:", x) # x = 9/3 = 3.0 (returns remainder which is 0)
x = 10
x **= 2
print("After x **= 2:", x) # x = 10 raise to power 2)
x //= 3
print("After x //= 3:", x) # x = 100/3 = 33 (returns the whole number only i.e 33)

# Use case example:
# Define Varibales
balance = 1200
deposit = 300
withdraw = 500

balance += deposit # 1200 + 300 = 1500
balance -= withdraw # 1500 - 500 = 1000
print("Updated Balnce:", balance) 


## Logical Operators
x = 10
y = 20
# and operator
print(x < 15 and y > x) # returns True

# or operator
print(x > 5 or y > 15) # True

# not operator
print(not(x == 15)) # True because x = 10 not 15 
print(not(x == 10)) # False because x is equal to 10

# Use case Example 1 - Scholarship Eligibilty
# Define variables
age = 23
score = 89

# Must be older than 18 and score above 75
eligible = (age > 18) and (score < 90) 
print("Scholarship Eligible:", eligible) # True (all conditions are met)

# Use case Example 2 - Event Access
age = 24
has_ticket = False

can_enter = (age >= 23) and (has_ticket or age < 26)
print("Grant Access:", can_enter) # True because age is less than 26 even without tickets
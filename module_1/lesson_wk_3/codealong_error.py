## SYNTAX ERROR 
#  Indentation Error
#for i in range(3):
#print(i)

# Missing Colon/parenthesis Error
#if 5 > 3
#    print("Hey")

# Missing parenthesis
# print "Hello"

## RUNTIME ERRORS
# A. ZeroDivisionError
#x = 10 / 0

# B. NameError 
#print(age) # Age isn't defined

# C. TypeError
#result = "5" + 10

# D. ValueError
#number = int("abc")

# E. IndexError
#fruits = ["apples", "banana"]
#print(fruits[3])

# F. KeyError 
#data = {"name": "Ada"}
#print(data["age"])

# G. FileNotFoundError
#f = open("missing.txt")

# Handling Runtime Error
# A. try block
#try: 
#    x = 10 / 2
#    print("Result:", x)

# B. except block
#try: 
#    x = 10 / 0
#except ZeroDivisionError:
#    print("cannot divide by zero.")

#try:
#    number = int("abc")
#    result = 10 / 0
#except ValueError:
#    print("Invalid Conversion to int")
#
#except ZeroDivisionError:
#    print("Cannot Divide by Zero")

# C. finally block
#try:
#    f = open("sample.txt", "r")
#    content = f.read()
#except FileNotFoundError:
  #  print("File not found")
#finally:
#    print("Closing file if was opened.")


#balance = 10000 # starting balance

#print("Welcome to the ATM")
#amount = input("Enter amount to withdraw: ")

#try:
#    amount = float(amount)

#    if amount > balance:
#        raise ValueError("insufficient funds.")
    
#    balance -= amount
#    print("Withdrawal Successful. New Balance: N", balance)

#except ValueError as e:
#    print("Error", e)

#except Exception as e:
#    print("Unexpected error:", e)

#finally:
#    print("Transaction session closed.")

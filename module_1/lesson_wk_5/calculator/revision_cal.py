# Creating a basic calculator
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Error! Division by zero")
        
def exponent(a, b):
    return a ** b

def modulus(a, b):
    if b != 0:
        return a / b
    else:
        print("Error! Division by zero")
    
def square(a):
    if a <= 0:
        print("Square root of negative number")
    else:
        return math.sqrt(a)

# Print the functions of the Calculator
print("\n---Basic Calculator---")
print("\n1. Addition")
print("\n2. Subtraction")
print("\n3. Multiplication")
print("\n4. Division")
print("\n5. Exponent")
print("\n6. Modulus")
print("\n7. Squareroot")
print("\n8. Exit the program")





def main():
    while True:
        try:
            choice = input("Please select what you would like to do 1/2/3/4/5/6/7/8: ")
            if choice in ('1', '2', '3', '4', '5','6'):
                num1 = float(input("Please enter first number: "))
                num2 = float(input("Please enter a second number: "))
                print(num1,num2)
                if choice == '1':
                    print(f"The sum of {num1} and {num2} is {add(num1,num2)}")
                elif choice == '2':
                    print(f"Subtraction: {subtract(num1,num2)}")
                elif choice == '3':
                    print(f"Multiplication: {multiply(num1,num2)}")
                elif choice == '4':
                    print(f"Division: {division(num1,num2)}")
                elif choice == '5':
                    print(f"Exponential: {exponent(num1,num2)}")
                elif choice == '6':
                    print(f"Modulus: {modulus(num1,num2)}")
            elif choice == '7':
                num = float(input("Please enter a number: "))
                print(f"The Square root of {num} is {square(num)}")
            elif choice == '8':
                break
            else:
                raise ValueError("You have entered an invalid option")
            user = input("Do you want to perform another operation? yes or no: ").lower().strip()
            if user == 'yes':
                continue
            else:
                print("You have exited the program")
                break
        except ValueError as e:
            print(e)
        except Exception as e:
            print("Unexpected error", e)


if __name__ == "__main__":
    main()


import math

# Simple calculator program

def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b!=0:
        return a / b
    else: 
        return "Error Division by zero"
    
def modulus(a, b):
    if b!=0:
        return a % b
    else: 
        return "Error Division by zero"

def exponent(a, b):
    if b!=0:
        return a ** b

def squared(a):
    if a < 0:
        return "Error, cannot take square root of negative numbers"
    else:
        return math.sqrt(a)


# Display operations of the calculator
print("\n----Basic Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exponent")
print("7. Square root")
print("8. Exit program")


# Take input from the user for operation choice

def main():
    while True:
        try:
            choice = input("please enter a choice (1/2/3/4/5/6/7/8): ")
            if choice in ('1','2','3','4','5','6'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(num1,num2)
                if choice == '1':
                    print(f"The sum of {num1} and {num2}:", add(num1, num2))
                elif choice == '2':
                    print(f"{num1} - {num2}:", subtract(num1, num2))
                elif choice == '3':
                    print(f"{num1} x {num2}:", multiply(num1, num2))
                elif choice == '4':
                    print(f"{num1} / {num2}:", divide(num1, num2))
                elif choice == '5':
                    print(f"{num1} % {num2}", modulus(num1, num2))
                elif choice == '6':
                    print(f"{num1} ", exponent(num1, num2))
            elif choice == '7':
                num = float(input("Please enter a number: "))
                print("Result:", squared(num))
            elif choice == '8':
                break
            else:
                raise ValueError ("Invalid input")
            user = input("Do you want to perform another operation? Yes or No: ").lower().strip()
            if user == 'yes':
                continue
            else:
                print("You have exited the program")
                break
        except ValueError as e:
            print(e)
        # except Exception as e:
        #     print("Unexpected error:", e)

if __name__ == "__main__":
     main()


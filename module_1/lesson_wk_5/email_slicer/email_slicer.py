# Function to slice an email into username and domain
import re

def email_slicer(email):
    if "@" in email and '.' in email.split('@')[1]:
        username, domain = email.split('@')
        return username, domain
    else:
        return None, None

# Ask user to enter their email address

while True:
    try:
        email_format = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        email = input("PLease enter your email address: ")#.title().capitalize()
        if re.fullmatch(email_format, email):
            print("Valid format")
            username, domain = email_slicer(email)
            if username and domain:
                print(f"Username: {username}\nDomain: {domain}")
            else:
                print("Error!, You have entered an invalid email.")
                break
        else:
            print("Invalid format")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)



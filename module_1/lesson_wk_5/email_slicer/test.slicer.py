# import re

# def email_slicer(email):
#     if "@" in email and '.' in email.split('@')[1]:
#         username, domain = email.split('@')
#         return username, domain
#     else:
#         return None, None
    

# while True:
#     try:
#         email_format = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
#         email = input("Please enter a valid Email address: ")
#         if re.fullmatch(email_format, email):
#             print("valid email")
#             username, domain = email_slicer(email)
#             if username and domain:
#                 print(f"Username: {username}\nDomain: {domain}")
#             else:
#                 print("Error!, you have entered an invalid email")
#                 break
#         else:
#             print("Invalid Email")
#     except ValueError as e:
#         print(e)
#     except Exception:
#         print("Unexpected error", e)



import re

def email_slicer(email):
    if "@" in email and '.' in email.split('@')[1]:
        username, domain = email.split('@')
        return username, domain
    else:
        return None, None
    

while True:
    try:
        email_format = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        email = input("Please enter your email address: ")
        if re.fullmatch(email_format, email):
            print("Valid format")
            username, domain = email_slicer(email)
            if username and domain:
                print(f"Username: {username}\nDomain {domain}")
            else:
                print("You have entered an invalid email address")
        else:
            print("Invalid format")
            break
    except ValueError as e:
        print(e)
    except Exception:
        print("Unexpected error",e)
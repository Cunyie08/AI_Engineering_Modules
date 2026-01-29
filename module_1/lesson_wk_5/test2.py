class UserProfile:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender=""
        self.nin= 0
        self.farm_location = ""
        self.farm_size_sqm =""
        self.pin = 0

  
            
    def get_name(self):

        while True:
                try:
                    self.name = str(input("Please enter your name: ").strip())
                    if self.name == "":
                        raise ValueError("Invalid input!\n Enter a name")
                    elif self.name.isdigit()== True:
                      raise ValueError("Invalid input!\n Enter a name")
                    else:
                        return (self.name)  
                except ValueError as e:
                    print(e)
                except Exception as e:
                    print("Unexpected error:", e)
  

    def get_age(self):

        while True:
            try:
                self.age= int(input("Please enter your age: "))
                if self.age <= 0:
                    print("Age cannot be negative or zero")
                else:
                    return (self.age)
            except ValueError:
                print("Invalid input, input a number")
            except Exception as e:
                print("Unexpected error:", e)
            
    def get_nin(self):

        while True:
            try: 
                self.nin = input("Please enter your NIN: ")
                if (len(self.nin) != 11) :
                    raise ValueError("Invalid input! please enter 11 digits") 
                elif self.nin.isdigit() == False:
                    raise ValueError("Invalid input! please enter a number")
                elif self.nin.startswith("0"):
                    raise ValueError("Invalid input, Number can't starts with zero")
                else:
                        return (self.nin) 
            except ValueError as e:
                print(e)
            except Exception as e:
                print("Unexpected error:", e)
            
    def get_gender(self):

        while True:
            try:
                self.gender = str(input("Please enter your gender: ")).strip()
                if self.gender == "":
                    raise ValueError("Invalid input!\n Enter a gender")
                elif self.gender.isdigit()== True:
                     raise ValueError("Invalid input!\n Enter a gender")
                else:
                    return (self.gender)  
            except ValueError as e:
                print(e)
            except Exception as e:
                print("Unexpected error:", e)

    def get_farm_location(self):

        while True:
            try:
                self.farm_location = str(input("Please enter your farm_location: "))
                if (len(self.farm_location) == "") or (self.farm_location.isdigit()== True):
                    raise ValueError("Invalid input!\n Enter a farm_location")
                else:
                    return (self.farm_location)  
            except ValueError as e:
                print(e)
            except Exception as e:
                print("Unexpected error:", e)
            
    def get_farm_size_sqm(self):

        while True:
            try:
                self.farm_size_sqm= float(input("Please enter your farm size: "))
                if self.farm_size_sqm <= 0:
                    print("Your farm size cannot be negative or zero")
                else:
                    return (self.farm_size_sqm)
            except ValueError:
                print("Invalid input, input a number")
            except Exception as e:
                print("Unexpected error:", e)
    
    def new_pin(self):
        while True:
            try:
                new_pin =(input("Enter your four digit pin: "))
                if (len(self.pin)!= 4 and (self.pin.isdigit()== False)):
                    raise TypeError
                self.__pin += new_pin
                return self.pin

            except TypeError as t:
                print("Invalid input:", t)
        


    def get_user_details(self):
        farmer_info ={
            "Name": self.get_name(),
            "Age" : self.get_age(),
            "Gender": self.get_gender(),
            "NIN" : self.get_nin(),
            "Farm Location": self.get_farm_location(),
            "Farm Size" : self.get_farm_size_sqm()
        }

    # def display_profile(self):
    #     """Prints the user's profile details."""
    #     print(f"\nUser Profile:")
    #     print(f"Name: {self.name}")
    #     print(f"Age: {self.age}")



# Create an instance of the UserProfile class
my_profile = UserProfile()

# Call the method to get user details
# my_profile.get_user_details()

print(my_profile.get_user_details())

# Display the collected details
# my_profile.display_profile()            
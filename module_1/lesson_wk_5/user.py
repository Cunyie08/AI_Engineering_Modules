from abc import ABC, abstractmethod



class User(ABC):
    def __init__(self, name, age, gender,farm_location, farm_size,):
        self.name= name
        self.age = age
        self.gender= gender
        self.farm_location = farm_location
        self.farm_size_sqm = farm_size
        self.__pin = 0                  # Private attribute
        self.nin = []
        # self.validate_nin() = False

    def validate_nin(self):
        while True:
            try:
                collect_nin=int(input("Enter your nin:"))       
                if (len(collect_nin)!= 11):
                    raise ValueError ("Invalid input66")
                elif (collect_nin.isdigit() ==False):
                    raise ValueError ("Invalid input")
                elif collect_nin.startswith("0"):
                    raise ValueError("Invalid input, Number can't starts with zero")
                else:
                    self.nin.append(collect_nin)
                    if self.nin == True:
                        return f"{self.nin} has been succesfully validated"
            except ValueError as e:
                print(e)
            except Exception as e:
                print("Unexpected error", e)
    
    def new_pin(self):
        new_pin = int(input("Enter your four digit pin: "))
        self.__pin += new_pin
        return self.__pin

ade = User("Ade Mike",20, "Male", "Obada", 300)

print(ade.name)
print(ade.validate_nin())
print(ade.new_pin())



        
#     # Private method - only the class can use this``
    
#     def __verify_pin(self, entered_pin):
#         return entered_pin == self.__pin 

#     @abstractmethod
#     def reg_method(self):
#         pass
#     @abstractmethod
#     def pin_authentication(self):
#         pass
#     @abstractmethod
#     def               





# class Farmer(User):
#     def __init__(self, name, age, gender,farm_location, farm_size,):
#         self.name= name
#         self.age = age
#         self.gender= gender
#         self.farm_location = farm_location
#         self.farm_size_sqm = farm_size
        
# ade= User("Ade Mike",20, "Male",  "Obada", 300) 
# print(ade.validate_nin())                  


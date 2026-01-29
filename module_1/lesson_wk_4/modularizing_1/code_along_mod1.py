# #3 Python built-in functions

# # range()
# for i in range(4):
#     print(i) # 0 1 2 3 

# # zip()
# names = ["Dame", "Jim", "Tom" ]
# scores = [87, 80, 90]
# for n, s in zip(names, scores):
#     print(n, "scored", s) #Dame scored 87 # Jim scored 80 # Tom scored 90


# names = ["Kay", "Tay", "Jay"]
# programs = ["Eng.", "Dev", "Cyber"]
# ids = [0o02, 0o03, 0o04]
# for n, p, i in zip(names, programs, ids):
#     print(n, "with", i, "is studying", p) # Kay with 2 is studying Eng. # Tay with 3 is studying Dev. # Jay with 4 is studying Cyber


# # maps()
# nums = [1, 2, 3, 4,5]
# squared = list(map(lambda x: x**2, nums))
# print(squared) # [1, 4, 9, 16]

# # filter()
# odd_nums = list(filter(lambda x: x %3 == 0,nums))
# print(odd_nums)

# ## Store performance & Feedback system

# # Step 1: Input store details
# item1 = input("Enter the name of the item: ")
# price1 = int(input("Enter the cost of" + " " + item1 + ": "))

# item2 = input("Enter the name of the item: ")
# price2 = int(input("Enter the cost of" + " " + item2 + ": "))

# item3 = input("Enter the name of the item: ")
# price3 = int(input("Enter the cost of" + " " + item3 + ": "))

# # Step 2: Store input in a list
# items = [item1, item2, item3]
# prices = [price1, price2, price3]

# # Step 3: Display data
# print("\nStore Data:")
# for index, (i, p) in enumerate(zip(items, prices)):
#     print(f"{index + 1}. {i} - N{p}.00")

# # Step 4: Summarize using built-ins
# total_sales = sum(prices)
# average_sales = round(total_sales / len(prices), 2)
# highest_value = max(prices)
# lowest_value = min(prices)

# print("\nPerformance Sheet:")
# print("Total Sales:", total_sales)
# print("Average Sales:", average_sales)
# print("Top Sales:", highest_value)
# print("Low Sales:", lowest_value)

# # Step 5: Ranking (using sorted and zip)
# ranked = sorted(zip(items, prices), reverse=True)
# print("\nRanking:")
# for rank, (price, item) in enumerate(ranked, 1):
#     print(f"{rank}. {item} - {price}")


# # Step 6: Check data types
# print("\nData Type Checks:")
# print("Type of Items:", type(items))
# print("Type of Prices", type(prices))
# print("ID of Item list", id(items))
# print("ID of Price list", id(prices))

# # Step 7: Filter selling items (>=5000)
# selling_items = list(filter(lambda p: p >= 500000, prices))
# print("\nSelling Items:",selling_items)

# # Step 8: Map items to uppercase
# upper_items = list(map(lambda i: i.upper(), items))
# print("Uppercase:", upper_items)

# # Step 9 : Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)


## USER DEFINED FUNCTION

# # Defining a function
# def greet():
#     print("Hello, Welcome to NCC!.")

# greet()

# def meet():
#     print("Meeting is at 10pm!")

# greet(), meet()

# Function with an argument - the placeholder
# def greet(name):
#     print("Hello", name, "Welcome to NCC!.")

# # Calling with parameter - the actual name
# greet("Anna")
# greet("Sham")


## WHEN TO USE RETURN(), PRINT() AND YIELD() KEYWORDS INSIDE A FUNCTION

# # Print() - used to display your output not storing
# def greet(name):
#     print("Hello", name)

# # greet("ESTER") # Output - Hello Esther

# # Function call
# result = greet("Esther")
# print("Result:", result) # output - none

# # Return() - Used to give back a value
# def divide(x, y):
#     return x / y

# # Function call
# result = divide(10,6)
# print("The output is", result)

# ## Yield - Used for producing a sequence (Generators)
# def count_the_diff(n):
#     i = 2
#     while i <= n:
#         yield i
#         i += 3

# for number in count_the_diff(11):
#     print(number) # output 2 5 8 11


## Types of Arguments

# Postional Arguments

# def introduce(store, location):
#     print("Our Store name is", store)
#     print("It is located in", location, ".")

# Function call
# introduce("NCC Hub", "Abeokuta") # Our Store name is NCC Hub # It is located in Abeokuta 

# introduce("Abeokuta", "NCC Hub") # Incorrect order, this will throw a semantic error


## Keyword Arguments

# def introduce(store, location):
#     print("Our Store name is", store)
#     print("It is located in", location, ".")

# # function call
# introduce(store = "NCC Hub", location = "Abeokuta")

# introduce(location = "Abeokuta", store = "NCC Hub") # Returns same output, order doesn't matter.

## Default Arguments

# def introduce(store, location = "Abeokuta"):
#     print("Our Store name is", store)
#     print("It is located in", location, ".")

# # function call
# introduce("NCC Hub") # Despite giving the name a vlaue, it returns default value for location and prints the defined store name.

# introduce("NCC Abk Hub", location = "Lagos") # Location changes to Lagos and the store name too.


## Varying Length Arguments
#  Non-Keyword arguments (*args - tuple)
# def sub_numbers(*args):
#     total = 0
#     for num in args:
#         total -= num
#         print("Subtraction:", total)

# # function call
# sub_numbers(2, 3, 4) #output is -2, -5, -9
# sub_numbers(10, 20, 30, 40, 50) #output is -10, -30, -60, -100, -150

## Keyword argument(**kwargs - dict)
# def store_details(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# # function call
# store_details(Item ="Bags", Brand = "ASOS", Material = "Leather")

## USE CASE
def designer_profile(name, production_date, product_type = "Tote bag", *price, **extra_info):
    """
    Generate a profile of a designer using different types of arguments.
    """
    profile = f"\n------Fashion Designer Profile-----\n"
    profile += f"Name: {name}\n"
    profile += f"Production date: {production_date}\n"
    profile += f"Product Type: {product_type}\n"

    # price (*args)
    if price:
        profile += "Price: " + "," .join(price) + "\n"
    else:
        profile += "Price: Not yet specified\n"

    # Extra info (**kwargs)
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"
    
    return profile

print(designer_profile("ASOS", "24-1-2025")) # using postional arguments
print(designer_profile("Dune", "23-11-2025", product_type="Satchel")) # adding keyword/default argument
print(designer_profile("Demi K", "21-1-2026", "Abaya", f"{120000:,.2F}")) # Adding variable-length positional arguments (*args)
print(designer_profile(
    "Demi K", "21-1-2026", 
    "Abaya", 
    f"{120000:,.2F}",
    fabric = "cotton", location = "Made in Nigeria", product_no = "#DK23091"
)) # Adding variable-length keyword arguments (*kwargs)
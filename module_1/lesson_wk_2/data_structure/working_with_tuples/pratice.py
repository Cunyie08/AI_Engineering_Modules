# Using Parentheses - tuple with multiple items
tools = ("Hammer", "Screwdriver", "Pliers")
print(tools)

# Without parentheses
nums = 2, 4, 6, 8, 10
print(nums)

# Single-item tuple (must include a comma) & checking data type
single_item = ("chicken",)
print(single_item)
print(type(single_item))
item_no = 234
print(item_no)
print(type(item_no))

# Using the tuple () constructor
fruits_list = ["kiwi", "grapes", "tangerine"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

# Ordered
colors = ("red", "yellow", "blue")
print(colors[-1])

# Immutable (uncomment and run. This will cause an error)
#colors[-1] = "yellow"

# Allow duplicates
nums = (1, 2, 2, 3)
print(nums)

# Mixed data types
mixed = ("apples", 3, True, 89.43)
print(mixed)

# Nested tuples
nested = (("x","y"),("a","d"))
print(nested)

## Tuple Operations

# Indexing
fruits = ("kiwi", "grapes", "mango", "orange")
print(fruits[2])
print(fruits[-1])

# Slicing
print(fruits[0:-1]) # starts from 0th and stops at the specified number
print(fruits[::2]) # starts from 0th stops, picks every second and stop before the specified number
print(fruits[::]) # everything returns

# Concatenation
tuple1 = (1,2)
tuple2 = (3,4)
result = tuple1 + tuple2
print(result)

# Repetition
nums = (1,2)
print(nums*10)

# Membership
fruits = ("kiwi", "grapes", "mango", "orange")
print("banana" in fruits) # false
print("orange" in fruits)

# Iteration
for fruits in fruits:
    print(fruits) # returns the elements on separate lines


## Unpacking Tuples
person = ("Anas",28,"Palestinian")
name,age,country = person
print(name)
print(age,country)

# Tuple Methods
nums = (1, 2, 2, 3, 4, 4, 4, 3, 4, 4)
print(nums.count(2)) # counts how many times each number appears
print(nums.index(4))

## Converting Between List and Tuple

# Tuples to List
t = (1,4,8,98)
lst = list(t)
lst.append(3)
lst.append(2)
print(lst) # Adds 3 and 2 in the order of input


# List back to tuple
t = tuple(lst)
print(t)

# Built in functions with Tuples
nums = (2, 4, 6, 8, 10)

print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
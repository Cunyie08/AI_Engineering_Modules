# Method 1: Using square brackets
empty_txt = []
print(empty_txt)
empty_txt2 = ()
print(empty_txt2)

# list of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)

# list of strings
fruits = ['apples', 'orange', 'grapes']
print(fruits)

# list of Mixed data types
mixed_list = ["Alice", 23, 89.5, True]
print(mixed_list)

# From string (each character becomes an element)
chars = list("Salut!")
print(chars)

# From a tuple
my_tuple = (10,20,30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

# From a range
numbers_range = list(range(16))
print(numbers_range)

# Squares of numbers 0-16
squares = [x**2 for x in range(16)]
print(squares)

# Even numbers between 0-16
evens = {x for x in range (17) if x %2 == 0}
print(evens)

# Matrix-like list
matrix = [[1,2], [3,4], [5,6]]
print(matrix)

# Accessing elements in a nested list
print(matrix[0])
print(matrix[1][0])
print(f"{matrix[0]} and {matrix[-1]}")


###  Characteristics

# Ordered Collection
fruits = ['apples', 'orange', 'grapes']
print(fruits)
print(fruits[0])
print(fruits[-1])

# Allows duplicates
items = ["rice", "plantain", 'beans', 'plantain']
print(items)

# Mutable (changeable
numbers = [1, 2, 3, 4, 5]
numbers[1] = 10
numbers[-1] = 28
print(numbers)

# Contains different data types
mixed_list = ["john", 23, 89.5, False]
print(mixed_list)

# Contains other lists (2D or Multidimensional lists)
nested_list = [[2,4], ["Gaza", "westbank"]]
print(nested_list)
print(nested_list[1][0])

# Dynamic Size
names = ["Chris"]
names.append("the")
names.append("instructor")
print(names)


## List operations in Python

# 1. Concatenation
list1 = [2,4,6,8]
list2 = [1,3,5,7]
result = list1 + list2
print(result)

# Reptition
nums = [1,2,3,4]
repeated = nums * 2
print(repeated)

# Indexing
fruits = ["apples", "kiwi", "watermelon"]
print(fruits[-1])
print(fruits[1])
print(f"{fruits[0]}" + " " + "and" + " " f"{fruits[-1]}")
print(f"{fruits[0]} and {fruits[-1]}")


# Slicing
nums = [2,4,6,8,10,12,14,16,18,20]
print(nums[1:-1]) # returns no from the first specified no to the b4 the last spno.
print(nums[:3]) # returns number from the first to the specified number
print(nums[3:]) # returns no from the first specified no to the b4 the last no
print(nums[::2]) #returns the 0th number and every two no after till the nth no


# Membership (in/not in)
comment = ["Gaza", "is", "beautiful"]
print("Congo" in comment)
print("gaza" in comment)
print("Gaza" in comment)

# Lenght
items = ["rice", "plantain", 'beans', 'plantain']
print(len(items))

# Min and Max 
nums = [2,4,6,8,10,12,14,16,18,20]
print(min(nums))
print(max(nums))
print(min(nums),max(nums))

# Sum ()
nums = [2,4,6,8,10,12,14,16,18,20]
print(sum(nums))
print(sum(nums[::3]))

# Comprehension
squares = [x**2 for x in range(10)]
print(squares)

# Copying a list
a = [2,4,6]
b = a.copy() 
print(b)
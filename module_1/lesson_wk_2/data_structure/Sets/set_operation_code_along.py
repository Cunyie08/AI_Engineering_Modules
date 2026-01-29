# Adding elements
day = {"wed", "nes"}
print(day) 
day.add("day")
print(day) #unordered

# Removing elements
day.remove("nes") # returns error if element is missing, it removes if found
print(day)
day.discard("wed") # removes element if found, if not found no error returned
print(day)

# Pop an element
day = {"wed", "nes", "day"}
removed = day.pop()
print("Removed:", removed)
print("Remaining:", day)

# Clear a set
day.clear()
print(day)

## Mathematical operations 
set1 = {1, 3, 5, 5, 7, 9, 2, 4, 6, 8, 10}
set2 = {1, 3, 5, 7, 9}

# Union
print(set1 | set2)
print(set.union(set1))

# Intersection
print(set1 & set2)
print(set1.intersection(set2))

# Difference 
print(set1 - set2)
print(set1.difference(set2))

# Symmetric Difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# Collecting unique visitors to an event
 # 1. create empty set
guests = set()

 # 2. Adding guests - it is case sentitive
guests.add("Mike")
guests.add("Nike")
guests.add("Hike")
guests.add("Mike")
guests.add("mike")

# Checking if a guest attended 

name = "nike"
if name in guests:
    print(f"{name} attended the party")
else:
    print(f"{name} did not attend the party")
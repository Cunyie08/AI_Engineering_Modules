## Different ways toimport modules in Python

#1. Import the whole module 
import math 
print(math.sqrt(9)) # - Note that you must specify the module name when calling a function within it.


# 2. Import as an alias
import math as m # - This shortens the module name, this is common with libraries like numpy, pandas, etc
print(math.sqrt(25)) 

# 3. Import specific functions or variables
from math import sqrt, pi
print(sqrt(36))
print(pi)


## Writing your own Module

# my_module/first.py
# Importing the whole package

import my_package

print(my_package.add(2, 2))
print(my_package.subtract(4, 1))
print(my_package.capitalize_text("data python"))
print(my_package.reverse_text("balloon"))
print(my_package.greet("Ademide"))

# OR import specific modules
from my_package import string_utils

print(string_utils.capitalize_text("what's good cunyie?"))
print(string_utils.greet("Cunyie"))
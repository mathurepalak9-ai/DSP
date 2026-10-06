#Program 1: Build-in Moodule (math)
import math
num = 16
print("Square root of", num, "is", math.sqrt(num))
print("Factorial of", num, "is", math.factorial(num))
print("Power:", math.pow(2, 3))
print("Log: ", math.log(10))

#Program 2: Functional Programming Module
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print("\n Sum using reduce:", result)


#Program 3: User Defined Module Concept
#Create file my_module.py
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b

#Import and use module
import my_module  # type: ignore[import-not-found]
print("Addition:", my_module.add(5, 3))
print("Multiplication:", my_module.multiply(4, 2))



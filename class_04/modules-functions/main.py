# Modules
# User-Defined Module

import my_module

print(my_module.greet("Sara"))
print(my_module.add(5, 7))

# Built-in Modules

import math

print(math.sqrt(16))      # Square root
print(math.factorial(5))  # 120

import random

print(random.randint(1, 10))  # Random number between 1 and 10

from math import pi
print(pi)

# Third-party Modules

import requests

response = requests.get("https://catfact.ninja/fact")
print(response.status_code)

# Functions

def greet():
    print("Hello, welcome to Python functions!")

greet()

# Function with parameters

def greet1(name):
    return f"Hello, {name}!"

print(greet1("Sara"))
print(greet1("Ali"))

#Function with Return Value

def square(x):
    return x * x

result = square(5)
print("Square is:", result)

# Function with Default Parameters

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Ali")

# Keyword Arguments

def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

student_info(age=18, name="Adeel")


# Arbitrary Arguments

def total_marks(*marks):
    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(80, 75, 90, 85)

# Arbitrary Keyword Arguments

def student_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

student_details(name="Ali", age=20, course="Python")


# Lambda Functions

square = lambda x: x * x
print(square(6))

add = lambda a, b: a + b
print(add(5, 3))

# Recursive Functions

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120


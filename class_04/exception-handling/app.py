# Exception Handling in Python

# Handling Specific Exceptions

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple except Blocks

try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Using else Block

try:
    value = int(input("Enter a number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result is {result}")

# Using finally Block

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
    print("File closed.")

# Raising Exceptions

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age

# User-Defined Exceptions

class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative.")
    return age

#------------------------

def divide_numbers():
    try:
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))
        result = num1 / num2
    except ValueError:
        print("Please enter valid integers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"The result is {result}")
    finally:
        print("Operation completed.")

divide_numbers()




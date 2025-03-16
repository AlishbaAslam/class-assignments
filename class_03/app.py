# Python Conditions and If statements

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# If statement

# num1 = 20
# num2 = 100
# if num2 > num1:
#   print("num2 is greater than num1")

# Elif statement

# num1 = 20
# num2 = 20
# if num2 > num1:
#   print("num2 is greater than num1")
# elif num1 == num2:
#   print("num1 and num2 are equal")

# Else statement

# num1 = 50
# num2 = 10
# if num2 > num1:
#   print("num2 is greater than num1")
# elif num1 == num2:
#   print("num1 and num2 are equal")
# else:
#   print("num1 is greater than num2")

# If and Else statement

# num1 = 100
# num2 = 50
# if num2 > num1:
#   print("num2 is greater than num1")
# else:
#   print("num2 is not greater than num1")

# Logical operators
# Logical operators is used to combine conditional statements.

# And

# num1 = 100
# num2 = 40
# num3 = 800
# if num1 > num2 and num3 > num1:
#   print("Both conditions are True")

# Or

# num1 = 100
# num2 = 40
# num3 = 800
# if num1 > num2 or num1 > num3:
#   print("At least one of the conditions is True")

# Not

# num1 = 40
# num2 = 800
# if not num1 > num2:
#   print("num1 is NOT greater than num2")

# Nested If

# num1 = 30

# if num1 > 10:
#   print("Above ten,")
#   if num1 > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")


# For loop

# for i in range(5):  # Loops 5 times (0 to 4)
#     print(i)

# While loop

# x = 0
# while x < 5:
#     print(x)
#     x += 1  # Increase x by 1 each time

# Loop Control Statements

# break 
# for i in range(5):
#     if i == 3:
#         break  # Stops when i is 3
#     print(i)

# continue 
# for i in range(5):
#     if i == 2:
#         continue  # Skips when i is 2
#     print(i)

# For loop with else (No break)

# num = [1, 2, 3, 4, 5]

# for i in num:
#     print(i)
# else:
#     print("Loop completed!")

# Nested loop

# i = 1

# while i < 5:
#     j = 1
#     while j < 5:
#         print(j)
#         j += 1
#     i += 1

# LIST (Mutable)

# fruits = ["apple", "banana", "cherry"]

# fruits.append("orange")  # ['apple', 'banana', 'cherry', 'orange']

# fruits.remove("banana") # ['apple', 'cherry', 'orange']

# fruits.sort()  # ['apple', 'cherry', 'orange']

# fruits.reverse()  # ['orange', 'cherry', 'apple']

# print(fruits) # ['orange', 'cherry', 'apple']

# Tuple (Immutable)

# colors = ("red", "green", "blue")

# print(colors[1])  # 'green'

# print(colors.index("blue"))  # 2

# print(colors.count("red"))  # 1

# Dictionary (Key-Value pairs)

# student = {
#     "name": "Ali",
#     "age": 20,
#     "course": "Python"
# }

# print(student["name"])  # 'Ali'

# student["grade"] = "A"

# student["age"] = 21

# student.pop("course")

# print(student.keys())  # dict_keys(['name', 'age', 'grade'])

# print(student.values())  # dict_values(['Alice', 21, 'A'])

# print(student)

# SET (Unordered and mutable)

# fruits = {"apple", "banana", "cherry", "apple"}  # Duplicates are removed

# print(fruits)  # {'apple', 'banana', 'cherry'}

# fruits.add("orange")
# print(fruits)  # {'apple', 'banana', 'cherry', 'orange'}

# fruits.remove("banana")  # Removes 'banana' (raises error if not found)
# fruits.discard("cherry")  # Removes 'cherry' (does not raise error if not found)

# print(fruits)  # {'apple', 'orange'}

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# # Union (All unique elements from both sets)
# print(A | B)  # {1, 2, 3, 4, 5, 6}

# # Intersection (Common elements)
# print(A & B)  # {3, 4}

# # Difference (Elements in A but not in B)
# print(A - B)  # {1, 2}

# # Symmetric Difference (Elements in either set, but not both)
# print(A ^ B)  # {1, 2, 5, 6}


# FROZENSET (Immutable)

# frozen_fruits = frozenset(["apple", "banana", "cherry"])

# print(frozen_fruits)  # frozenset({'apple', 'banana', 'cherry'})

# print("apple" in frozen_fruits)  # True

# A = frozenset([1, 2, 3])
# B = frozenset([3, 4, 5])

# print(A | B)  # frozenset({1, 2, 3, 4, 5})  # Union
# print(A & B)  # frozenset({3})  # Intersection





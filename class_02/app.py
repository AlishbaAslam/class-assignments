# 1. Arithmetic Operators

a = 5
b = 2

print(a + b)  # Addition: 7
print(a - b)  # Subtraction: 3
print(a * b)  # Multiplication: 10
print(a / b)  # Division: 2.5
print(a // b)  # Floor Division: 2
print(a % b)  # Modulus: 1
print(a ** b)  # Exponentiation: 25

# 2. Assignment Operators

x = 10
x += 5  # x = x + 5
print(x)  # 15

x -= 3  # x = x - 3
print(x)  # 12

x *= 2  # x = x * 2 
print(x)  # 24

x /= 3  # x = x / 3
print(x)  # 8.0

x //= 4  # x = x // 4
print(x)  # 2.0

# 3. Comparison Operators

a = 5
b = 4

print(a == b)  # False
print(a != b)  # True
print(a > b)  # True
print(a < b)  # False
print(a >= b)  # True
print(a <= b)  # False

# 4. Logical Operators

x = True
y = False

print(x and y)  # False
print(x or y)  # True
print(not x)  # False

# 5. Identity Operators

a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)  # True (same memory location)
print(a is c)  # False (different memory location)
print(a is not c)  # True (different memory location)

# 6. Membership Operators

name = "Alishba"
list = [10, 20, 30, 40, 50]

print("A" in name)  # True
print("D" not in name)  # True
print(40 in list)  # True
print(1 in list)  # False

# 7. Bitwise Operators

a = 5  # 101 in binary
b = 3  # 011 in binary

print(a & b)  # 1 (Binary: 001)
print(a | b)  # 7 (Binary: 111)
print(a ^ b)  # 6 (Binary: 110)
print(~a)  # -6 (Inverts all bits)
print(a << 1)  # 10 (Binary: 1010)
print(a >> 1)  # 2 (Binary: 10)

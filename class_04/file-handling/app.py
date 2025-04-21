# Create and Write to a File (w mode)

# Opening a file in write mode

file = open("library.txt", "w")
file.write("Hello, World!")
file.close()

# Append to a File (a mode)

# Opening a file in append mode

file = open("library.txt", "a")
file.write("\nThis will add this line")
file.close()

# Read from a File (r mode)

# Reading a file

file = open("library.txt", "r")
content = file.read()
print(content)
file.close()

# Binary Read Mode (rb)

# Reading a file in binary mode

file = open("library.txt", "rb")
content = file.read()
print(content)
file.close()

# Using with Statement (Best Practice)

# Best practice for opening a file

with open("library.txt", "r") as file:
    content = file.read()
    print(content)

# Exception Handling with File Operations

# Handling exceptions manually

try:
    file = open("library.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()


# Exclusive Creation Mode (x)

# Creating a file using exclusive mode

try:
    file = open("library.txt", "x")
    file.write("This file is created using 'x' mode.")
    file.close()
except FileExistsError:
    print("File already exists!")

# File Pointer: tell() and seek()

# Demonstrating file pointer functions

file = open("library.txt", "r")
print("Current Position:", file.tell())         # Get current position
print(file.readline())                          # Read one line
print("After reading one line:", file.tell())   # New position
file.seek(0)                                    # Move back to start
print("After seek(0):", file.tell())
file.close()



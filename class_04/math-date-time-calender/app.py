# Epoch     January 1, 1970, 00:00:00 (UTC)
# Ticks     unit of time    tick = 1 second

# Epoch   	Starting point of time (usually Jan 1, 1970)
# Ticks  	Number of seconds passed since the epoch

# Time Module (Epoch, Ticks, Local Time)

import time

# Number of seconds since Epoch
print("Ticks since Epoch:", time.time())

# Local time as a struct_time tuple
print("Local time:", time.localtime())

# Readable format
print("Formatted time:", time.asctime(time.localtime()))

# Calendar Module

import calendar

# Calendar for January 2025
print("Calendar for Jan 2025:")
print(calendar.month(2025, 1))

#  Datetime Module

from datetime import date, datetime

# Creating specific dates
d1 = date(2023, 4, 19)
d2 = date(2023, 4, 30)
print("Date 1:", d1)
print("Date 2:", d2)

# Current date and time
now = datetime.now()
print("Now:", now)

# Datetime Formatting (strftime)

import datetime

dt = datetime.datetime(2025, 1, 1)
print("Microseconds:", dt.strftime("%f"))
print("Day Name:", dt.strftime("%A"))
print("Year:", dt.strftime("%Y"))
print("Month Name:", dt.strftime("%B"))

# Built-in Math Functions

print(abs(-10))          # 10
print(pow(2, 4))         # 16
print(round(3.1416, 2))  # 3.14
print(max(1, 9, 5))      # 9
print(min(1, 9, 5))      # 1

# Math Module Functions

import math

print(math.sqrt(16))          # 4.0
print(math.factorial(5))      # 120
print(math.sin(math.pi/2))    # 1.0
print(math.log(10))           # Natural log
print(math.log10(100))        # Base-10 log
print(math.exp(2))            # e^2
print(math.ceil(4.2))         # 5
print(math.floor(4.8))        # 4


# ---------------------------------
# -- Date & Time => Introduction --
# ---------------------------------

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Print The Current Date and Time
print(datetime.datetime.now())

print("=" * 50)  # Separator

# Print The Current Year
print(datetime.datetime.now().year)

# Print The Current Month
print(datetime.datetime.now().month)

# Print The Current Day
print(datetime.datetime.now().day)

print("=" * 50)  # Separator

# Print Start and End Of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("=" * 50)  # Separator

# print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())

print("=" * 50)  # Separator

# Print The Current Time Hour
print(datetime.datetime.now().time().hour)

# Print The Current Time Minute
print(datetime.datetime.now().time().minute)

# Print The Current Time Second
print(datetime.datetime.now().time().second)

print("=" * 50)  # Separator

# Print Start and End Of Time
print(datetime.time.min)
print(datetime.time.max)

print("=" * 50)  # Separator

# Print Specific Date
print(datetime.datetime(1982, 10, 25))
print(datetime.datetime(1982, 10, 25, 10, 45, 55, 150364))

print("=" * 50)  # Separator

myBirthDay = datetime.datetime(2005, 8, 4)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} And ", end="")
print(f"Date Now Is {dateNow}")

print(f" I Lived For {dateNow - myBirthDay}")
print(f" I Lived For {(dateNow - myBirthDay).days} Days.")

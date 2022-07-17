# -----------------------------------
# -- String - Formatting - Old Way --
# -----------------------------------

name = "Osama"
age = 36
rank = 10
print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("=" * 50)  # Separator

print("My Name is: %s" % "Osama")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name, age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

print("=" * 50)  # Separator

a = "Osama"
b = "Python"
c = 10
print("My Name is %s Iam %s Developer With %d Years Exp" % (a, b, c))
# %s => String
# %d => Number
# %f => Float

print("=" * 50)  # Separator

# Control Floating Point Number
my_number = 10
print("My Number is: %d" % my_number)
print("My Number is: %f" % my_number)
print("My Number is: %.2f" % my_number)

print("=" * 50)  # Separator

# Truncate String
my_long_string = "Hello People of Elzero Web School, I Love You All"
print("Your Message is %s" % my_long_string)
print("Your Message is %.5s" % my_long_string)

# -----------------------------------
# -- String - Formatting - New Way --
# -----------------------------------

name = "Osama"
age = 36
rank = 10
print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error
print("=" * 50)  # Separator

print("My Name is: {}".format("Osama"))
print("My Name is: {}".format(name))
print("My Name is: {} My Age: {}".format(name, age))
print("My Name is: {:s} Age: {:d} & Rank is: {:f}".format(name, age, rank))
print("=" * 50)  # Separator

a = "Osama"
b = "Python"
c = 10
print("My Name is {} Iam {} Developer With {:d} Years Exp".format(a, b, c))
print("=" * 50)  # Separator
# {:s} => String
# {:d} => Number
# {:f} => Float

# Control Floating Point Number
my_number = 10
print("My Number is: {:d}".format(my_number))
print("My Number is: {:f}".format(my_number))
print("My Number is: {:.2f}".format(my_number))
print("=" * 50)  # Separator

# Truncate String
my_long_string = "Hello Peoples of Elzero Web School I Love You All"
print("Message is {}".format(my_long_string))
print("Message is {:.5s}".format(my_long_string))
print("Message is {:.13s}".format(my_long_string))
print("=" * 50)  # Separator

# Format Money
my_money = 500162350198
print("My Money in Bank Is: {:d}".format(my_money))
print("My Money in Bank Is: {:,d}".format(my_money))
print("My Money in Bank Is: {:_d}".format(my_money))
print("=" * 50)  # Separator

# Re-arrange Items
d, e, f = "One", "Two", "Three"
print("Hello {} {} {}".format(d, e, f))  # Output => Hello One Two Three
print("Hello {1} {2} {0}".format(d, e, f))  # Output => Hello Two Three One
print("Hello {2} {0} {1}".format(d, e, f))  # Output => Hello Three One Two
print("=" * 50)  # Separator

g, h, i = 10, 20, 30
print("Hello {} {} {}".format(g, h, i))
print("Hello {1:d} {2:d} {0:d}".format(g, h, i))
print("Hello {2:f} {0:f} {1:f}".format(g, h, i))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(g, h, i))
print("=" * 50)  # Separator

# Format in Version 3.6+
my_name = "Osama"
my_age = 36
print("My Name is : {my_name} and My Age is : {my_age}")
print(f"My Name is : {my_name} and My Age is : {my_age}")

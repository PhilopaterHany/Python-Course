# ---------------------------------------------------------------
# ---------------- Tuple & Its Methods - Part 01 ----------------
# ---------------------------------------------------------------
# [1] Tuple Items Are Enclosed in Parentheses ()
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, Use Index To Access Any Item
# [4] Tuple Are Immutable => You Cannot Add or Delete Items
# [5] Tuple Items Are Not Unique (Items Can Be Repeated)
# [6] Tuple Can Contain Different Data Types
# [7] Operators Used in String and Lists Are Available In Tuples
# ---------------------------------------------------------------

# Tuple Syntax & Type Test
my_awesome_tuple_one = ("Osama", "Ahmed")
my_awesome_tuple_two = "Osama", "Ahmed"

print(my_awesome_tuple_one)
print(my_awesome_tuple_two)

print(type(my_awesome_tuple_one))
print(type(my_awesome_tuple_two))

print("=" * 50)  # Separator

# Tuple Indexing
my_awesome_tuple_three = (1, 2, 3, 4, 5)
print(my_awesome_tuple_three[0])
print(my_awesome_tuple_three[-1])
print(my_awesome_tuple_three[-3])

print("=" * 50)  # Separator

# Tuple Assign Values
my_awesome_tuple_four = (1, 2, 3, 4, 5)
# my_awesome_tuple_four[2] = "Three"
# print(my_awesome_tuple_four)  # Error => 'tuple' object does not support item assignment

# Tuple Data
my_awesome_tuple_five = ("Osama", "Osama", 1, 2, 3, 100.5, True)
print(my_awesome_tuple_five[1])
print(my_awesome_tuple_five[-1])

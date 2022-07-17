# ------------------------------------------------------------
# String Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ------------------------------------------------------------

# Indexing ( Access Single Item )
my_string = "I Love Python"
print(my_string[0])  # Index 0 => I => 1st Character From The Beginning, Output => I
print(my_string[9])  # Index 9 => t => 10th Character From The Beginning, Output => t

print("=" * 50)  # Separator

print(my_string[-1])  # Index -1 => First Character From The End, Output => n
print(my_string[-6])  # Index -6 => 6th Character From The End, Output => P

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]
print(my_string[7:13])  # Start From index 8 and end at index 11, Output => Python
print(my_string[2:6])  # Start From index 3 and end at index 5, Output => Love

print("=" * 50)  # Separator

print(my_string[:10])  # If Start Is Not Written, It Will Start From 0, Output => I Love Pyt
print(my_string[7:])  # If End Is Not Written, It Will Go To The End, Output => Python

print("=" * 50)  # Separator

print(my_string[:])  # Full Data, Output => I Love Python
print(my_string[0::1])  # Full Data, Output => I Love Python

print("=" * 50)  # Separator

print(my_string[::1])  # Full Data, Output => I Love Python
print(my_string[::2])  # Will Move 2 Steps, Output => ILv yhn

print("=" * 50)  # Separator

print(my_string[::3])  # Will Move 3 Steps, Output => Io tn

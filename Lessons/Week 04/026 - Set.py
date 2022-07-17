# ---------------------------------------------------------------------------------------
# ----------------------------------------- Set -----------------------------------------
# ---------------------------------------------------------------------------------------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cannot Be Done
# [4] Set Contain Immutable Data Types Only (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Are Unique (No Repetition)
# ---------------------------------------------------------------------------------------

# Not Ordered & Not Indexed
my_set_one = {"Osama", "Ahmed", 100}
print(my_set_one)
# print(mySetOne[0])

# Slicing Cannot Be Done
my_set_two = {1, 2, 3, 4, 5, 6}
# print(my_set_two[0:3])

# Contain Immutable Data Types Only
# my_set_three = {"Osama", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
my_set_three = {"Osama", 100, 100.5, True, (1, 2, 3)}
print(my_set_three)

# Items Are Unique
my_set_four = {1, 2, "Osama", "One", "Osama", 1}
print(my_set_four)

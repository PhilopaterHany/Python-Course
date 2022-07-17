# --------------------------------
# -- String - Methods - Part 04 --
# --------------------------------

# replace(Old Value, New Value, Count)
my_string = "Hello One Two Three One One"
print(my_string.replace("One", "1"))
print(my_string.replace("One", "1", 1))
print(my_string.replace("One", "1", 2))

print("=" * 50)  # Separator

# join(Iterable)
my_list = ["Osama", "Mohamed", "Elsayed"]
print("-".join(my_list))
print(" ".join(my_list))
print(", ".join(my_list))
print(type(", ".join(my_list)))

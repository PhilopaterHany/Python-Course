my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    if type(item2) == int:
        break
    my_data.append(str(item2).lower())
    my_data.append(str(item3).lower())
    final_string = "".join(my_data).capitalize()

print(final_string)  # Output => Elzero

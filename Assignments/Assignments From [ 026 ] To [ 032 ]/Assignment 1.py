my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))

print(unique_list)  # Output => [1, 2, 3, 4, 5]

print(type(unique_list))  # Output => list

unique_list.pop(-1)  # Another Solution => unique_list.remove(unique_list[-1])
print(unique_list)  #  Output => [1, 2, 3, 4]

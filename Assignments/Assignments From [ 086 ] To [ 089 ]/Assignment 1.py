my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    for c in data:
        my_data += c.lower()
    final_string = "".join(my_data).capitalize()

print(final_string)  # Output => Elzero

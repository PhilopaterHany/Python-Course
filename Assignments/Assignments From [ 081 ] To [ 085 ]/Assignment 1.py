def reverse_string(my_string):
    yield my_string[::-1]


# Reverse The String
for c in reverse_string("Elzero"):
    print(c)

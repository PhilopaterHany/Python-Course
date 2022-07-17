# -----------------------------------
# -- Tuple & Its Methods - Part 02 --
# -----------------------------------

# Tuple With One Element
my_tuple_one = ("Osama",)
my_tuple_two = "Osama",

print(my_tuple_one)
print(my_tuple_two)

print(type(my_tuple_one))
print(type(my_tuple_two))

print(len(my_tuple_one))
print(len(my_tuple_two))

print("=" * 50)  # Separator

# Tuple Concatenation
a = (1, 2, 3, 4)
b = (5, 6)
c = a + b
d = a + ("A", "B", True) + b
print(c)
print(d)

print("=" * 50)  # Separator

# Tuple, List, String Repeat (*)
myString = "Osama"
myList = [1, 2]
myTuple = ("A", "B")
print(myString * 6)
print(myList * 6)
print(myTuple * 6)

print("=" * 50)  # Separator

# Methods => count()
a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))

print("=" * 50)  # Separator

# Methods => index()
b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7))  # Error
print("The Position of Index Is: {:d}".format(b.index(7)))
print(f"The Position of Index Is: {b.index(7)}")

print("=" * 50)  # Separator

# Tuple Destruct
a = ("A", "B", 4, "C")
x, y, _, z = a
print(x)
print(y)
print(z)

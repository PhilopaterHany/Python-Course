# -----------------------
# --- Type Conversion ---
# -----------------------

# str()
a = 10
print(type(a))
print(type(str(a)))

print("=" * 50)  # Separator

# tuple()
c = "Osama"  # String
d = [1, 2, 3, 4, 5]  # List
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))

print("=" * 50)  # Separator

# list()
c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(f))

print("=" * 50)  # Separator

# set()
c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = ["A", "B", "C"]  # List
f = {"A": 1, "B": 2}  # Dictionary

print(set(c))
print(set(d))
print(set(e))
print(set(f))

print("=" * 50)  # Separator

# dict()
d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
e = [["One", 1], ["Two", 2], ["Three", 3]]  # List

print(dict(d))
print(dict(e))

print("=" * 50)  # Separator

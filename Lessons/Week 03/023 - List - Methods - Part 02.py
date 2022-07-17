# ------------------------------
# -- List - Methods - Part 02 --
# ------------------------------

# clear() (Removes All Elements In An Array)
a = [1, 2, 3, 4]
a.clear()
print(a)
print("=" * 50)  # Separator

# copy() (Returns A Shallow Copy)
b = [1, 2, 3, 4]
c = b.copy()
print(b)  # Main List
print(c)  # Copied List
b.append(5)
print(b)  # Main List
print(c)  # Copied List
print("=" * 50)  # Separator

# count() (Returns The Number Of Times The Element Was Found)
d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))
print("=" * 50)  # Separator

# index() (Returns The index Of The Given Element)
e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))
print("=" * 50)  # Separator

# insert() (Adds Element)
f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")
print(f)
print("=" * 50)  # Separator

# pop() (Removes Element)
g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))

# ------------------------------
# -- List - Methods - Part 01 --
# ------------------------------

# append() (Adds Elements At The End Of The List)
my_friends = ["Osama", "Ahmed", "Sayed"]
my_old_friends = ["Haytham", "Samah", "Ali"]
my_friends.append("Alaa")
my_friends.append(100)
my_friends.append(150.200)
my_friends.append(True)
my_friends.append(my_old_friends)
print(my_friends)
print(my_friends[2])
print(my_friends[6])
print(my_friends[7])
print(my_friends[7][2])
print("=" * 50)  # Separator

# extend() (Flats/Concatenates The Lists)
a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]
a.extend(b)
a.extend(c)
print(a)
print("=" * 50)  # Separator

# remove() (Removes The Given Element)
x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
x.remove("Osama")
print(x)
print("=" * 50)  # Separator

# sort() (Arrange The Elements From 1-9 and From A-Z)
y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort(reverse=True)  # (Arrange The Elements From 9-1 and From Z-a)
print(y)
print("=" * 50)  # Separator

# reverse() (It Reverses The List => The Last Element Becomes The First One and so on...)
z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z)

# -----------------------------
# -- Set - Methods - Part 02 --
# -----------------------------

# difference()
a = {1, 2, 3, 4}
b = {1, 2, 3, "Osama", "Ahmed"}
print(a)
print(a.difference(b))  # a - b
print(a)
print("=" * 50)  # Separator

# difference_update()
c = {1, 2, 3, 4}
d = {1, 2, "Osama", "Ahmed"}
print(c)
c.difference_update(d)  # c - d
print(c)
print("=" * 50)  # Separator

# intersection()
e = {1, 2, 3, 4, "X", "Osama"}
f = {"Osama", "X", 2}
print(e)
print(e.intersection(f))  # e & f
print(e)
print("=" * 50)  # Separator

# intersection_update()
g = {1, 2, 3, 4, "X", "Osama"}
h = {"Osama", "X", 2}
print(g)
g.intersection_update(h)  # g & h
print(g)
print("=" * 50)  # Separator

# symmetric_difference()
i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4, "X"}
print(i)
print(i.symmetric_difference(j))  # i ^ j
print(i)
print("=" * 50)  # Separator

# symmetric_difference_update()
k = {1, 2, 3, 4, 5, "X"}
ll = {"Osama", "Zero", 1, 2, 4, "X"}
print(k)
k.symmetric_difference_update(ll)  # k ^ l
print(k)

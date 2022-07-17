# -----------------------------
# -- Set - Methods - Part 01 --
# -----------------------------

# clear()
a = {1, 2, 3}
a.clear()
print(a)
print("=" * 50)  # Separator

# union()
b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}
print(b | c)
print(b.union(c, x))
print("=" * 50)  # Separator

# add()
d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)
print("=" * 50)  # Separator

# copy()
e = {1, 2, 3, 4}
f = e.copy()
print(e)
print(f)
print("=" * 50)  # Separator

# add()
e.add(6)
print(e)
print(f)
print("=" * 50)  # Separator

# remove()
g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7)
print(g)
print("=" * 50)  # Separator

# discard()
h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)
print("=" * 50)  # Separator

# pop()
i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())
print("=" * 50)  # Separator

# update()
j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"])
j.update(k)
print(j)

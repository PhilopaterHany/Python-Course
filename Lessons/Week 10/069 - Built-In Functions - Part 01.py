# ----------------------------------
# -- Built-In Functions - Part 01 --
# ----------------------------------
# all()
# any()
# bin()
# id()
# ----------------------------------

x = [1, 2, 3, 4, []]

if all(x):
    print("All Elements Are True")
else:
    print("There's At Least One Element Is False")

print("=" * 50)  # Separator

x = [0, 0, []]
if any(x):
    print("There's At Least One Element is True")
else:
    print("There's No Any True Elements")

print("=" * 50)  # Separator

print(bin(100))

print("=" * 50)  # Separator

a = 1
b = 2
print(id(a))
print(id(b))

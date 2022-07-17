# ---------------------------------------------------------------------------
# --------------------------------- Boolean ---------------------------------
# ---------------------------------------------------------------------------
# [1] In Programming You Need to Know If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False and True.
# ---------------------------------------------------------------------------

name = " "
print(name.isspace())

print("=" * 50)  # Separator

print(100 > 200)
print(100 > 100)
print(100 > 90)

print("=" * 50)  # Separator

# True Values
print(bool("Osama"))
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

print("=" * 50)  # Separator

# False Values
print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(False))
print(bool(()))
print(bool({}))
print(bool(None))

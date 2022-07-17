# ------------------------------------
# -- Dictionary - Methods - Part 02 --
# ------------------------------------

# setdefault()
user = {
    "name": "Osama"
}
print(user)
print(user.setdefault("age", 36))
print(user)
print("=" * 50)  # Separator

# popitem()
member = {
    "name": "Osama",
    "skill": "PS4"
}
print(member)
member.update({"age": 36})
print(member.popitem())
print("=" * 50)  # Separator

# items()
view = {
    "name": "Osama",
    "skill": "XBox"
}
all_items = view.items()
print(view)
view["age"] = 36
print(all_items)
print("=" * 50)  # Separator

# fromkeys()
a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"
print(dict.fromkeys(a, b))

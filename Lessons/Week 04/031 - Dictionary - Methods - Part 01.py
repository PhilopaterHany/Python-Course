# ------------------------------------
# -- Dictionary - Methods - Part 01 --
# ------------------------------------

# clear()
user = {
    "name": "Osama"
}
print(user)
user.clear()
print(user)

print("=" * 50)  # Separator

# update()
member = {
    "name": "Osama"
}
print(member)
member["age"] = 36
print(member)
member.update({"country": "Egypt"})
print(member)

print("=" * 50)  # Separator

# copy()
main = {
    "name": "Osama"
}
b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

print("=" * 50)  # Separator

# keys() + values()
print(main.keys())
print(main.values())

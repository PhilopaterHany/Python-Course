# ----------------------------------------------------
# -- Function - Packing & Unpacking Arguments *Args --
# ----------------------------------------------------

print(1, 2, 3, 4)

myList = [1, 2, 3, 5]

print(myList)
print(*myList)

print("=" * 50)  # Separator


def say_hello(*people):  # n1, n2, n3, n4
    for name in people:
        print(f"Hello {name}")


say_hello("Osama", "Ahmed", "Sayed", "Mahmoud")

print("=" * 50)  # Separator


def show_details(name, *skills):
    print(f"Hello {name} Your Skills Are: ")
    for skill in skills:
        print(skill)


show_details("Osama", "HTML", "CSS", "JavaScript")

print("=" * 50)  # Separator

show_details("Ahmed", "HTML", "CSS", "JavaScript", "Python", "PHP", "MySQL")

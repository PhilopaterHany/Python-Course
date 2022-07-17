# ----------------
# -- User Input --
# ----------------

first_name = input("Write Your First Name: ")
middle_name = input("Write Your Middle Name: ")
last_name = input("Write Your Last Name: ")

first_name = first_name.strip().capitalize()
middle_name = middle_name.strip().capitalize()
last_name = last_name.strip().capitalize()

print(f"Hello {first_name} {middle_name:.1s} {last_name} Happy To See You.")

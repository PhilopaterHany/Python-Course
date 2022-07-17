# -------------------------------------
# -- Membership Control => Practical --
# -------------------------------------

# List Contains Admins
admins = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

# Login
name = input("Write Your Name: ").strip().capitalize()

# If Name Is In Admins
if name in admins:
    print(f"Hello {name}, Welcome Back!")
    option = input(
        "Do You Want To Delete Or Update Your Name ? ").strip().capitalize()
    # Update Option
    if option == "Update" or option == "U":
        the_new_name = input("Write Your New Name: ").strip().capitalize()
        admins[admins.index(name)] = the_new_name
        print("Name Updated Successfully.")
        print(f"Current Admins: {admins}")
    # Delete Option
    elif option == "Delete" or option == "D":
        admins.remove(name)
        print("Name Deleted Successfully.")
        print(f"Current Admins: {admins}")
    # Wrong Option
    else:
        print("Sorry, Wrong Option Has Been Chosen.")
else:
    status = input(
        "You Are Not An Admin. Should I Add You ( Yes Or No )? ").strip().capitalize()
    if status == "Yes" or status == "Y":
        print("You Have Been Added Successfully.")
        admins.append(name)
        print(f"Current Admins: {admins}")
    else:
        print("You Have Not Been Added.")

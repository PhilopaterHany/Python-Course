# -----------------------------------
# -- Function - Default Parameters --
# -----------------------------------

def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    print(
        f"Hello {name}, Your Age is {age} Years Old and Your Country Is {country}.")


say_hello("Osama", 36, "Egypt")
say_hello("Mahmoud", 28, "KSA")
say_hello("Sameh", 38)
say_hello("Ramy")
say_hello()

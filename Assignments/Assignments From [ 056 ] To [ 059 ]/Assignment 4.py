def say_hello(name="Unknown Person", age="Unknown", country="An Unknown Country"):
    return f"Hello {name.strip().capitalize()}, You Are {age} Years Old and You Live In {country.strip().capitalize()}"


print(say_hello("Osama", 38, "Egypt"))
print("=" * 50)  # Separator
print(say_hello("Philopater", 17))
print("=" * 50)  # Separator
print(say_hello())

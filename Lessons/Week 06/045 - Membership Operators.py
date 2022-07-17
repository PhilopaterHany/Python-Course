# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# String
name = "Osama"
print("s" in name)
print("a" in name)
print("A" in name)

print("=" * 50)  # Separator

# List
friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Osama" in friends)
print("Sayed" in friends)
print("Mahmoud" not in friends)

print("=" * 50)  # Separator

# Using "in" and "not in" With If Condition
countries_One = ["Egypt", "KSA", "Kuwait", "Bahrain", "Syria"]
countries_one_discount = 80
countries_Two = ["Italy", "USA"]
countries_two_discount = 50
my_country = "Italy"

if my_country in countries_One:
    print(f"Hello, You Have A ${countries_one_discount} Discount.")
elif my_country in countries_Two:
    print(f"Hello, You Have A ${countries_two_discount} Discount.")
else:
    print("Sorry, You Have No Discount.")

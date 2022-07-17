# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

country = "A"
if country == "Egypt":
    print(f"The Temprature in {country} Is 38 Degree Celsius.")
elif country == "KSA":
    print(f"The Temprature in {country} Is 42 Degree Celsius.")
else:
    print("Sorry, Country Is Not In The List.")

# Short If
movie_rate = 18
age = 18

if age < movie_rate:
    # Condition If True
    print("Sorry, This Movie Is Not Suitable For You.")
else:
    # Condition If False
    print("This Movie Is Not Suitable For You. Enjoy Your Movie!")


# Condition If True | If Condition | Else | Condition If False
print("Sorry, This Movie Is Not Suitable For You." if age < movie_rate else "This Movie Is Not Suitable For You. Enjoy Your Movie!")

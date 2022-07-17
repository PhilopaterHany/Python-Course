age = int(input("Write Your Age: ").strip())

if 10 < age < 100:
    print(f"You are {age * 12:,} Months Old.")
    print(f"You are {age * 12 * 4:,} Weeks Old.")
    print(f"You are {age * 365:,} Days Old.")
    print(f"You are {age * 365 * 24:,} Hours Old.")
    print(f"You are {age * 365 * 24 * 60:,} Minutes Old.")
    print(f"You are {age * 365 * 24 * 60 * 60:,} Seconds Old.")
else:
    print("Sorry, Your Age Is Out Of Range (10 ~ 100).")

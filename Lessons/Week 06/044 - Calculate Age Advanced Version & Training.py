# -----------------------------------------------
# -- Calculate Age Advanced Version & Training --
# -----------------------------------------------

# Write A Very Beautiful Note
print("=" * 70)
print(" You Can Write The First Letter Or Full Name of The Time Unit ".center(70, '='))
print("=" * 70)

# Collect Age Data
age = int(input("Write Your Age: ").strip())

# Collect Time Unit Data
unit = input("Choose Time Unit (Months, Weeks, Days): ").strip().lower()

# Get Time Units
months = age * 12
weeks = age * 12 * 4
days = age * 365

if unit == "months" or unit == "m":
    print("You Chose The Unit: Months")
    print(f"You Are {months:,} Months Old.")
elif unit == "weeks" or unit == "w":
    print("You Chose The Unit: Weeks")
    print(f"You Are {weeks:,} Weeks Old.")
elif unit == "days" or unit == "d":
    print("You Chose The Unit Days")
    print(f"You Are {days:,} Days Old.")

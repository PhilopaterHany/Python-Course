# -----------------------------
# -- Break & Continue & Pass --
# -----------------------------

myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# Continue
for number in myNumbers:
    if number == 13:
        continue
    print(number)

print("=" * 50)  # Separator

# Break
for number in myNumbers:
    if number == 13:
        break
    print(number)

print("=" * 50)  # Separator

# Pass
for number in myNumbers:
    if number == 13:
        pass
    print(number)

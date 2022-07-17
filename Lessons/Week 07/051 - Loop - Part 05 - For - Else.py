# --------------------------------------------------------------------------------------
# ------------------------------------- Loop => For -------------------------------------
# --------------------------------------------------------------------------------------
# for item in iterable_object :
#   Do Something With Item
# --------------------------------------------------------------------------------------
# item Is A Vairable You Create and Call Whenever You Want.
# item Refers To The Current Position And Will Run And Loop On All Items Till The End.
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# --------------------------------------------------------------------------------------

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in myNumbers:
    # print(number * 17)
    if number % 2 == 0:  # Even
        print(f"{number} Is An Even Number.")
    else:
        print(f"{number} Is An Odd Number.")
else:
    print("The Loop Has Finished")

print("=" * 50)  # Separator

myName = "Osama"
for letter in myName:
    print(f"[ {letter.upper()} ]")

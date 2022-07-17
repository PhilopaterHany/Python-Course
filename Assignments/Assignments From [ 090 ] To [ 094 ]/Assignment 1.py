num = input("Write Your Number: ")

if len(num) >= 2:
    raise IndexError("Sorry, Only One Character Is Allowed.")
elif int(num) <= 0:
    raise ValueError("Sorry, The Number Must Be Larger Than 0.")
elif num.isalpha():
    raise Exception("Sorry, Only Numbers Are Allowed.")
else:
    print("=" * 20)
    print(f"The number Is {num}")
    print("=" * 20)

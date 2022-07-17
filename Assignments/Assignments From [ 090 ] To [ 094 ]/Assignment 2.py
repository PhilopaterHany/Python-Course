letter = input("Write A Letter From A to Z: ")

try:
    if (len(letter) == 1 and letter.isalpha()):
        print(f"You Wrote The Letter => {letter}")
    else:
        if len(letter) > 1:
            raise IndexError
        elif not letter.isalpha():
            raise TypeError
except IndexError:
    print("Sorry, You Must Write One Character Only.")
except TypeError:
    print("Sorry, The Letter Is Not In [A - Z]")

# --------------------------------
# ---- Loop => While Training ----
# ---- Simple Password Checker ---
# --------------------------------

tries = 4
mainPassword = "o@nn.sa"
inputPassword = input("Write Your Password: ")
while inputPassword != mainPassword:  # True
    tries -= 1  # tries = tries - 1
    print(f"Wrong Password, { 'Last' if tries == 0 else tries } Chance Left")
    inputPassword = input("Write Your Password: ")
    if tries == 0:
        print("All Tries Have Finished.")
        break
        print("Will Not Be Printed.")
else:
    print("Correct Password.")

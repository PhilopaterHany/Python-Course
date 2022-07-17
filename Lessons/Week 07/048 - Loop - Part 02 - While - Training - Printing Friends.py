# --------------------------------------------
# ---------- Loop => While Training ----------
# --------------------------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# --------------------------------------------

myF = ["Osama", "Ahmed", "Gamal", "Ali", "Philopater", "Sarah", "Mohamed", "Farah", "Abdallah", "Ashraf", "George"]

# print(len(myF))  # List Length [11]

a = 0
while a < len(myF):  # a < 11
    print(f"#{str(a + 1).zfill(2)} => {myF[a]}")
    a += 1  # a = a + 1
else:
    print("All Friends Have Been Printed To Screen Successfully.")

# print(myF[0])
# print(myF[1])
# print(myF[2])
# print(myF[3])
# print(myF[4])
# print(myF[5])
# print(myF[6])
# print(myF[7])
# print(myF[8])
# print(myF[9])
# print(myF[10])

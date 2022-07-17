# ---------------------------------------------
# --------------- Loop => While ---------------
# ---------------------------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# ---------------------------------------------

a = 0
while a < 15:
    print(a)
    a += 1  # a = a + 1
print("Loop Is Done.")  # True Became False
while False:
    print("Will Not Be Printed.")

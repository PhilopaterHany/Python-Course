# ----------------------------------------------------------------
# ----------------- Built-In Functions => Filter -----------------
# ----------------------------------------------------------------
# [1] Filter Takes A Function + Iterator
# [2] Filter Runs A Function On Each Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filters Out All Elements For Which The Function Returns True
# [5] The Function Needs To Return Boolean Value
# ----------------------------------------------------------------

# Example 1
def checkNumber(num):
    return num > 10


myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]
myResult = filter(checkNumber, myNumbers)
for number in myResult:
    print(number)

print("=" * 50)  # Separator

# Example 2
def checkName(name):
    return name.startswith("O")


myTexts = ["Osama", "Philopater", "Omar", "Ahmed", "Sayed", "Othman"]
myReturnedData = filter(checkName, myTexts)
for person in myReturnedData:
    print(person)

print("=" * 50)  # Separator

# Example 3
myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ameer"]
for p in filter(lambda name: name.startswith("A"), myNames):
    print(p)

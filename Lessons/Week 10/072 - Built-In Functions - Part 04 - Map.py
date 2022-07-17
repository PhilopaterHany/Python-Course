# -------------------------------------------------------------------
# -------------------- Built-In Functions => Map --------------------
# -------------------------------------------------------------------
# [1] Map Takes A Function + Iterator
# [2] Map Is Called Map, Because It Maps The Function On Each Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# -------------------------------------------------------------------

# Use Map With Predefined Function
def formatText(text):
    return f"- {text.strip().capitalize()} -"


myTexts = [" OSama ", "AHMED", "  sAYed  "]
myFormatedData = map(formatText, myTexts)
print(myFormatedData)

for name in list(map(formatText, myTexts)):
    print(name)

print("=" * 50)  # Separator

# Use Map With Lambda Function
def formatText(text):
    return f"- {text.strip().capitalize()} -"


myTexts = [" OSama ", "AHMED", "  sAYed  "]
for name in list(map((lambda text: f"- {text.strip().capitalize()} -"), myTexts)):
    print(name)

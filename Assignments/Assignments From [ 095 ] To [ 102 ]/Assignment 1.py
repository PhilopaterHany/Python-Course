import re
# regex => ([A-z])\s
for letter in re.findall(r"([A-z])\s", "eeeeE llllLl lllzzZzzzz eroe operationr pollo "):
    print(letter, end="")

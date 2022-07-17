# --------------------------------
# -- String - Methods - Part 02 --
# --------------------------------

# split() - rsplit()
a = "I Love Python and PHP and MySQL"
print(a.split())
print("=" * 50)  # Separator

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))
print("=" * 50)  # Separator

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3))
print("=" * 50)  # Separator

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3))
print("=" * 50)  # Separator

# center()
e = "Osama"
print(e.center(9))  # Spaces
print(e.center(9, "#"))  # Hashes
print(e.center(15, "@"))  # @
print("=" * 50)  # Separator

# count()
f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))  # 2 PHP Words
print(f.count("PHP", 0, 25))  # Only One PHP Word
print("=" * 50)  # Separator

# swapcase()

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())
print("=" * 50)  # Separator

# startswith()
i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))
print("=" * 50)  # Separator

# endswith()
j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))

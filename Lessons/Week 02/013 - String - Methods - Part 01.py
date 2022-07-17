# --------------------------------
# -- String - Methods - Part 01 --
# --------------------------------

# strip()
a = "    I Love Python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

print("=" * 50)  # Separator

# rstrip()
b = "#####I Love Python####"
print(b.strip("#"))
print(b.rstrip("#"))
print(b.lstrip("#"))

print("=" * 50)  # Separator

# lstrip()
c = "@#@#@#I Love Python@#@#@#"
print(c.strip("@#"))
print(c.rstrip("@#"))
print(c.lstrip("@#"))

print("=" * 50)  # Separator

# title()
d = "I Love 2d Graphics and 3g Technology and python"
print(d.title())

print("=" * 50)  # Separator

# capitalize()
e = "I Love 2d Graphics and 3g Technology and python"
print(e.capitalize())

print("=" * 50)  # Separator

# zfill
f, g, h, i = "1", "11", "111", "1111"
print(f)
print(g)
print(h)
print(i)
print("=" * 50)  # Separator
print(f.zfill(4))
print(g.zfill(4))
print(h.zfill(4))
print(i.zfill(4))

print("=" * 50)  # Separator

# upper()
j = "oSamA"
print(j.upper())

print("=" * 50)  # Separator

# lower()
k = "OSamA"
print(k.lower())

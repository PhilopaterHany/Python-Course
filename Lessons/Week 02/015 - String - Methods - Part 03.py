# --------------------------------
# -- String - Methods - Part 03 --
# --------------------------------

# index(SubString, Start, End)
a = "I Love Python"
print(a.index("P"))  # Index Number 7
print(a.index("P", 0, 10))  # Index Number 7
# print(a.index("P", 0, 5))  # If it didn't find the string, it returns an error
print("=" * 50)  # Separator

# find(SubString, Start, End)
b = "I Love Python"
print(b.find("P"))  # Index Number 7
print(b.find("P", 0, 10))  # Index Number 7
print(b.find("P", 0, 5))  # If it didn't find the string, it returns -1
print("=" * 50)  # Separator

# rjust(Width, Fill Char) - ljust(Width, Fill Char)
c = "Osama"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "Osama"
print(d.ljust(10))
print(d.ljust(10, "#"))

print("=" * 50)  # Separator

# splitlines()
e = """First Line
Second Line
Third Line"""
print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"
print(f.splitlines())

print("=" * 50)  # Separator

# expandtabs()
g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))
print("=" * 50)  # Separator

# istitle()
h = "I Love Python And 3G"
i = "I Love Python And 3g"
print(h.istitle())
print(i.istitle())
print("=" * 50)  # Separator

# isspace()
j = " "
k = ""
print(j.isspace())
print(k.isspace())
print("=" * 50)  # Separator

# isLower()
ll = 'i love python'
m = 'I Love Python'
print(ll.islower())
print(m.islower())
print("=" * 50)  # Separator

# isidentifier()
n = "osama_elzero"
o = "OsamaElzero100"
p = "Osama--Elzero100"
print(n.isidentifier())
print(o.isidentifier())
print(p.isidentifier())
print("=" * 50)  # Separator

# isalpha()
q = "AaaaaBbbbbb"
r = 'AaaaaBbbbbb111'
print(q.isalpha())
print(r.isalpha())
print("=" * 50)  # Separator

# isalnum()
s = "AaaaaBbbbbb"
t = "AaaaaBbbbbb111"
print(s.isalnum())
print(t.isalnum())

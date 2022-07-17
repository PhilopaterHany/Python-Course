# ----------------------------------
# -- Built-In Functions - Part 07 --
# ----------------------------------
# enumerate()
# help()
# reversed()
# ----------------------------------

# enumerate(iterable, start=0)
mySkills = ["Html", "Css", "Js", "PHP"]
mySkillsWithCounter = enumerate(mySkills, 20)
print(type(mySkillsWithCounter))
for counter, skill in mySkillsWithCounter:
    print(f"{counter} - {skill}")

print("=" * 50)  # Separator

# help()
print(help(print))

print("=" * 50)  # Separator

# reversed(iterable)
myString = "Elzero"
print(reversed(myString))
for letter in reversed(myString):
    print(letter)
for s in reversed(mySkills):
    print(s)

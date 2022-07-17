# -----------------
# -- Loop => For --
# --- Trainings ---
# -----------------

# Range
myRange = range(1, 101)
for number in myRange:
    print(number)

print("=" * 50)  # Separator

# Dictionary
mySkills = {
    "HTML": "98%",
    "CSS": "87%",
    "PHP": "63%",
    "JavaScript": "82%",
    "Python": "90%",
    "MySQL": "56%"
}
print(mySkills['JavaScript'])
print(mySkills.get("Python"))
print("=" * 50)  # Separator
for skill in mySkills:
    # print(skill)
    print(f"My Progress In {skill} Is: {mySkills.get(skill)}")

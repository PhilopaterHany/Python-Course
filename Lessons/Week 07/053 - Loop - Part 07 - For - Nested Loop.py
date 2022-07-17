# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

# List
students = ["Osama", "Ahmed", "Sayed", "Philopater"]
skills = ['HTML', 'CSS', 'JavaScript']
for name in students:  # Outer Loop
    print(f"{name} Skills Are: ")
    for skill in skills:  # Inner Loop
        print(f"-- {skill}")
    print("=" * 35)

# Dictionary
students = {
    "Osama": {
        "HTML": "98%",
        "CSS": "96%",
        "JavaScript": "99%"
    },
    "Ahmed": {
        "HTML": "81%",
        "CSS": "92%",
        "JavaScript": "73%"
    },
    "Sayed": {
        "HTML": "91%",
        "CSS": "63%",
        "JavaScript": "95%"
    },
    "Philopater": {
        "HTML": "98%",
        "CSS": "87",
        "JavaScript": "79%"
    }
}

print(students["Osama"])
print(students["Ahmed"])
print(students["Sayed"])
print(students["Philopater"])
print("=" * 50)  # Separator
print(students["Osama"]['CSS'])
print(students["Ahmed"]['CSS'])
print(students["Sayed"]['CSS'])
print(students["Philopater"]['CSS'])

print("=" * 50)  # Separator

for name in students:
    print(f"Skills and Progress For {name}: ")
    for skill in students[name]:
        print(f"-- {skill} => {students[name][skill]}")
    print("=" * 35)

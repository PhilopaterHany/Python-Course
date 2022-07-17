# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------

mySkills = {
    "HTML": "98%",
    "CSS": "90%",
    "JavaScript": "87%",
    "Python": "79%",
    "PHP": "64%"
}

print(mySkills.items())

print("=" * 50)  # Separator

for skill in mySkills:
    print(f"{skill} => {mySkills[skill]}")

print("=" * 50)  # Separator

for skill_key, skill_progress in mySkills.items():
    print(f"{skill_key} => {skill_progress}")

print("=" * 50)  # Separator

myUltimateSkills = {
    "HTML": {
        "Main": "98%",
        "PugJS": "88%"
    },
    "CSS": {
        "Main": "90%",
        "SCSS": "86%"
    }
}

for main_key, main_value in myUltimateSkills.items():
    print(f"{main_key} Progress Is: ")
    for child_key, child_value in main_value.items():
        print(f"-- {child_key} => {child_value}")

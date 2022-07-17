# -------------------------------------------------------
# -- Function - Packing & Unpacking Arguments **KWArgs --
# -------------------------------------------------------

def show_skills(*skills):
    print(type(skills))
    for skill in skills:
        print(f"{skill}")


show_skills("HTML", "CSS", "JavaScript")

print("=" * 50)  # Separator

mySkills = {
    'HTML': "98%",
    'CSS': "90%",
    'JavaScript': "87%",
    'Python': "82%",
    "PHP": "64%"
}


def show_skills(**skills):
    print(type(skills))
    for skill, value in skills.items():
        print(f"{skill} => {value}")


show_skills(**mySkills)

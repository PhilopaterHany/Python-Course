# -------------------------------------------------------
# -- Function - Packing & Unpacking Arguments Training --
# -------------------------------------------------------

myTuple = ("HTML", "CSS", "JavaScript")

mySkills = {
    'Python': "80%",
    'MySQL': "60%",
    'PHP': "70%"
}


def show_skills(name, *skills, **skillsWithProgres):
    print(f"Hello {name}, \nSkills Without Progress: ")
    for skill in skills:
        print(f"- {skill}")
    print("Skills With Progress: ")
    for skill_key, skill_value in skillsWithProgres.items():
        print(f"-- {skill_key} => {skill_value}")


show_skills("Osama", *myTuple, **mySkills)

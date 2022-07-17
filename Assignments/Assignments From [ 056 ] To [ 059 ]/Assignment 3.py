def show_skills(name="Unknown", *skills):
    name = name.strip().capitalize()
    if skills:
        print(f"Hello {name}, Your Skills:")
        for skill in skills:
            print(f"-- {skill}")
    else:
        print(f"Hello {name}, You Have No Skills To Show.")


show_skills("Osama", "SCSS", "PugJS", "TypeScript", "PHP", "MySQL")
print("=" * 50)  # Separator
show_skills("Philopater", "HTML", "CSS", "JavaScript", "Python")
print("=" * 50)  # Separator
show_skills("Ahmed")

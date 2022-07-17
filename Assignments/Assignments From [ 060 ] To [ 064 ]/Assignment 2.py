def get_people_scores(name="", **scores):
    name = name.strip().capitalize()
    if scores:
        if name:
            print(f"Hello {name}, This Is Your Score Table:")
        for subj, value in scores.items():
            print(f"-- {subj} => {value}")
    else:
        if name:
            print(f"Hello {name}, You Have No Scores To Show.")
        else:
            print("Sorry, No Input Was Given.")


get_people_scores("Osama", Chemistry=98, Biology=94, Math=86)
# Output:
# "Hello Osama, This Is Your Score Table:"
# "Chemistry => 98"
# "Biology => 94"
# "Math => 86"

print("=" * 50)  # Separator

get_people_scores("Philopater", Logic=77, Problems=71)
# Output:
# "Hello Philopater, This Is Your Score Table:"
# "Logic => 77"
# "Problems => 71"

print("=" * 50)  # Separator

get_people_scores(Logic=50, Problems=30)
# Output:
# "Logic => 50"
# "Problems => 30"

print("=" * 50)  # Separator

# Output => "Hello Ahmed, You Have No Scores To Show."
get_people_scores("Ahmed")

print("=" * 50)  # Separator

get_people_scores()  # Output => "Sorry, No Input Was Given."

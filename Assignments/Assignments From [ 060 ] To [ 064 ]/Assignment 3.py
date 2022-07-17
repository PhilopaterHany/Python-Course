scores_list = {
    "Chemistry": 98,
    "Biology": 96,
    "Math": 92
}


def get_the_scores(name="", **scores):
    if scores:
        if name:
            print(f"Hello {name} This Is Your Score Table:")
        for subj, value in scores.items():
            print(f"-- {subj} => {value}")
    else:
        if name:
            print(f"Hello {name}, You Have No Scores To Show.")
        else:
            print("No Input Was Given. Please Enter The Required Data.")


get_the_scores("Philopater", **scores_list)
# Output:
# Hello Philopater This Is Your Score Table:
# Chemistry => 98
# Biology => 96
# Math => 92

print("=" * 50)  # Separator

get_the_scores("Osama")  # Output => Hello Osama, You Have No Scores To Show.

print("=" * 50)  # Separator

get_the_scores(**scores_list)
# Output:
# Chemistry => 98
# Biology => 96
# Math => 92

print("=" * 50)  # Separator

get_the_scores()  # Output => No Input Was Given. Please Enter The Required Data.

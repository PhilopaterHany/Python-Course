def get_score(**skills):
    if skills:
        for skill, value in skills.items():
            print(f"-- {skill} => {value}")
    else:
        print("Sorry, No Input. Please Enter Your Skills.")


get_score(Chemistry=98, Biology=94, Math=86)
# Output:
# "-- Chemistry => 98"
# "-- Biology => 94"
# "-- Math => 86"

print("=" * 50)  # Separator

get_score(Logic=77, Problems=71)
# Output:
# "-- Logic => 77"
# "-- Problems => 71"

print("=" * 50)  # Separator

get_score(Logic=77, Problems=71)  # Output => Sorry, No Input. Please Enter Your Skills.

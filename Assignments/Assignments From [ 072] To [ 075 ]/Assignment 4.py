skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# Method 1
def remove_nums(ele):
    return type(ele) != int


filtered_skills = list(filter(remove_nums, skills))
filtered_skills.reverse()

for num, skill in enumerate(filtered_skills, 50):
    print(f"{num} => {skill}")

print("=" * 50)  # Separator

# Method 2
filtered_data = list(filter(lambda ele: type(ele) != int, skills))
filtered_data.reverse()
counter = 50
for skill in filtered_data:
    print(f"{counter} => {skill}")
    counter += 1

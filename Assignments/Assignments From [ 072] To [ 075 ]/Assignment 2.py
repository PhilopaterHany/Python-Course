friends_filter = ["Osama", "Wessam", "Philo", "Essam", "Gamal", "Othman"]


def get_names(ele):
    return ele.lower().endswith("m")
    # return ele[-1].lower() == "m"


names = filter(get_names, friends_filter)

for name in names:
    print(name)

print("=" * 50)  # Separator

for name in filter(lambda ele: ele.lower().endswith("m"), friends_filter):
    print(name)

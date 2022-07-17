friends_map = ["APhiloS", "BAhmedZ", "FSamehK", "LOsamaV"]


def remove_chars(ele):
    return ele[1:-1]


cleaned_list = map(remove_chars, friends_map)

for name in cleaned_list:
    print(name)

print("=" * 50)  # Separator

for name in map(lambda ele: ele[1:-1], friends_map):
    print(name)

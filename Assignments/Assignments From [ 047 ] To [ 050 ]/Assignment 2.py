friends = ["Osama", "Mohamed", "farah", "sarah", "Philopater"]

i = 0
j = 0
while i < len(friends):
    if friends[i][0].isupper():
        print(friends[i])
    else:
        j += 1
    i += 1
print(f"{i} Names Has Been Printed Successfully. {j} Names Has Been Ignored.")

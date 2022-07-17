friends = ("Osama", "Mohamed", "Philopater")

friends = list(friends)
friends[0] = "Elzero"
friends = tuple(friends)

print(friends)  # Output => ('Elzero', 'Mohamed', 'Philopater')
print(type(friends))  # Output => tuple
print(f"{len(friends)} Elements")  # Output => 3 Elements

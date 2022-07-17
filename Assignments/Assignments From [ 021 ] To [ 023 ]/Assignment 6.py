friends = ["Nasser", "Ahmed", "Osama", "Elzero", "Philopater"]

friends[0:2] = []
print(friends)  # Output => ['Osama', 'Elzero', 'Salem']

friends[-1:] = []
# Another Solution: friends.remove(friends[-1])
print(friends)  # Output => ['Osama', 'Elzero']

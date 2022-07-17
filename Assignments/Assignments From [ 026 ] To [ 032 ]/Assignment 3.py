my_set = {1, 2, 3}
letters = {"A", "B", "C"}


print(my_set) # Output => {1, 2, 3}

my_set.clear()
print(my_set)  # Output => set()

letters.discard("C")
my_set.update(letters)
print(my_set)  # Output => {"A", "B"}
my_set.discard("C")

nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums | letters)
print(nums.union(letters))
print(set(list(nums) + list(letters)))

nums.update(letters)
print(nums)

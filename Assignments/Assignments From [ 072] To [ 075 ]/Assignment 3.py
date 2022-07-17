from functools import reduce

nums = [2, 4, 6, 2]


def multiplication_product(acc, curr):
    return acc * curr


print(reduce(multiplication_product, nums))
print("=" * 50)  # Separator
print(reduce(lambda acc, curr: acc * curr, nums))

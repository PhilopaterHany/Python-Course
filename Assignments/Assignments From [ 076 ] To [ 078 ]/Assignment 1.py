import random

print(f"Random Number Between 10 and 50 => {random.randint(10, 50)}")

print("=" * 50)  # Separator

even = random.randint(2, 10)
while even % 2 != 0:
    even = random.randint(2, 10)
else:
    print(f"Random Even Number Between 2 and 10 => {even}")

print("=" * 50)  # Separator

odd = random.randint(2, 10)
while odd % 2 == 0:
    odd = random.randint(1, 9)
else:
    print(f"Random Odd Number Between 1 and 9 => {odd}")

print("=" * 50)  # Separator

print(dir(random))

numbers = [15, 81, 5, 17, 20, 21, 13]
numbers.sort(reverse=True)
counter = 0
for number in numbers:
    if number % 5 == 0:
        counter += 1
        print(f"{counter} => {number}")
else:
    print("All Numbers Have Been Printed Successfully.")

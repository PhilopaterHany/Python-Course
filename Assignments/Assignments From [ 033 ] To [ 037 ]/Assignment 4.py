num_one = 10
num_two = 20

result = num_one + num_two
print(result)  # Output => 30
print(result ** 3)  # Output => 27000
print((result ** 3) % 26000)  # Output => 1000
print(float(((result ** 3) % 26000) / 5))  # Output => 200.0
print(type(str(float(((result ** 3) % 26000) / 5))))  # Output => <class 'str'>

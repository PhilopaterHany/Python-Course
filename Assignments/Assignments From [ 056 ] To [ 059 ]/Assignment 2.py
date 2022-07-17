def addition(*nums):
    result = 0
    for num in nums:
        if num == 10:
            continue
        elif num == 5:
            result -= num
        else:
            result += num
    return result


print(addition(10, 20, 30, 10, 15))  # Output => 65
print(addition(10, 20, 30, 10, 15, 5, 100))  # Output => 160

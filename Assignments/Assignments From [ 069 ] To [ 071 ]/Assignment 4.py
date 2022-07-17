def my_all(arg):
    count = 0
    for ele in arg:
        if ele:
            count += 1
    # if count == len(arg):
    #     return True
    # else:
    #     return False
    return True if count == len(arg) else False


def my_any(arg):
    count = 0
    for ele in arg:
        if ele:
            count += 1
    # if count >= 1:
    #     return True
    # else:
    #     return False
    return True if count >= 1 else False


def my_min(arg):
    arg = list(arg)
    num = 0  # Any Number
    for ele in arg:
        if num > ele:
            num = ele
    return num


def my_max(arg):
    arg = list(arg)
    num = 0  # Any Number
    for ele in arg:
        if num < ele:
            num = ele
    return num


print(my_all((1, 2, 3)))  # Output => True
print(my_all([1, 2, 3, []]))  # Output => False
print("=" * 50)  # Separator
print(my_any((0, 1, [], False)))  # Output => True
print(my_any([(), 0, False]))  # Output => False
print("=" * 50)  # Separator
print(my_min([10, 100, -20, -100, 50]))  # Output => -100
print(my_min((10, 100, -20, -100, 50)))  # Output => -100
print("=" * 50)  # Separator
print(my_max([10, 100, -20, -100, 50, 700]))  # Output => 700
print(my_max((10, 100, -20, -100, 50, 700)))  # Output => 700

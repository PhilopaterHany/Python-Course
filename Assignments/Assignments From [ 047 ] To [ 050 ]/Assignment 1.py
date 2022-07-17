num = int(input("Enter A Random Number: ").strip()) - 1

if num > 0:
    i = 0
    while num >= 1:
        if num != 6:
            print(num)
            i += 1
        num -= 1
    print(f"{i} Numbers Has Been Printed Successfully.")
else:
    print(f"Sorry, The Number You Have Entered ({num}) Is Not Greater Than 0.")

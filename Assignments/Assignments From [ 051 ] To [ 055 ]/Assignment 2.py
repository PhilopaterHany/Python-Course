skip_list = [6, 8, 12]
for number in range(1, 21):
    if number in skip_list:
        continue
    else:
        print(str(number).zfill(2))
else:
    print("All Numbers Have Been Printed Successfully.")

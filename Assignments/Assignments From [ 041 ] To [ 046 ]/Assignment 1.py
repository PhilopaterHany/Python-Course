num1 = int(input("Enter The First Number: ").strip())
num2 = int(input("Enter The Second Number: ").strip())
operation = input(
    "Please Choose The Type Of The Operation (+,-,*,/,%)").strip()
operation_list = ["+", "-", "*", "/", "%"]

if operation in operation_list:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        result = num1 % num2
    print(f"{num1:,} {operation} {num2:,} = {result}")
else:
    print("Sorry, Unknown Operation.")

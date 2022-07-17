def calculate(num1, num2, operation="add"):
    if type(num1) != str and type(num2) != str:
        if operation.lower() == "add" or operation.lower() == "a":
            return num1 + num2
        elif operation.lower() == "subtract" or operation.lower() == "s":
            return num1 - num2
        elif operation.lower() == "multiply" or operation.lower() == "m":
            return num1 * num2
        else:
            return f"Invalid Operation ({operation})."
    else:
        return f"Invalid Input. Please Enter Numbers."


print(calculate(10, 20))  # Output => 30
print(calculate(10, 20, "AdD"))  # Output => 30
print(calculate(10, 20, "a"))  # Output => 30
print(calculate(10, 20, "A"))  # Output => 30

print("=" * 50)  # Separator

print(calculate(10, 20, "S"))  # Output => -10
print(calculate(10, 20, "subTRACT"))  # Output => -10

print("=" * 50)  # Separator

print(calculate(10, 20, "Multiply"))  # Output => 200
print(calculate(10, 20, "m"))  # Output => 200

print("=" * 50)  # Separator

print(calculate("elzero", "10", "A"))  # Output => Invalid Input. Please Enter Numbers.

print(calculate(40, 20, "division"))  # Output => Invalid Operation (division).

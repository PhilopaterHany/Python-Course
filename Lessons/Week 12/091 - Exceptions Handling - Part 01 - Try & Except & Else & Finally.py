# -----------------------------------
# --      Exceptions Handling      --
# -- Try & Except & Else & Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# -----------------------------------
# Else    => If No Errors
# Finally => Run The Code
# -----------------------------------

number = int(input("Write Your Age: "))

print(number)
print(type(number))

try:  # Try The Code and Test Errors
    number = int(input("Write Your Age: "))
    print("Good, This Is Integer From Try")
except:  # Handle The Errors If Its Found
    print("Bad, This is Not Integer")
else:  # If Theres No Errors
    print("Good, This Is Integer From Else")
finally:
    print("Print From Finally Whatever Happens")


try:
    # print(10 / 0)
    # print(x)
    print(int("Hello"))
except ZeroDivisionError:
    print("Can't Divide")
except NameError:
    print("Identifier Is Not Found")
except ValueError:
    print("Value Error Elzero")
except:
    print("An Error Happens")

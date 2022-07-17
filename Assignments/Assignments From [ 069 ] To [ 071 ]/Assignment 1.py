values = (0, 1, 2)

if any(values):  # If Any Value In "values" Tuple Equals True, then:
    # Create A Variable Named "my_var" and It Equals 0
    my_var = 0

# Declaring "my_list" Variable
my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# If my_list[0] my_list[1] my_list[2] my_list[3] Are True => True
# OR
# If my_list Elements till index 5 Are True => False becuase my_var equals 0
# OR
# If All Of my_list Elements Are True => False becuase my_var equals 0
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
    print("Good")
else:
    print("Bad")

# Output => Good

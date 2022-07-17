# --------------------------------------------------------------------------------------
# ------------------------------------- Generators -------------------------------------
# --------------------------------------------------------------------------------------
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Supports Iteration and Returns Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next() It Continues From Where It Stopped Not From The Begining
# [5] When It Is Called, It Does Not Start Automatically, It Gives You The Control Only
# --------------------------------------------------------------------------------------

def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4


myGen = myGenerator()

print(next(myGen), end=" ")
print("Hello From Python")
print(next(myGen), end=" ")

for number in myGen:
    print(number)

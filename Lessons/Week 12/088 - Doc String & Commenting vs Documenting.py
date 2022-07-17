# --------------------------------------------------------------
# ----------- Doc String & Commenting vs Documenting -----------
# --------------------------------------------------------------
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From Help and Doc Attributes
# [3] Made For Understanding The Functionality Of A Complex Code
# [4] Theres One Line and Multiple Line Doc Strings
# --------------------------------------------------------------

def elzero_function(name):
    """
    Elzero Function
        It Say Hello From Elzero
    Parameter:
        name => Person Name That Use Function
    Return:
        Return Hello Message To The Person
    """
    print(f"Hello {name} From Elzero")


elzero_function("Ahmed")
print(dir(elzero_function))
print(elzero_function.__doc__)
help(elzero_function)

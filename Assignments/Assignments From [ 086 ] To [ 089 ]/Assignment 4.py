# Write Function With Help To Get The Output
def say_hello_to(name):
    """
    "Parameter(someone) => Person Name"
    "Function To Say Hello To Anyone"
    """
    return f"Hello {name} !"


print(say_hello_to("Osama"))  # Output => "Hello Osama !"
print(say_hello_to("Philopater"))  # Output => "Hello Philopater !"
# print(dir(say_hello_to))
print(say_hello_to.__doc__)
# help(say_hello_to)

# Create Your Decorator Here
def my_decorator(func):
    def sugar_adder():
        print("Sugar Added From Decorator")
        func()
        print("#" * 26)
    return sugar_adder


@my_decorator
def make_tea():
    print("Your Tea Is Ready!")


@my_decorator
def make_coffee():
    print("Your Coffee Is Ready!")


make_tea()
make_coffee()

# Output:
# "Sugar Added From Decorator"
# "Your Tea Is Ready!"
# "####################"
# "Sugar Added From Decorator"
# "Your Coffee Is Ready!"
# "####################"

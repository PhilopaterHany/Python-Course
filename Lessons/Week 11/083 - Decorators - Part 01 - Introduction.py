# -------------------------------------------------------------------------------------------
# ----------------------------------- Decorators => Intro -----------------------------------
# -------------------------------------------------------------------------------------------
# [1] Sometimes It Is Called Meta Programming
# [2] Everything In Python Is An Object Even Functions
# [3] Decorator Takes A Function and Add Some Functionality Then Returns It
# [4] Decorator Wraps Other Function and Enhances Its Behaviour
# [5] Decorator Is A Higher Order Function (Function That Accepts A Function As A Parameter)
# -------------------------------------------------------------------------------------------

def myDecorator(func):  # Decorator
    def nestedFunc():  # Any Name, It Is Just For Decoration
        print("Before")  # Message From Decorator
        func()  # Execute The Function
        print("After")  # Message From Decorator
    return nestedFunc  # Return All Data


@myDecorator
def sayHello():
    print("Hello From Say Hello Function")


@myDecorator
def sayHowAreYou():
    print("Hello From Say How Are You Function")


afterDecoration = myDecorator(sayHello)
afterDecoration()
sayHello()
print("=" * 50)  # Separator
sayHowAreYou()

# myFriends = ["Ahmed", "Osama", "Sayed"]

# def sayHello(SomePeople) -> list:
#   for Someone in SomePeople:
#     print(f"Hello {Someone}")

# sayHello(myFriends)

"""
This Is The File's Docstring
"""

my_friends = ["Ahmed", "Osama", "Sayed"]


def say_hello(some_people) -> list:
    """
    This Function Says Hello To Each Person In A List
    """
    for someone in some_people:
        print(f"Hello {someone}")


say_hello(my_friends)

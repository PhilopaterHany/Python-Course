# ------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# ------------------------------------------------

class Food:  # Base Class
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"{self.name} Is Created From Base Class")

    def eat(self):
        print("Eat Method From Base Class")


class Apple(Food):  # Derived Class
    def __init__(self, name, price, amount):
        # Food.__init__(self, name)  # Create Instance From Base Class
        super().__init__(name, price)
        self.amount = amount
        print(f"{self.name} Is Created From Derived Class And Price Is {self.price} And Amount Is {self.amount}")

    def get_from_tree(self):
        print("Get From Tree From Derived Class")


# food_one = Food("Pizza")
food_two = Apple("Pizza", 150, 500)
food_two.eat()
food_two.get_from_tree()

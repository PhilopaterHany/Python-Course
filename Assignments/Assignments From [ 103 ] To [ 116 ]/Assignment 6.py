class A:
    def __init__(self, one):
        self.one = one


class B:
    def __init__(self, two):
        self.two = two


class C:
    def __init__(self, three):
        self.three = three


class Text(A, B, C):
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three

    def show_name(self):
        return f"Your Name Is {self.one}{self.two}{self.three}"


the_name = Text("El", "ze", "ro")

print(the_name.show_name())

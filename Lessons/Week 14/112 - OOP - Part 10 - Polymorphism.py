# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# -------------------------------------------------

n1 = 10
n2 = 20

print(n1 + n2)

s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2)

print(len([1, 2, 3, 4, 5, 6]))
print(len("Osama Elzero"))
print(len({"Key_One": 1, "Key_Two": 2}))


class A:
    def do_something(self):
        print("From Class A")
        raise NotImplementedError("Derived Class Must Implement This Method")


class B(A):
    def do_something(self):
        print("From Class B")


class C(A):
    def do_something(self):
        print("From Class C")


my_instance = B()
my_instance.do_something()

# ----------------------------------------------------------------------------------------
# -------------- Object Oriented Programming => ABCs => Abstract Base Class --------------
# ----------------------------------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# ----------------------------------------------------------------------------------------

from abc import ABCMeta, abstractmethod


class Programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass

    @abstractmethod
    def has_name(self):
        pass


class Python(Programming):
    def has_oop(self):
        return "Yes"


class Pascal(Programming):
    def has_oop(self):
        return "No"

    def has_name(self):
        return "Pascal"


one = Pascal()

print(one.has_oop())
print(one.has_name())

# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------

from elzero import say_hello as ss
from elzero import say_hello
import elzero as ee
import elzero
import sys

sys.path.append(r"D:\Games")
print(sys.path)
print(dir(elzero))

elzero.say_hello("Osama")
elzero.say_hello("Mohamed")
elzero.say_hello("Philopater")

elzero.say_how_are_you("Osama")
elzero.say_how_are_you("Mohamed")
elzero.say_how_are_you("Philopater")

# Alias
ee.say_hello("Osama")
ee.say_hello("Mohamed")
ee.say_hello("Philopater")

ee.say_how_are_you("Osama")
ee.say_how_are_you("Mohamed")
ee.say_how_are_you("Philopater")

say_hello("Osama")

ss("Osama")

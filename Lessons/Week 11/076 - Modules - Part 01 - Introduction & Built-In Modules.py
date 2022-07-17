# -----------------------------------------------------
# ------------ Modules => Built-In Modules ------------
# -----------------------------------------------------
# [1] Module is A File That Contains A Set Of Functions
# [2] You Can Import A Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Save Your Time
# -----------------------------------------------------

# Import Main Module
from random import randint, random
import random
print(random)
print(f"Print Random Float Number {random.random()}")

# Show All Functions Inside Module
print(dir(random))

# Import One Or Two Functions From Module
print(f"Print Random Float {random()}")
print(f"Print Random Integer {randint(100, 900)}")

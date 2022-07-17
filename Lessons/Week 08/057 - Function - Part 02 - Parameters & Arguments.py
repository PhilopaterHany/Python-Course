# -----------------------------------------
# --- Function - Parameters & Arguments ---
# -----------------------------------------

a, b, c = "Osama", "Ahmed", "Sayed"

print(f"Hello {a}")
print(f"Hello {b}")
print(f"Hello {c}")

# def                     => Function Keyword [Define]
# say_hello()             => Function Name
# name                    => Parameter
# print(f"Hello {name}")  => Task
# say_hello("Ahmed")      => Ahmed is The Argument

print("=" * 50)  # Separator


def say_hello(n):
    print(f"Hello {n}")


say_hello(a)
say_hello(b)
say_hello(c)

print("=" * 50)  # Separator


def addition(n1, n2):
    print(n1 + n2)


addition(100, 300)
addition(-50, 100)

print("=" * 50)  # Separator


def addition(n1, n2):
    if type(n1) != int or type(n2) != int:
        print("Only Integers Are Allowed")
    else:
        print(n1 + n2)


addition(100, 500)

print("=" * 50)  # Separator


def full_name(first, middle, last):
    print(
        f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")


full_name("   osama   ", 'mohamed', "elsayed")

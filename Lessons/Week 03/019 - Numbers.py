# -------------
# -- Numbers --
# -------------

# Integer
print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))
print("=" * 50)  # Separator

# Float
print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))
print("=" * 50)  # Separator

# Complex
my_complex_number = 5+6j
print(type(my_complex_number))
print("Real Part Is: {}".format(my_complex_number.real))
print("Imaginary Part Is: {}".format(my_complex_number.imag))
print("=" * 50)  # Separator
# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

print(100)
print(float(100))
print(complex(100))
print("=" * 50)  # Separator
print(10.50)
print(int(10.50))
print(complex(10.50))
print("=" * 50)  # Separator
print(10+9j)
# print(int(10+9j))  # Error

# --------------------------------------------------------
# ------------------------- List -------------------------
# --------------------------------------------------------
# [1] List Items Are Enclosed in Square Brackets []
# [2] List Are Ordered, Use Index To Access Item
# [3] List Are Mutable => You Can Add, Delete & Edit Items
# [4] List Items Are Not Unique (Items Can Be Repeated)
# [5] List Can Contain Different Data Types
# --------------------------------------------------------

my_awesome_list = ["One", "Two", "One", 1, 100.5, True]

print(my_awesome_list)  # Whole List
print(my_awesome_list[1])  # "Two"
print(my_awesome_list[-1])  # True
print(my_awesome_list[-3])  # 1

print("=" * 50)  # Separator

print(my_awesome_list[1:4])  # ['Two', 'One', 1]
print(my_awesome_list[:4])  # ['One', 'Two', 'One', 1]
print(my_awesome_list[1:])  # ['Two', 'One', 1, 100.5, True]

print("=" * 50)  # Separator

print(my_awesome_list[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
print(my_awesome_list[::2])  # ['One', 'One', 100.5]

print("=" * 50)  # Separator

print(my_awesome_list)
# my_awesome_list[1] = 2
# my_awesome_list[-1] = False
my_awesome_list[0:3] = ["A"]
print(my_awesome_list)

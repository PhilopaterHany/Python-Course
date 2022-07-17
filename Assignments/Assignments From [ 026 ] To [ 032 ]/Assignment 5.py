my_dict = {
    "HTML": 98,
    "CSS": 87,
    "JavaScript": 74,
}
print(f"{list(my_dict.keys())[0]} Progress Is {list(my_dict.values())[0]}")
print(f"{list(my_dict.keys())[1]} Progress Is {list(my_dict.values())[1]}")
print(f"{list(my_dict.keys())[2]} Progress Is {list(my_dict.values())[2]}")

my_dict.update({"Python": 65})

print(f"{list(my_dict.keys())[3]} Progress Is {list(my_dict.values())[3]}")

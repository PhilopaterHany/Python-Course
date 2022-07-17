# ----------------------------------------------------------------------
# ----------------------------- Dictionary -----------------------------
# ----------------------------------------------------------------------
# [1] Dict Items Are Enclosed in Curly Braces {}
# [2] Dict Items Are {Key: Value}
# [3] Dict Key Must Be Immutable => (Number, String, Tuple) List Is Not
# [4] Dict Value Can Be Any Data Type
# [5] Dict Key Must Be Unique
# [6] Dict Is Not Ordered, You Can Access Its Elements With Key
# ----------------------------------------------------------------------

# Dictionary
user = {
    "name": "Osama",
    "age": 36,
    "country": "Egypt",
    "skills": ["Html", "Css", "JS"],
    "rating": 10.5
}
print(user)
print(user['country'])
print(user.get("country"))

print(user.keys())
print(user.values())

print("=" * 50)  # Separator

# Two-Dimensional Dictionary
languages = {
    "One": {
        "name": "Html",
        "progress": "80%"
    },
    "Two": {
        "name": "Css",
        "progress": "90%"
    },
    "Three": {
        "name": "Js",
        "progress": "90%"
    }
}
print(languages)
print(languages['One'])
print(languages['Three']['name'])
print("=" * 50)  # Separator

# Dictionary Length
print(len(languages))
print(len(languages["Two"]))
print("=" * 50)  # Separator

# Create Dictionary From Variables
framework_one = {
    "name": "Vue.js",
    "progress": "80%"
}
framework_two = {
    "name": "React.js",
    "progress": "80%"
}
framework_three = {
    "name": "Angular",
    "progress": "80%"
}
all_framework = {
    "one": framework_one,
    "two": framework_two,
    "three": framework_three
}
print(all_framework)

# ----------------------------------------------------------------------
# ------------ Object Oriented Programming => Magic Methods ------------
# ----------------------------------------------------------------------
# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
#           Called When We Use the Built-in len() Function on the Object
# ----------------------------------------------------------------------

class Skill:
    def __init__(self):
        self.skills = ["Html", "Css", "Js"]

    def __str__(self):
        return f"These Are My Skills => {self.skills}"

    def __len__(self):
        return len(self.skills)


profile = Skill()
print(profile)
print(len(profile))

profile.skills.append("PHP")
profile.skills.append("MySQL")

print(len(profile))

print(profile.__class__)
my_string = "Osama"
print(type(my_string))
print(my_string.__class__)
print(dir(str))
print(str.upper(my_string))

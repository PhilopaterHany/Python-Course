class User:
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

    def full_details(self):
        self.title = "Mr" if self.gender == "Male" else "Mrs"
        return f"Hello {self.title} {self.fname} {self.lname[0]}. [{str(40 - self.age).zfill(2)}] Years To Reach Age Of 40"


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details())  # Output => Hello Mr Osama M. [02] Years To Reach Age Of 40
print(user_two.full_details())  # Output => Hello Mrs Eman O. [15] Years To Reach Age Of 40

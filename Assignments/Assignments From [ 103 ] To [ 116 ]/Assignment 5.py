# Main Class
class Members:
    def __init__(self, n, p):
        self.name = n
        self.permission = p

    def show_info(self):
        return f"Your Name Is {self.name} And You Are A {self.permission}."


# Create Admin Class Here
class Admins(Members):
    def __init__(self, n, p):
        self.name = n
        self.permission = p

    def show_info(self):
        return f"Your Name Is {self.name} And You Are An {self.permission}."


# Create Moderators Class Here
class Moderators(Admins):
    def __init__(self, n, p):
        self.name = n
        self.permission = p

    def show_info(self):
        return f"Your Name Is {self.name} And You Are A {self.permission}."


member_one = Admins("Osama", "Admin")
member_two = Moderators("Philopater", "Moderator")
member_three = Members("Mohamed", "Member")


print(member_one.show_info())  # Output => Your Name Is Osama And You Are An Admin.

print(member_two.show_info())  # Output => Your Name Is Philopater And You Are A Moderator.

print(member_three.show_info())  # Output => Your Name Is Mohamed And You Are A Member.

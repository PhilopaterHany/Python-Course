# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 1 --
# -----------------------------------------------------

# Input Big Message
input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add A New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose An Option: """

# Input Option Choose
user_input = input(input_message).strip().lower()

# Command List
commands_list = ["s", "a", "d", "u", "q"]

# Define The Methods
def show_skills():
    print("Show Skills")


def add_skill():
    print("Add Skill")


def delete_skill():
    print("Delete Skill")


def update_skill():
    print("Update Skill Progress")


# Check If Command Is Exists
if user_input in commands_list:
    print(f"Command Found {user_input}")
    if user_input == "s":
        show_skills()
    elif user_input == "a":
        add_skill()
    elif user_input == "d":
        delete_skill()
    elif user_input == "u":
        update_skill()
    else:
        print("Application Has Been Closed.")
else:
    print(f"Sorry, This Command \"{user_input}\" Is Not Found.")

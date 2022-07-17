# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 2 --
# -----------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

# Commit and Close Method
def commit_and_close():
    # Save (Commit) Changes
    db.commit()

    # Close Database
    db.close()
    print("Connection To Database Is Closed")


# My User ID
uid = 2

# Input Big Message
input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""

# Input Option Choose
user_input = input(input_message).strip().lower()

# Command List
commands_list = ["s", "a", "d", "u", "q"]

# Define The Methods
def show_skills():
    print("Show Skills")
    commit_and_close()


def add_skill():
    sk = input("Write Skill Name: ").strip().capitalize()
    prog = input("Write Skill Progress ").strip()
    cr.execute(f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")
    commit_and_close()


def delete_skill():
    sk = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")
    commit_and_close()


def update_skill():
    print("Update Skill Progress")
    commit_and_close()


# Check If Command Is Exists
if user_input in commands_list:
    # print(f"Command Found {user_input}")
    if user_input == "s":
        show_skills()
    elif user_input == "a":
        add_skill()
    elif user_input == "d":
        delete_skill()
    elif user_input == "u":
        update_skill()
    else:
        print("App Is Closed.")
else:
    print(f"Sorry This Command \"{user_input}\" Is Not Found")

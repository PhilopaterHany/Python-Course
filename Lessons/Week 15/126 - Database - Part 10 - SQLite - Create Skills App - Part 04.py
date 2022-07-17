# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 4 --
# -----------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()


def commit_and_close():
    """Commit Changes and Close Connection To Database"""
    db.commit()  # Save (Commit) Changes
    db.close()  # Close Database
    print("Connection To Database Is Closed")


# My User ID
uid = 1

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
    cr.execute(f"select * from skills where user_id = '{uid}'")
    results = cr.fetchall()
    print(f"You Have {len(results)} Skills.")
    if len(results) > 0:
        print("Showing Skills With Progress: ")
    for row in results:
        print(f"Skill => {row[0]},", end=" ")
        print(f"Progress => {row[1]}%")
    commit_and_close()


def add_skill():
    sk = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}'")
    results = cr.fetchone()
    if results == None:  # Theres No Skill With This Name In Database
        prog = input("Write Skill Progress ").strip()
        cr.execute(f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")
    else:  # Theres A Skill With This Name in Database
        print("You Cannot Add It")
    commit_and_close()


def delete_skill():
    sk = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")
    commit_and_close()


def update_skill():
    sk = input("Write Skill Name: ").strip().capitalize()
    prog = input("Write The New Skill Progress ").strip()
    cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")
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
        commit_and_close()
else:
    print(f"Sorry This Command \"{user_input}\" Is Not Found")

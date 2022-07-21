# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 3 --
# -----------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("Lessons/Week 15/app.db")

# Setting Up The Cursor
cr = db.cursor()


def commit_and_close():
    """Commit Changes and Close Connection To Database"""
    db.commit()  # Save (Commit) Changes
    db.close()  # Close Database
    print("Connection To Database Has Been Closed.")


# My User ID
uid = 2

# Input Big Message
input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add A New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option: """

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
        print(f"{row[0]} => {row[1]}%")
        print("=" * 50)  # Separator
    commit_and_close()


def add_skill():
    sk = input("Write Skill Name: ").strip().capitalize()
    prog = input("Write Skill Progress: ").strip()
    cr.execute(f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")
    print(f"\"{sk}\" Skill Has Been Added Successfully With Progress {prog}%.")
    commit_and_close()


def delete_skill():
    sk = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")
    print(f"\"{sk}\" Skill Has Been Deleted Successfully.")
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
        print("Application Has Been Closed.")
        commit_and_close()
else:
    print(f"Sorry This Command \"{user_input}\" Is Not Found")

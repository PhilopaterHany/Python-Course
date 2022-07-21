# --------------------------------------------
# -- Databases => SQLite => Update & Delete --
# --------------------------------------------

# Import SQLite Module
import sqlite3

# Creating Database And Connect
db = sqlite3.connect("Lessons/Week 15/app.db")

# Setting Up The Cursor
cr = db.cursor()

# Updating Data
# cr.execute("update users set name = 'Mahmoud' where user_id = 4")
# cr.execute("update users set name = 'Sayed' where user_id = 5")
# cr.execute("update users set name = 'Ameer' where user_id = 6")

# Deleting Data
cr.execute("delete from users where user_id = 4")

# Fetching Data
cr.execute("select * from users")

for user in cr.fetchall():
    print(user)

# Saving (Commit) Changes
db.commit()

# Closing Database
db.close()

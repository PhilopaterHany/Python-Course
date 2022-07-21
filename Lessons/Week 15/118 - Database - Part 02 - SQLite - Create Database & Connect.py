# ------------------------------------------------------
# -- Databases => SQLite => Create Database & Connect --
# ------------------------------------------------------
# - Connect
# - Execute
# - Close
# ------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("Lessons/Week 15/app.db")

# Create The Tables and Fields
db.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# Close Database
db.close()

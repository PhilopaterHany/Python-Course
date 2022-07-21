# --------------------------------------------------------------------------------------------
# -------------------- Databases => SQLite => Retrieve Data From Database --------------------
# --------------------------------------------------------------------------------------------
# - fetchone => returns a single record or None if no more rows are available
# - fetchall => fetches all the rows of a query result. It returns all the rows
#               as a list of tuples. An empty list is returned if there is no record to fetch
# - fetchmany(size) =>
# --------------------------------------------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("Lessons/Week 15/app.db")

# Setting Up The Cursor
cr = db.cursor()

# Create The Tables and Fields
# cr.execute("create table if not exists users (user_id integer, name text)")
# cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# Inserting Data (Commented Because We Have Already Inserted Data In The Previous Lesson)
# my_list = ["Philopater", "Osama", "Mohamed", "Ali", "Farah", "Sarah", "Mona"]
# for key, user in enumerate(my_list):
#     cr.execute(f"insert into users(user_id, name) values({key + 1}, '{user}')")

# Fetching & Printing Data
cr.execute("select * from users")

for user in cr.fetchall():
    print(user)

# print(cr.fetchall())
# print(cr.fetchmany(2))

# Save (Commit) Changes
db.commit()

# Close Database
db.close()

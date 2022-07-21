# --------------------------------------------------------------------------
# ------------ Databases => SQLite => Insert Data Into Database ------------
# --------------------------------------------------------------------------
# - cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# - commit => Save All Changes
# --------------------------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("Lessons/Week 15/app.db")

# Setting Up The Cursor
cr = db.cursor()

# Create The Tables and Fields
cr.execute("create table if not exists users (user_id integer, name text)")
cr.execute(
    "create table if not exists skills (name text, progress integer, user_id integer)")

# Inserting Data
# cr.execute("insert into users(user_id, name) values(1, 'Philopater')")
# cr.execute("insert into users(user_id, name) values(2, 'Osama')")
# cr.execute("insert into users(user_id, name) values(3, 'Mohamed')")
# cr.execute("insert into users(user_id, name) values(4, 'Ali')")
# cr.execute("insert into users(user_id, name) values(5, 'Farah')")
# cr.execute("insert into users(user_id, name) values(6, 'Sarah')")
# cr.execute("insert into users(user_id, name) values(7, 'Farida')")

my_list = ["Philopater", "Osama", "Mohamed", "Ali", "Farah", "Sarah", "Farida"]
for key, user in enumerate(my_list):
    cr.execute(f"insert into users(user_id, name) values({key + 1}, '{user}')")

# Save (Commit) Changes
db.commit()

# Close Database
db.close()

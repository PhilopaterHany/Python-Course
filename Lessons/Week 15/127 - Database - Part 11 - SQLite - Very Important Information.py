# --------------------------------------------------------
# -- Databases => SQLite => Very Important Informations --
# --------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

my_tuple = ('Pascal', '65', 4)

# Inserting Data
# cr.execute("insert into skills values(?, ?, ?)", my_tuple)

# Fetch Data From Database
# cr.execute("select * from skills order by name limit 3 offset 2")
# cr.execute("select * from skills where user_id > 1")
cr.execute("select * from skills where user_id not in(1, 2, 3)")
# Assign Data To Variable
results = cr.fetchall()

# Loop On Results
for row in results:
    print(f"Skill Name => {row[0]},", end=" ")
    print(f"Skill Progress => {row[1]},", end=" ")
    print(f"User ID => {row[2]}")

# Save (Commit) Changes
db.commit()

# Close Database
db.close()

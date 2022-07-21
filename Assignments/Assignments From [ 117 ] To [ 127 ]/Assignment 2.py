import sqlite3

db = sqlite3.connect("Assignments/Assignments From [ 117 ] To [ 127 ]/elzero.db")
cr = db.cursor()

cr.execute("create table users (id integer UNIQUE, name text UNIQUE, birthdate date UNIQUE, email text UNIQUE)")

db.commit()
db.close()

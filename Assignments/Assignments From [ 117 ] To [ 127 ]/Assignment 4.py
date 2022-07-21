import sqlite3

db = sqlite3.connect("Assignments/Assignments From [ 117 ] To [ 127 ]/elzero.db")
cr = db.cursor()

cr.execute("select * from users order by id desc limit 1")
result = cr.fetchone()
print(result)

db.commit()
db.close()

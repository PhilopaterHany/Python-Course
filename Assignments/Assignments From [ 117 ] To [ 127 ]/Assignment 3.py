import sqlite3

db = sqlite3.connect("Assignments/Assignments From [ 117 ] To [ 127 ]/elzero.db")
cr = db.cursor()

cr.execute("insert into users(id , name , birthdate , email) values(1 ,'Ali','11/04/2005','a@elzero.org')")
cr.execute("insert into users(id , name , birthdate , email) values(2 ,'Osama','25/10/1982','o@elzero.org')")
cr.execute("insert into users(id , name , birthdate , email) values(3 ,'Mohamed','05/03/1991','m@elzero.org')")
cr.execute("insert into users(id , name , birthdate , email) values(4 ,'Sayed','09/06/1987','s@elzero.org')")
cr.execute("insert into users(id , name , birthdate , email) values(5 ,'Philopater','04/08/2005','p@elzero.org')")

db.commit()
db.close()

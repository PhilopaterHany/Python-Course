import sqlite3

db = sqlite3.connect("Assignments/Assignments From [ 117 ] To [ 127 ]/elzero.db")
cr = db.cursor()

def show_skills():
    cr.execute("select * from users")
    result = cr.fetchall()
    print("Showing Others Data: ")
    for row in result:
        print(f"ID => {row[0]}")
        print(f"Name => {row[1]}")
        print(f"Birthdate => {row[2]}")
        print(f"Email => {row[3]}")
        print("=" * 50)  # Separtaor

def delete_user():
    id = input("Write User ID: ")
    cr.execute("select * from users where id = ?", id)
    result = cr.fetchone()
    if result == None:
        print("Sorry, User ID Is Not Found.")
    else:
        cr.execute("delete from users where id = ?", id)
        print("User Has Been Deleted Successfully.")
        show_skills()

delete_user()

db.commit()
db.close()

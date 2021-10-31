import sqlite3

with sqlite3.connect("company.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
    id integer PRIMARY KEY,
    name text NOT NULL,
    dept text NOT NULL,
    salary integer);""")

# cursor.execute("""INSERT INTO employees(id, name, dept, salary)
#     VALUES("1", "Bob", "Sales", "25000")""")
# db.commit()

newID = input("Enter ID number : ")
newName = input("Enter Name : ")
newDept = input("Enter Department : ")
newSalary = input("Enter Salary : ")

cursor.execute("""INSERT INTO employees(id, name, dept, salary)
        VALUES(?,?,?,?)""",(newID, newName, newDept, newSalary))
db.commit()

cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())

db.close()    
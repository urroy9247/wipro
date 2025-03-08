import MySQLdb

conn = MySQLdb.connect (
    host = "localhost",
    user = "root",
    passwd = "rps@123",
    db = "rps"
)

mycursor = conn.cursor()

query = "CREATE TABLE dept ( deptid int PRIMARY KEY, deptname VARCHAR(50))"

mycursor.execute(query)

conn.commit()

print('Table dept created successfully')
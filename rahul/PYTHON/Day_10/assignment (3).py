import MySQLdb

conn = MySQLdb.connect(
    host = 'localhost',
    user  = 'root',
    passwd = 'rps@123',
    db = 'rps'
)

mycursor = conn.cursor()

query = "CREATE TABLE emp ( empid int primary key, empname VARCHAR(15), deptID INT NULL, foreign key (deptID) references dept(deptid))"

mycursor.execute(query)

conn.commit()

print('Table created successfully')
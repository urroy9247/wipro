import MySQLdb

conn = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'rps@123',
    db = 'rps'
)

mycursor = conn.cursor()

data = [(100,'IT'),(200,'HR'),(300,'Sales'),(400,'admin')]

query = "INSERT INTO dept (deptid ,deptname) values (%s ,%s)"


mycursor.executemany(query,data)
conn.commit()
print('Inserted data')

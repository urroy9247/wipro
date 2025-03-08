import MySQLdb

conn = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'rps@123',
    db = 'rps'
)

mycursor = conn.cursor()

query = "INSERT INTO emp(empid,empname,deptID) VALUES (1,'A',100),(2,'B',100),(3,'C',200),(4,'D',400),(5,'E',NULL)"



mycursor.execute(query)

conn.commit()
print('Inserted emp data')
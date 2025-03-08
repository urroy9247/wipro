import MySQLdb
 
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="rps@123",
    db="rps"
)

mycursor = connection.cursor()

# Executing the SQL query to create a new table
mycursor.execute("select d.deptname from dept d left join emp e on d.deptID = e.deptid where e.empid is null")

# Commit the transaction (optional, not needed for CREATE TABLE)
result = mycursor.fetchall()
for i in result:
    print(i)

mycursor.execute("select empname from emp where deptID is null")

result = mycursor.fetchall()
for i in result:
    print(i)
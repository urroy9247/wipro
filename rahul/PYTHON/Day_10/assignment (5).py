import MySQLdb
 
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="rps@123",
    db="rps"
)

mycursor = connection.cursor()

# Executing the SQL query to create a new table
mycursor.execute("select deptID,group_concat(empname) as employes from emp group by deptID having count(deptID)>1")

# Commit the transaction (optional, not needed for CREATE TABLE)
result = mycursor.fetchall()
for i in result:
    print(i)
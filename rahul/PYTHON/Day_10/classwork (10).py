import MySQLdb
 
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="rps@123",
    db="rps"
)

mycursor = connection.cursor()
 
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
 
mycursor.execute(sql)
 
connection.commit()
 
print(mycursor.rowcount, "record(s) deleted")
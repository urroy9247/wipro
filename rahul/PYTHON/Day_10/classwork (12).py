import MySQLdb
 
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="rps@123",
    db="rps"
)

mycursor = connection.cursor()


sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
 
mycursor.execute(sql)
 
connection.commit()
 
print(mycursor.rowcount, "record(s) affected")
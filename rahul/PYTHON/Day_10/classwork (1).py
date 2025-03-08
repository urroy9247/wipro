import MySQLdb
 
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="rps@123",
    db="rps"
)
mycursor = connection.cursor()  # cursor is an  object to execute sql statements
 
 
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
 
val = ("John", "Highway 21")
 
mycursor.execute(sql, val)
 
connection.commit()
 
print(mycursor.rowcount, "record inserted.")
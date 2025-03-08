import MySQLdb
 
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="rps@123",
    db="rps"
)

mycursor = connection.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")
 
myresult = mycursor.fetchall()
 
for x in myresult:
  print(x)
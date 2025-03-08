import MySQLdb
 
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="rps@123",
    db="rps"
)

mycursor = connection.cursor()

sql = "SELECT * FROM customers order by name desc;"
 
mycursor.execute(sql)
 
myresult = mycursor.fetchall()
 
for x in myresult:

  print(x)
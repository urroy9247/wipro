import MySQLdb
 
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="rps@123",
    db="rps"
)

mycursor = connection.cursor()

sql = "SELECT * FROM customers WHERE address = %s"

adr = ("Yellow Garden 2", )
 
mycursor.execute(sql, adr)
 
myresult = mycursor.fetchall()
 
for x in myresult:

  print(x)
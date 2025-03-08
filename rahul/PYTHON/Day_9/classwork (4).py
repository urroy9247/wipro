import MySQLdb
 
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="rps@123",
    db="rps"
)
 
cursor = connection.cursor()
cursor.execute("select database();")
db = cursor.fetchone()
 
if db:
    print("You're connected to database: ", db)
else:
    print('Not connected.')

    cursor = db.cursor()
 
cursor.execute("insert into customers(name,address) values ('rahul','kcl')")
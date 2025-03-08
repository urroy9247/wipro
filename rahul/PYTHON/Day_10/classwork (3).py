import MySQLdb
 
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="rps@123",
    db="rps"
)

mycursor = connection.cursor()

# Executing the SQL query to create a new table
mycursor.execute("select name from customers")

# Commit the transaction (optional, not needed for CREATE TABLE)
names = mycursor.fetchall()
connection.commit()
for i in names:
    print(i)

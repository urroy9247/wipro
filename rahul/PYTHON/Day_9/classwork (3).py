import mysql.connector

# Establishing a connection to the database
mydb = mysql.connector.connect(
  host="localhost",  # Your MySQL host
  user="root",   # Replace with your MySQL username
  password="rps@123",  # Replace with your MySQL password
  database="rps"  # Replace with your database name
)

# Creating a cursor object to interact with the database
mycursor = mydb.cursor()

# Executing the SQL query to create a new table
mycursor.execute("CREATE TABLE customers (name VARCHAR(15), address VARCHAR(15))")

# Commit the transaction (optional, not needed for CREATE TABLE)
mydb.commit()

# Optional: Print confirmation message
print("Table 'customers' created successfully.")
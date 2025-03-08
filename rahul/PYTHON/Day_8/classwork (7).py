import sqlite3
 
# Use 'with' to open and close the connection automatically
 
with sqlite3.connect('rps_database.db') as con:
 
    cursor = con.cursor()
 
    # Insert a record into the Students table
    stmt= " INSERT INTO Students (name, age, email)   VALUES ('Murugadoss', 45, 'murugadoss@yahoo.com'); "
 
    cursor.execute(stmt)
 
    # Commit the changes automatically
    con.commit()
 
    # No need to call connection.close(); it's done automatically!
    print("Record inserted successfully!")
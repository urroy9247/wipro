import sqlite3
 
# Use 'with' to connect to the SQLite database
with sqlite3.connect('rps_database.db') as connection:
    cursor = connection.cursor()
 
    # SQL command to update a student's age
    delete_query = " DELETE from Students WHERE name = ?; "

 
    # Data for the update
    student_name = 'Murugadoss'
 
    # Execute the SQL command with the data
    cursor.execute(delete_query, (student_name,))
 
    # Commit the changes to save the update
    connection.commit()
 
    # Print a confirmation message
    print(f"Deleted name {student_name} from table.")
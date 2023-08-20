#!/usr/bin/python3
'''
A script that selects and displays all states from the database hbtn_0e_0_usa.
'''

# Import necessary modules
import sys
import MySQLdb

if __name__ == "__main__":
    '''
    Main script to retrieve and display all states from the database.
    '''
    # Create a database connection using MySQLdb
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Execute SQL query to select all states from the "states" table
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows of the query result
    rows = cur.fetchall()

    # Iterate through the rows and print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()

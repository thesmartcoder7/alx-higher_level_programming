#!/usr/bin/python3
"""
This script retrieves and displays rows from the 'states' table of the 'hbtn_0e_0_usa'
database where the 'name' column matches the provided argument.
"""

# Import necessary modules
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Main script to retrieve and display rows from the 'states' table.
    """
    # Create a database connection using MySQLdb
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Execute SQL query to select rows from 'states' table based on the provided argument
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],)
    )

    # Fetch all rows of the query result
    rows = cur.fetchall()

    # Iterate through the rows and print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()

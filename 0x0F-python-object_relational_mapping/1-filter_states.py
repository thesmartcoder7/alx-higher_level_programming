#!/usr/bin/python3
"""
A script that selects states with names starting with "N" from the database hbtn_0e_0_usa.
"""

# Import necessary modules
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Main script to retrieve and display states with names starting with "N" from the database.
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

    # Execute SQL query to select states with names starting with "N"
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(query)

    # Fetch all rows of the query result
    rows = cur.fetchall()

    # Iterate through the rows and print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()

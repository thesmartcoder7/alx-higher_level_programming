#!/usr/bin/python3
"""
A Python script that lists all states from the database
hbtn_0e_0_usa with a given name.
"""

# Import necessary modules
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Main script to retrieve and list states with a given
    name from the database.
    """
    # Create a database connection using MySQLdb
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to select states with a given name
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(
            argv[4]
        )
    )

    # Fetch all rows of the query result
    rows = cursor.fetchall()

    # Iterate through the rows and print each row with the given name
    for row in rows:
        if row[1] == argv[4]:
            print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

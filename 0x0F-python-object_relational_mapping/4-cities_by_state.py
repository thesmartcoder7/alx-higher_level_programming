#!/usr/bin/python3
"""
This script is used to select cities by states from the
database hbtn_0e_4_usa.
"""

# Import necessary modules
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Select and print cities along with their corresponding
    states from the database.
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

    # Execute SQL query to select cities along with their corresponding states
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id ORDER \
        BY cities.id ASC"
    )

    # Fetch all rows of the query result
    rows = cur.fetchall()

    # Iterate through the rows and print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()

#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

# Import necessary modules
import sys
import MySQLdb

if __name__ == "__main__":
    """
    List all cities of a given state from the database.
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

    # Execute SQL query to select cities of the given state
    cur.execute(
        "SELECT cities.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s ORDER BY cities.id ASC", (sys.argv[4],)
    )

    # Fetch all rows of the query result
    rows = cur.fetchall()

    # Print the names of cities separated by commas
    print(", ".join([row[0] for row in rows]))

    # Close the cursor and the database connection
    cur.close()
    db.close()

#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table where name matches the argument
Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name>
"""
import sys
import MySQLdb


def filter_states():
    """
    Takes in an argument and displays all values in the states table where name matches the argument
    Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name>
    """
    try:
        user1 = sys.argv[1]
        pass1 = sys.argv[2]
        db1 = sys.argv[3]
        match = sys.argv[4]
        database = None
        c = None
        database = MySQLdb.connect(
            port=3306, host="localhost", user=user1, passwd=pass1, db=db1
        )
        c = database.cursor()
        # Using format() makes this vulnerable to SQL injection as required
        query = "SELECT * FROM states WHERE name = '{}' " \
                "ORDER BY states.id ASC".format(match)
        c.execute(query)
        [print(state) for state in c.fetchall()]
    except MySQLdb.Error as e:
        print(f"Error connecting to database, {e}")
    finally:
        if c:
            c.close()
        if database:
            database.close()


if __name__ == "__main__":
    filter_states()

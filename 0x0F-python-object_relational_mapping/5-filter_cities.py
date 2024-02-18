#!/usr/bin/python3

""" Select all states from database """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ Main function """
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                            user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    query = "SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (argv[4],))
    query_rows = cur.fetchall()
    states = [row[0] for row in query_rows]
    print(", ".join(states))
    cur.close()
    conn.close()

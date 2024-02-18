#!/usr/bin/python3

""" Select all states from database """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ Main function """
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE '{}' \
            ORDER BY states.id ASC".format(argv[4])
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

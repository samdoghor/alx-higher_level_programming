#!/usr/bin/python3
""" 0x0F-python-object_relational_mapping """

from sys import argv

import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name,
                state.name FROM states state, cities cities
                WHERE cities.state_id = state.id ORDER BY cities.id ASC""")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()

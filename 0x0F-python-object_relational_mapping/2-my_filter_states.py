#!/usr/bin/python3
""" Select and print all states  """

from sys import argv

import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    query = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(argv[4])
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()

#!/usr/bin/python3

import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

cur = db.cursor()
query = f"""SELECT * FROM states WHERE name LIKE BINARY '{argv[4]}' ORDER BY states.id ASC"""
cur.execute(query)
query_rows = cur.fetchall()
for row in query_rows:
    print(row)

cur.close()
db.close()
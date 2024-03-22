#!/usr/bin/python3
""" 0x0F-python-object_relational_mapping """

from sys import argv

import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute(
        """SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id WHERE
        states.name = %s ORDER BY cities.id ASC""", (argv[4], ))

    print(", ".join(map(lambda x: x[0], cur.fetchall())))

    cur.close()
    db.close()

#!/usr/bin/python3
"""
Lists all states with name starting with N
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()

    cur.execute("""SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name=%s""", (argv[4],))
    rows = cur.fetchall()

    ret = []
    for row in rows:
        ret.append(row[0])
    print(', '.join(ret))

    cur.close()
    db.close()

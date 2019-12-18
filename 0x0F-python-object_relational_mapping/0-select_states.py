#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    if len(argv) == 4:
        new = MySQLdb.connect(user=argv[1], passwd=argv[2],
                                port=3306, host='localhost',
                                db=argv[3])
        cursor = new.cursor()
        cursor.execute('SELECT * FROM states ORDER BY id')
        for row in cursor.fetchall():
            print(row)

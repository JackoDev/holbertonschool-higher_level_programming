#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    if len(argv) == 4:
        db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                                port=3306, host='localhost',
                                db=argv[3])
        cursor = db.cursor()
        cursor.execute('SELECT * FROM states ORDER BY state.id')
        for state in cursor.fetchall():
            print(state)
        cursor.close()
        db.close()

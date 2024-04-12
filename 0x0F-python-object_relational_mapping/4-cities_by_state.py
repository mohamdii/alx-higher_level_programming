#!/usr/bin/python3
"""Diff db"""
import sys
import MySQLdb

if __name__ == "__main__":
    dataB = MySQLdb.connect(host='localhost', db=sys.argv[3], user=sys.argv[1], passwd=sys.argv[2])
    cur = dataB.cursor()
    cur.execute('SELECT * FROM cities ORDER BY cities.id')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dataB.close()
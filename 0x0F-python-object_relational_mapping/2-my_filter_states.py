#!/usr/bin/python3
"""A scripttt"""
import MySQLdb
import sys
if __name__ == "__main__":
    dataB = MySQLdb.connect(host='localhost', db=sys.argv[3], passwd=sys.argv[2], user=sys.argv[1])
    cur = dataB.cursor()
    cur.execute('SELECT * FROM states WHERE name = "{}" ORDER BY states.id ASC;'.format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dataB.close()
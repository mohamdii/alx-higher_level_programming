#!/usr/bin/python3
"""Python script"""
import sys
import MySQLdb

if __name__ == "__main__":
    dataB = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = dataB.cursor()
    cur.execute('SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s',(sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row, end=" ")
    cur.close()
    dataB.close()
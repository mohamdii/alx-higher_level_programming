#!/usr/bin/python3
"""Its more specified and pay attention to quotes in exec"""
import MySQLdb
import sys
if __name__ == "__main__":
    dataB = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = dataB.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY states.id ASC;')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dataB.close()
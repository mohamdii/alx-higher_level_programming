#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    dataB = MySQLdb.connect(port=3306, host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = dataB.cursor()
    cur.execute('SELECT * FROM states WHERE states.id=4 OR states.id=5;')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dataB.close()
#!/usr/bin/python3
'''
A script to filters state by user inputs
'''

# import Libraries
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
FROM `states` \
WHERE BINARY `name` ='{s}'".format(sys.argv[4])
    for state in cur.fetchall():
        print(state)

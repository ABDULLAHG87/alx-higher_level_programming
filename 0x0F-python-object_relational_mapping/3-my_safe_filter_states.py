#!/usr/bin/python3
'''
 A Scipt that takes in arguments and displays all values in the states
using the SQL injection
'''

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    
    cur.execute("SELECT * FROM `states` WHERE `name` = '{}' ORDER BY `id`".format(sys.argv[4]))
    for state in cur.fetchall():
        print(state)

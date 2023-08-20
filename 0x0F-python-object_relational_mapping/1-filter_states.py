#!/usr/bin/python3
'''
A script that list all states with a nme starting with N from data base
'''

#import libraries
import sys
import MySQLdb

# Running Module as a Script

if __name__ == "__main__":
    #creating connection
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cur.fetchall() if state[1][0] == 'N']

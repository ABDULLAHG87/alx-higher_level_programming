#!/usr/bin/python3
'''
Lists all states from the database htbn_0e_0_usa
Syntax of Usage: ./0-select_states.py <mysql username>\
                                      <mysql password>\
                                      <database>
Internal connection Parameters:
    host: Localhost
    port: 3306
'''


import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]

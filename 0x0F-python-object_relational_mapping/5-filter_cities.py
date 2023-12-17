#!/usr/bin/python3
'''
 Script to display all cities of ag iven state from the
 states table of the database
'''

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                  ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([city[2] for city in cur.fetchall()
                     if city[4] == sys.argv[4]]))

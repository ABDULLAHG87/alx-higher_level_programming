#!/usr/bin/python3
'''
Script to list al citeis of the database htn_0e_4_usa
'''

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd= sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                  FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                  ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    for city in cur.fetchall():
        print(city)

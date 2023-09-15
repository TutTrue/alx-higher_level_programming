#!/usr/bin/python3
"""takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""


import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE"
                f"'{args[4]}' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == args[4]:
            print(row)
    cur.close()
    conn.close()

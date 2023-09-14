#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import MySQLdb
    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1], passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()